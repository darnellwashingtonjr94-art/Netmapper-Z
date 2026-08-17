.PHONY: install test clean docker-build

install:
	pip install -r requirements.txt

test:
	python -m unittest discover tests

clean:
	rm -rf __pycache__ */__pycache__ *.db *.json *.html

docker-build:
	docker build -t netmapper-z .
