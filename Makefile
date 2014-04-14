.PHONY: test
test:
	nosetests2

install:
	mkdir -p ~/.gnumeric/plugins
	test -e ~/.gnumeric/plugins/sheetmusic || ln -s "$$PWD/spellbook" ~/.gnumeric/plugins/sheetmusic
