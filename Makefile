all: flakes test

test:
	python setup.py test

analysis:: flakes

flakes:
	@echo Searching for static errors...
	@flake8 --statistics --count readchar

coveralls::
	coveralls

publish:
	@python setup.py bdist_wheel upload
