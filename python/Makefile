.PHONY: venv


# UTILITIES
VENV = venv
PIP = pip3
PY = python3
PYTEST = py.test


# FILENAMES
VENVNAME = venv
REQUIREMENTS = requirements.txt
RESEARCH = research.py

ELLER = eller_algorithm.py
WAVE = wave_algorithm.py

MTEST_PATH = mtest_pathfinding.py
MTEST_GEN = mtest_mazegeneration.py

CHECK = check_maze.py
TESTS = tests.py

MAIN_FILES = $(ELLER) $(WAVE) $(CHECK) $(TESTS)


# TARGETS
tests: $(TESTS)
	$(PYTEST) -s -v $(TESTS)

check_tests: $(TESTS)
	$(PYTEST) -s -v -m "check_maze" $(TESTS)

eller_tests: $(TESTS)
	$(PYTEST) -s -v -m "eller" $(TESTS)

wave_tests: $(TESTS)
	$(PYTEST) -s -v -m "wave" $(TESTS)

research: $(RESEARCH)
	@$(PY) $(RESEARCH)

mtest_path: $(MTEST_PATH)
	@$(PY) $(MTEST_PATH) < mtest_path.txt

mtest_gen: $(MTEST_GEN)
	@$(PY) $(MTEST_GEN) < mtest_gen.txt


# SERVICE
venv:
	$(PY) -m $(VENV) $(VENVNAME)
	@make pull_req

freeze_requirements:
	touch $(REQUIREMENTS)
	$(PIP) freeze > $(REQUIREMENTS)

install_requirements: $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)

style: $(MAIN_FILES)
	@for file in $(MAIN_FILES) ; do \
		echo "style checking $$file" ; \
		$(PY) -m pycodestyle $$file ; \
	done

