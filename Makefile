full: lint test launch

lint:
	pre-commit run --all-files

test:
	python3 -m pytest ./model_detection/tests/

launch:
	sh ./api.sh
