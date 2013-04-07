hadoop-talk-s5.html: hadoop-talk.txt
	pandoc -w s5 -s $< > $@

hadoop-talk-s5-FINAL.html: hadoop-talk.txt
	pandoc -w s5 --data-dir=. --self-contained -s $< > $@

clean:
	$(RM) *.html

.DELETE_ON_ERROR:
