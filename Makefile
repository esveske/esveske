PY := python
CP := $(PY) -c "import shutil,sys; shutil.copy(sys.argv[1],sys.argv[2])"

# all programs
progs := ast fiz mat pfe ele rac bio bmd hbh ggr glg hem ant ahl drh fan ist lin psh ska diz

# all years
years := 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019

# static pages
st_pages := style.css index.html pocetak.html stsicn.html uputstvo.html

PAGES := \
	$(patsubst %,gen/prog-%.html,$(progs)) \
	$(patsubst %,gen/god-%.html,$(years)) \
	$(patsubst %,gen/%,$(st_pages))
	
all: pdfs pages gen/sitemap.xml

pages: $(PAGES)

gen/%: static/%
	$(CP) $< $@

gen/prog-%.html: prog.py prog.template.html data.xlsx
	$(PY) prog.py $* $@

gen/god-%.html: god.py god.template.html data.xlsx
	$(PY) god.py $* $@

gen/sitemap.xml: sitemap.sh data.xlsx
	./sitemap.sh > $@


pdfs: $(patsubst %,gen/pdf/%/.gen,2010 2011 2012 2013 2014 2015 2016 2017)

gen/pdf/2010/.gen: pdf/2010/ps68cr.pdf pdf/2010/ps68cr.chop
	$(PY) chop.py $^ ./gen/pdf/2010 68 old
	echo "" > $@

gen/pdf/2011/.gen: pdf/2011/PS69_ZBORNIK2011.pdf pdf/2011/PS69.chop
	$(PY) chop.py $^ ./gen/pdf/2011 69 old
	echo "" > $@

gen/pdf/2012/.gen: pdf/2012/ps70_Zbornik2012_ispr.pdf pdf/2012/ps70.chop
	$(PY) chop.py $^ ./gen/pdf/2012 70 old
	echo "" > $@

gen/pdf/2013/.gen: pdf/2013/PS72-ZB13.pdf pdf/2013/ps72.chop
	$(PY) chop.py $^ ./gen/pdf/2013 13 new
	echo "" > $@

gen/pdf/2014/.gen: pdf/2014/ps2014.pdf pdf/2014/ps2014.chop
	$(PY) chop.py $^ ./gen/pdf/2014 14 new
	echo "" > $@

gen/pdf/2015/.gen: pdf/2015/ps2015.pdf pdf/2015/ps2015.chop
	$(PY) chop.py $^ ./gen/pdf/2015 15 new
	echo "" > $@

gen/pdf/2016/.gen: pdf/2016/ps2016.pdf pdf/2016/ps2016.chop
	$(PY) chop.py $^ ./gen/pdf/2016 16 new
	echo "" > $@

gen/pdf/2017/.gen: pdf/2017/ps2017.pdf pdf/2017/ps2017.chop
	$(PY) chop.py $^ ./gen/pdf/2017 17 new
	echo "" > $@

deploy: all
	cd gen; git commit -am 'deploy'; git push

.PHONY: all pdfs deploy pages