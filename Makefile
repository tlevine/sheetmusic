.PHONY: test install

test:
	nosetests2

install:
	./link

run:
	export PYTHONPATH=$$PWD
	gnumeric
