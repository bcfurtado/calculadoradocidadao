.PHONY: tests

start:
	export FLASK_APP=calculadoradocidadao/site.py; python -m flask run

tests:
	coverage run -m unittest discover
	coverage xml
	coverage report -m
