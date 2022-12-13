init-env:
	python3 -m venv venv
	. venv/bin/activate; \
		python3 -m pip install -U wheel setuptools pip; \
		python3 -m pip install -r requirements.txt
