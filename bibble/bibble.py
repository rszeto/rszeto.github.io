import sys
from pybtex.database.input import bibtex
from pybtex.database import BibliographyData, FieldDict, Entry
import jinja2
import jinja2.sandbox
import re
from calendar import month_name
import os
import argparse
import re

_months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
}

_bolded_author = {
    'first': 'Ryan',
    'last': 'Szeto'
}

# List of fields to not print in the publicly available BibTeX source
_ignore_fields_bibtex_source = ['url', 'key']

def _author_fmt(author):
    author_name = u' '.join(author.first() + author.middle() + author.last())
    if author.first()[0] == _bolded_author['first'] and author.last()[0] == _bolded_author['last']:
        return '<strong>' + author_name + '</strong>'
    else:
        return author_name

def _andlist(ss, sep=', ', seplast=', and ', septwo=' and '):
    if len(ss) <= 1:
        return ''.join(ss)
    elif len(ss) == 2:
        return septwo.join(ss)
    else:
        return sep.join(ss[:-1]) + seplast + ss[-1]

def _author_list(authors):
    return _andlist(map(_author_fmt, authors))

def _venue_type(entry):
    venuetype = ''
    if entry.type == 'inbook':
        venuetype = 'Chapter in '
    elif entry.type == 'techreport':
        venuetype = 'Technical Report '
    elif entry.type == 'phdthesis':
        venuetype = 'Ph.D. thesis, {}'.format(entry.fields['school'])
    return venuetype

def _venue(entry):
    f = entry.fields
    venue = ''
    if entry.type == 'article':
        venue = f['journal']
        try:
            if f['volume'] and f['number']:
                venue += ' {0}({1})'.format(f['volume'], f['number'])
        except KeyError:
            pass
    elif entry.type == 'inproceedings':
        venue = f['booktitle']
        try:
            if f['series']:
                venue += ' ({})'.format(f['series'])
        except KeyError:
            pass
    elif entry.type == 'inbook':
        venue = f['title']
    elif entry.type == 'techreport':
        venue = '{0}, {1}'.format(f['number'], f['institution'])
    elif entry.type == 'phdthesis':
        venue = ''
    else:
        venue = 'Unknown venue (type={})'.format(entry.type)
    return venue

def _title(entry):
    if entry.type == 'inbook':
        title = entry.fields['chapter']
    else:
        title = entry.fields['title']

    # remove curlies from titles -- useful in TeX, not here
    title = title.translate(None, '{}')
    return title

def _main_url(entry):
    urlfields = ('url', 'ee')
    for f in urlfields:
        if f in entry.fields:
            return entry.fields[f]
    return None

def _extra_urls(entry):
    """Returns a dict of URL types to URLs, e.g.
       { 'nytimes': 'http://nytimes.com/story/about/research.html',
          ... }
    """
    urls = {}
    for k, v in entry.fields.iteritems():
        if not k.endswith('_url'):
            continue
        k = k[:-4]
        urltype = k.replace('_', ' ')
        urls[urltype] = v
    return urls

def _month_match (mon):
    if re.match('^[0-9]+$', mon):
        return int(mon)
    return _months[mon.lower()[:3]]

def _month_name (monthnum):
    try:
        return month_name[int(monthnum)]
    except:
        return ''

def _sortkey(entry):
    e = entry.fields
    year =  '{:04d}'.format(int(e['year']))
    try:
        monthnum = _month_match(e['month'])
        year += '{:02d}'.format(monthnum)
    except KeyError:
        year += '00'
    return year

def main(bibfile, template, save_path, save_individual=False):
    # Make sure save_path is a directory if save_individual, and a valid file path otherwise
    if save_individual and not os.path.isdir(save_path):
        print('save_individual is true, but save_path is not a directory. Quitting')
        return
    elif not save_individual and not os.path.isdir(os.path.abspath(os.path.dirname(save_path))):
        print('save_individual is false, but save_path is not a valid file location. Quitting')
        return
    
    # Load the template.
    tenv = jinja2.sandbox.SandboxedEnvironment()
    tenv.filters['author_fmt'] = _author_fmt
    tenv.filters['author_list'] = _author_list
    tenv.filters['title'] = _title
    tenv.filters['venue_type'] = _venue_type
    tenv.filters['venue'] = _venue
    tenv.filters['main_url'] = _main_url
    tenv.filters['extra_urls'] = _extra_urls
    tenv.filters['monthname'] = _month_name
    with open(template) as f:
        tmpl = tenv.from_string(f.read())

    # Parse the BibTeX file.
    with open(bibfile) as f:
        db = bibtex.Parser().parse_stream(f)

    for k, v in db.entries.items():
        # Include the bibliography key in each entry.
        v.fields['key'] = k
        # Include the full BibTeX in each entry, minus fields to ignore
        filtered_v_field_items = filter(lambda x: x[0] not in _ignore_fields_bibtex_source, v.fields.items())
        filtered_v = Entry(v.type, fields=filtered_v_field_items, persons=v.persons)
        v.fields['bibtex'] = BibliographyData({k: filtered_v}).to_string('bibtex').strip()
        # Replace ' = "XXX"' with '={XXX}'
        v.fields['bibtex'] = re.sub(r' = \"(.*)\"', r'={\1}', v.fields['bibtex'])

    # Render the template.
    bib_sorted = sorted(db.entries.values(), key=_sortkey, reverse=True)
    if save_individual:
        for bib in bib_sorted:
            out = tmpl.render(entry=bib)
            file_path = os.path.join(save_path, '%s.html' % bib.key)
            with open(file_path, 'w') as f:
                f.write(out)
    else:
        out = tmpl.render(entries=bib_sorted)
        with open(save_path, 'w') as f:
            f.write(out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('bibfile', type=str, help='The .bib file with references')
    parser.add_argument('template', type=str, help='The HTML template')
    parser.add_argument('save_path', type=str, help='The output file if save_individual is not specified; the directory to store output files otherwise')
    parser.add_argument('--save_individual', action='store_true', help='Whether to save all references in one HTML file or generate multiple files')
    
    args = parser.parse_args()
    main(args.bibfile, args.template, args.save_path, args.save_individual)