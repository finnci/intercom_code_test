docker_build:
	docker build -t intercom_test .
test:
	python tests.py
