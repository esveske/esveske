CP := copy
PY := py

progs := ast fiz mat pfe rac bio bmd glg hem ant arh ist lin psh drh
years := 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017

ALL := \
	gen/index.html \
	$(patsubst %,gen/prog-%.html,$(progs)) \
	$(patsubst %,gen/god-%.html,$(years))
	
all: $(ALL) pdfs

gen/index.html: index.html
	$(CP) $< $(subst /,\,$@)

gen/prog-%.html: prog.py prog.template.html
	$(PY) prog.py $* $@

gen/god-%.html: god.py god.template.html
	$(PY) god.py $* $@


pdfs: $(patsubst %,gen/pdf/%/.gen,2010 2011 2012)

gen/pdf/2010/.gen: pdf/2010/ps68cr.pdf pdf/2010/ps68cr.chop
	$(PY) chop.py $^ ./gen/pdf/2010 68 old
	echo "" > $@

gen/pdf/2011/.gen: pdf/2011/PS69_ZBORNIK2011.pdf pdf/2011/PS69.chop
	$(PY) chop.py $^ ./gen/pdf/2011 69 old
	echo "" > $@

gen/pdf/2012/.gen: pdf/2012/ps70_Zbornik2012_ispr.pdf pdf/2012/ps70.chop
	$(PY) chop.py $^ ./gen/pdf/2012 70 old
	echo "" > $@

.PHONY: all pdfs