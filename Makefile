.PHONY: help install run lint

help: 
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

BIN = docker run \
	--interactive \
	--rm \
	-v "/code" \
	--name quarto-python \
	quarto-python

install: ## Install docker environnement
	docker build --tag=quarto-python .

install-local:
	pip install -r requirements.txt

run: ## Start the game
	 $(BIN) python ./src/quarto.py

test: ## Test the code
	$(BIN) python3 -m unittest discover

test-local:
	python3 -m unittest discover

lint: ## Check the code syntax and rules
	$(BIN) pycodestyle /code --max-line-length=150

.DEFAULT_GOAL := help
