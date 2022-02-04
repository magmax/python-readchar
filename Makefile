all: precommit test

test:
	python setup.py test

precommit::
	pre-commit run -a

publish:
	@python setup.py bdist_wheel upload
