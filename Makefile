docker_build:
	make test
	docker build -t intercom_test .
test:
	python tests.py
