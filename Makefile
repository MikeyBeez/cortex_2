# /Users/bard/Code/cortex_2/Makefile
.PHONY: help setup test test-quick test-cov lint format clean install-mcp docs

help:  ## Show this help
	@echo "Cortex_2 Development Commands"
	@echo "============================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup:  ## Set up development environment with uv
	./setup.sh

test:  ## Run all tests
	uv run python run_tests.py

test-quick:  ## Run quick unit tests only
	uv run python run_tests.py quick

test-cov:  ## Run tests with coverage report
	uv run pytest tests/ --cov=cortex --cov-report=html --cov-report=term

lint:  ## Run linting
	uv run ruff check src/
	uv run mypy src/

format:  ## Format code
	uv run black src/ tests/
	uv run ruff check --fix src/

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

install-mcp:  ## Build and install MCP server
	cd mcp_server && npm install && npm run build
	@echo "Add to Claude with:"
	@echo "claude mcp add cortex -s user -- node $(PWD)/mcp_server/dist/index.js"

docs:  ## Serve documentation locally
	cd documentation && uv run python -m http.server 8000

dev:  ## Start development server
	uv run uvicorn cortex.app:app --reload --host 0.0.0.0 --port 8000

module-create:  ## Create a new module template
	@read -p "Module name: " name; \
	uv run python -m cortex.cli module create $$name

module-list:  ## List all modules
	uv run python -m cortex.cli module list

module-test:  ## Test module loading
	@read -p "Module ID: " id; \
	uv run python -m cortex.cli module test $id

service-install:  ## Install Cortex as a macOS service
	chmod +x manage_service.sh
	./manage_service.sh install

service-uninstall:  ## Uninstall Cortex service
	./manage_service.sh uninstall

service-start:  ## Start Cortex service
	./manage_service.sh start

service-stop:  ## Stop Cortex service
	./manage_service.sh stop

service-restart:  ## Restart Cortex service
	./manage_service.sh restart

service-status:  ## Check Cortex service status
	./manage_service.sh status

service-logs:  ## Tail Cortex service logs
	./manage_service.sh logs

service-errors:  ## Tail Cortex service error logs
	./manage_service.sh errors

run:  ## Run any command with uv
	uv run $(filter-out $@,$(MAKECMDGOALS))

# Allow any arguments after 'make run'
%:
	@:
