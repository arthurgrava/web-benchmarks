clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name "dist" -type d | xargs rm -rf
	@find . -name "htmlcov" | xargs rm -rf
	@find . -name ".coverage" | xargs rm -rf
	@find . -name ".pytest_cache" | xargs rm -rf
	@find . -name ".cache" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "*.egg-info" | xargs rm -rf
	@find . -name "build" | xargs rm -rf
