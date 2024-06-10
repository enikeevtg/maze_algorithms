.PHONY: venv

#
PY = python3
PIP = pip3
VENV = venv

# filenames
TEST = test.py
VENVNAME = venv
REQUIREMENTS = requirements.txt

test: $(TEST)
	$(PY) $(TEST) < test.txt

venv:
	$(PY) -m $(VENV) $(VENVNAME)


# service
create_req:
	touch $(REQUIREMENTS)
	$(PIP) freeze > $(REQUIREMENTS)

req: $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

style:
	$(PY) -m pycodestyle *.py
