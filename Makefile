.PHONY: tests build readchar


# default target:
all: tests pre-commit build

test tests:
	@pytest

pre-commit precommit:
	@pre-commit run -a

build pack readchar:
	@python setup.py sdist bdist_wheel
