init-env: venv/bin/activate

build: venv/bin/activate
	. venv/bin/activate; python3 setup.py sdist

clean:
	rm -r venv || true
	rm -r dist || true
	rm -r miso_sdk.egg-info || true

upload: build
	. venv/bin/activate; twine upload dist/*

##################

venv/bin/activate:
	python3 -m venv venv
	. venv/bin/activate; \
		python3 -m pip install -U pip; \
		python3 -m pip install -r requirements.txt
