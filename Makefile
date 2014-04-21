.PHONY: test install

test:
	nosetests2

run:
	export PYTHONPATH=$$PWD
	gnumeric
