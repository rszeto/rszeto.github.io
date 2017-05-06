PYTHON=python

# targets that aren't filenames
.PHONY: all clean

all: _includes/pubs _includes/pubs/all-pubs.html

_includes/pubs/all-pubs.html: _bib/pubs.bib _bib/all-publications.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py $+ $@

_includes/pubs: _bib/pubs.bib _bib/one-publication.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py $+ $@ --save_individual

clean:
	$(RM) -r _site _includes/pubs
