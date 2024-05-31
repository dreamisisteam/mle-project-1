full: pre-commit test launch

pre-commit:
	pre-commit run --all-files

test:
	python3 -m pytest ./model_detection/tests/

launch:
	sh ./api.sh
