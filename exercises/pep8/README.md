# PEP-8
[![Build Status](https://travis-ci.com/bharris47/niko-exercises.svg?branch=master)](https://travis-ci.com/bharris47/niko-exercises)

## Context

[PEP-8](https://www.python.org/dev/peps/pep-0008/) is the standard style guide for Python. Code is read more often than written and therefore should be easy to read. Adhering to PEP-8 makes your code more consistent and easier for others to collaborate on. PEP-8 has rules for a variety of style issues including whitespace and variable naming.

## Objective

This exercise is meant to get you familiar with identifying and writing PEP-8 compliant code. Eventually, non-compliant code should stand out to you intuitively.

There is a module in the 01_pep8 package called name_generator.py. This file is not currently PEP-8 compliant. Your job is to correct all the PEP-8 compliancy issues and create a Pull Request with the fixed code.

Also make sure to update any tests to reflect changes to the code.

## Hints

PyCharm has tools to make this really simple. Check out the `Code` menu as well as the `Refactor` menu.

Instead of pushing to Gitlab and letting the CI run the tests, you can verify PEP-8 compliance and run tests locally.

```bash
pylint exercises/
pytest
```