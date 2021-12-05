.ONESHELL:
.PHONY: setup_env example run test
PROJECT_NAME=placeholder

CONDA_ROOT=$(shell conda info --root)
BINARIES = ${CONDA_ROOT}/envs/${PROJECT_NAME}/bin

setup_env:
	@echo ">>> Creating conda environment." \
	conda env create --name $(PROJECT_NAME) -f environment.yaml --force \

remove_env:
	conda env remove -n $(PROJECT_NAME)
example:
	@echo "Run example script"
	${BINARIES}/python -m src.example.run_example

test:
	@echo "Running all unit tests.."
	python -m pytest tests/

run: example test
