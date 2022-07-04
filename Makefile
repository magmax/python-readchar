all: test precommit pack

test:
	@pytest

precommit:
	@pre-commit run -a

pack:
	@python setup.py sdist bdist_wheel
