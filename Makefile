all: test precommit

test:
	@pytest

precommit:
	@pre-commit run -a

publish:
	@python setup.py bdist_wheel upload
