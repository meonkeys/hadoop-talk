name = hadoop-talk

$(name)-s5.html: $(name).txt
	pandoc -w s5 -s $< > $@

$(name)-s5-FINAL.html: $(name).txt
	pandoc -w s5 --data-dir=. --self-contained -s $< > $@

publish-slideshow: $(name)-s5-FINAL.html
	git checkout gh-pages
	mv $(name)-s5-FINAL.html index.html
	git commit -m 'generate new slideshow' index.html
	@echo -------
	@echo to publish to http://meonkeys.github.io/$(name)/ , run
	@echo
	@echo     git push origin gh-pages
	@echo
	@echo -------

clean:
	$(RM) *.html

.DELETE_ON_ERROR:
