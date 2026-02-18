PYTHON ?= python3

.PHONY: all clean test test-unit test-integration test-snapshot test-e2e

all: test

test: test-unit test-integration test-snapshot test-e2e

clean:
	@echo "No build artifacts to clean yet"

test-unit:
	$(PYTHON) -m unittest discover -s tests/unit -v

test-integration:
	$(PYTHON) -m unittest discover -s tests/integration -v

test-snapshot:
	$(PYTHON) -m unittest discover -s tests/snapshot -v

test-e2e:
	$(PYTHON) -m unittest discover -s tests/e2e -v
