# Makefile

# Root directory of your project
ROOT_DIR := services/

# Target to install requirements from all requirements.txt files
install-reqs:
	@cd $(ROOT_DIR) && \
	find . -name 'requirements.txt' -exec pip install -r {} \;

run:
	docker-compose up --build

.PHONY: install-reqs
