venv_pluton/bin/python: venv_pluton setup.py
	./venv_pluton/bin/python setup.py develop
	@touch venv_pluton/bin/python

venv_pluton:
	virtualenv3 venv_pluton
