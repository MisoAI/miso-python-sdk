init-env: venv/bin/activate

build: venv/bin/activate
	. venv/bin/activate; python3 setup.py sdist

clean:
	rm -r dist || true
	rm -r miso_sdk.egg-info || true

upload: venv/bin/activate dist/*.gz
	. venv/bin/activate; twine upload dist/*

deep-clean: clean
	rm -r venv || true

##################

venv/bin/activate:
	python3 -m venv venv
	. venv/bin/activate; \
		python3 -m pip install -U pip; \
		python3 -m pip install -r requirements.txt

dist/*.gz:
	make build
