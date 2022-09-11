# Contributing to readchar

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to this GitHub project. These are
mostly guidelines, not rules. Use your best judgment, and feel free to propose changes
to this document in a pull request.

## Opening an issue

If you want to open an issue about a problem or bug you encountered, simply go to the
GitHub page and click _New issue_ in the _issues_ section. You will be presented with
templates to use, choose a relevant one. (If no template fits, you can open a blank
issue. But make sure you input all the appropriate information!)

Fill out the template. You should at least provide the following information:

- a short but exact description of your problem (screenshots often help)
- steps on how to reproduce the problem
- Information about your system:
  - your OS
  - your Python version and implementation
  - the version of readchar you use

## Opening a pull request

Follow these steps if you want to contribute code to the project:

1. Fork this Git repository and create your branch from `master`.

1. Check out the code to your local machine by following the steps in
   [Getting the code](#getting-the-code) and make your changes.

1. **Make sure the tests pass!!**

1. If you added to the source code, add tests for your new code.

1. Update the documentation, if necessary.

1. Write a
   [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html),
   if you have multiple changes, make sure your commits are atomic (single irreducible
   change that makes sense on its own)

1. Done, you can open a pull request.

## Getting the code

If you want to experiment with the code yourself, you can get started by following these
steps.

1. Clone the repository.

   ```bash
   git clone https://github.com/magmax/python-readchar.git
   ```

1. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

1. Enter the virtual environment

   on Linux systems:

   ```bash
   source .venv/bin/activate
   ```

   or for Windows systems:

   ```bash
   .venv\Scripts\activate
   ```

1. Install dev-dependencies (this also automatically installs the library in editable mode)

   ```bash
   pip install -r requirements.txt
   ```

### Run the tests!

Always make sure all tests pass before suggesting any changes! This will avoid invalid
PR's.

The simplest way is to just run `make`. The provided makefile calls all tests for you.

```bash
make
```

If you don't have `make`, you could run all tests manually like this:

- run `pytest` (source-code testing)

  ```bash
  pytest
  ```

- run `pre-commit` (linting and styling)

  ```bash
  pre-commit run -a
  ```

- run `setup.py` (to test build process)

  ```bash
  python setup.py sdist bdist_wheel
  ```
