.PHONY: venv

#
PY = python3
PIP = pip3
VENV = venv

# filenames
TEST = test.py
RESEARCH = research.py
VENVNAME = venv
REQUIREMENTS = requirements.txt

test: $(TEST)
	$(PY) $(TEST) < test.txt

research: $(RESEARCH)
	$(PY) $(RESEARCH)

# service
venv:
	$(PY) -m $(VENV) $(VENVNAME)
	@make pull_req

push_req:
	touch $(REQUIREMENTS)
	$(PIP) freeze > $(REQUIREMENTS)

pull_req: $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

style:
	$(PY) -m pycodestyle wave_algorithm.py
