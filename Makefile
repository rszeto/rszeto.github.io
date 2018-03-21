PYTHON=python

# targets that aren't filenames
.PHONY: all clean

all: _includes/pubs _includes/pubs/all-pubs.html _includes/pubs/all-preprints.html

_includes/pubs/all-pubs.html: _pub/pubs.bib _pub/all-publications.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py $+ $@

_includes/pubs/all-preprints.html: _pub/preprints.bib _pub/all-publications.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py $+ $@

_includes/pubs: _pub/pubs.bib _pub/preprints.bib _pub/one-publication.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py _pub/pubs.bib _pub/one-publication.tmpl _includes/pubs --save_individual
	$(PYTHON) bibble/bibble.py _pub/preprints.bib _pub/one-publication.tmpl _includes/pubs --save_individual

clean:
	$(RM) -r _site _includes/pubs
