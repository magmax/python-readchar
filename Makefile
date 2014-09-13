all: flakes test

test:: run_unit_tests run_acceptance_tests

unit_test:: run_unit_tests

acceptance_test:: run_acceptance_tests

analysis:: flakes

flakes:
	@echo Searching for static errors...
	@flake8 --statistics --count readchar

coveralls::
	coveralls

run_unit_tests:
	@echo Running Tests...
	@py.test --cov readchar tests/unit

run_acceptance_tests:
	@echo Running Tests...
	@py.test tests/acceptance

publish:
	@python setup.py sdist --formats zip,gztar bdist_wheel upload
