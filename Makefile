PYTHON=python

# targets that aren't filenames
.PHONY: all clean

all: _includes/pubs/all-pubs.html

_includes/pubs/all-pubs.html: _bib/pubs.bib _bib/all-publications.tmpl
	mkdir -p _includes/pubs
	$(PYTHON) bibble/bibble.py $+ > $@

clean:
	$(RM) -r _site _includes/pubs/all-pubs.html
