start:
	export FLASK_APP=calculadoradocidadao/site.py; python -m flask run

tests:
	python -m test.test_index
