.PHONY: install run test lint

BIN = docker run \
			--interactive \
			--rm \
			-v "/code" \
			--name quarto-python \
			quarto-python

# Initialization ===============================================================

install:
	docker build --tag=quarto-python .

# Run ===============================================================

run:
	 $(BIN) #./src/quarto.py

# Lint ===============================================================

lint:
	$(BIN) pep8 /code --max-line-length=150