.PHONY: venv

#
PY = python3
PIP = pip3
VENV = venv

# filenames
TEST_PATH = test_pathfinding.py
TEST_MAZEGEN = test_mazegeneration.py
RESEARCH = research.py
VENVNAME = venv
REQUIREMENTS = requirements.txt

test_path: $(TEST_PATH)
	$(PY) $(TEST_PATH) < test_path.txt

test_mazegen: $(TEST_MAZEGEN)
	$(PY) $(TEST_MAZEGEN) < test_gen.txt

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
	$(PY) -m pycodestyle wave_algorithm.py eller_algorithm.py
