#################################################################################
#
# Makefile to build the project
#
#################################################################################

PROJECT_NAME = de-review
REGION = eu-west-2
PYTHON_INTERPRETER = python
WD=$(shell pwd)
PYTHONPATH=${WD}
SHELL := /bin/bash
PROFILE = default
PIP:=pip

## Create python interpreter environment.
create-environment:
	@echo ">>> About to create environment: $(PROJECT_NAME)..."
	@echo ">>> check python3 version"
	( \
		$(PYTHON_INTERPRETER) --version; \
	)
	@echo ">>> Setting up VirtualEnv."
	( \
	    $(PIP) install -q virtualenv virtualenvwrapper; \
	    virtualenv venv --python=$(PYTHON_INTERPRETER); \
	)

# Define utility variable to help calling Python from the virtual environment
ACTIVATE_ENV := source venv/bin/activate

# Execute python related functionalities from within the project's environment
define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

################################################################################################################
# Set Up
## Install flake8
flake:
	$(call execute_in_env, $(PIP) install flake8)

## Install pytest
pytest:
	$(call execute_in_env, $(PIP) install pytest)

## Run the flake8 code check
run-flake:
	$(call execute_in_env, flake8 \
	./src/section1/*.py \
	./src/section2/*.py \
	./src/section3/*.py \
	)
## Run a single test
unit-test:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v ${test_run})

## Run all the unit tests
unit-tests:
	$(call execute_in_env, PYTHONPATH=${PYTHONPATH} pytest -v)

## Run all checks
run-checks: run-flake unit-tests