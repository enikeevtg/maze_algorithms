import pytest
import re
import maze_constants as c
from check_maze import check_maze
from wave_algorithm import WaveAlgorithm
from eller_algorithm import EllerAlgorithm


tests_dir = "test_cases/"
check_maze_tc_file = tests_dir + "check_maze_tests.txt"
eller_tc_file = tests_dir + "ellers_algorithm_tests.txt"
wave_tc_file = tests_dir + "wave_algorithm_tests.txt"


# check loops and isolations tests
def get_walls_matrix(lines, rows, cols):
    walls_matrix = [[] for _ in range(rows)]
    for i in range(rows):
        line = next(lines)
        walls_matrix[i] = list(map(int, line.split()))
        if len(walls_matrix[i]) != cols:
            raise ValueError("elements out of matrix range")
    return walls_matrix


def get_check_maze_tc(lines):
    '''Test case from file parser'''
    next(lines)  # ========================================
    name = next(lines).rstrip()
    rows, cols = tuple(map(int, next(lines).split()))
    next(lines)  # right walls:
    r_w = get_walls_matrix(lines, rows, cols)
    next(lines)  # down walls:
    d_w = get_walls_matrix(lines, rows, cols)
    check = next(lines).split(': ')[1]
    # maze visual representation
    for _ in range(rows + 1):
        next(lines)
    return {"tc_name": name, "rows": rows, "cols": cols,
            "right_walls": r_w, "down_walls": d_w, "expected_output": check}


def get_check_maze_tcs():
    '''Check maze test cases file parser'''
    tcs = []
    with open(check_maze_tc_file, "r") as file:
        lines = (line.rstrip() for line in file)
        while True:
            try:
                tcs.append(get_check_maze_tc(lines))
            except StopIteration:
                break
    return tcs


def idfn_check_maze_tc(tc: dict):
    return f"""{tc["tc_name"]},{tc["rows"]}x{tc["cols"]},""" + \
           f"""{tc["expected_output"]}"""


@pytest.fixture(scope="module", params=get_check_maze_tcs(),
                ids=idfn_check_maze_tc)
def param_check_maze_tcs(request):
    return request.param


@pytest.mark.check_maze
def test_check_maze(param_check_maze_tcs):
    tc = param_check_maze_tcs
    rows = tc["rows"]
    cols = tc["cols"]
    right_walls = tc["right_walls"]
    down_walls = tc["down_walls"]
    output = check_maze(rows, cols, right_walls, down_walls)
    assert output == tc["expected_output"]


# eller algorithm tests
def get_eller_tcs():
    '''Eller's algorithm test cases file parser'''
    tcs = []
    with open(eller_tc_file, "r") as fp:
        for tc in fp.readlines():
            rows, cols = map(int, tc.split())
            tcs.append((rows, cols))
    return tcs


def idfn_eller_tc(tc):
    return f"""rows={tc[c.ROW]},cols={tc[c.COL]}"""


@pytest.fixture(scope="module", params=get_eller_tcs(),
                ids=idfn_eller_tc)
def param_eller_tcs(request):
    return request.param


@pytest.mark.eller
def test_eller(param_eller_tcs):
    maze = EllerAlgorithm()
    rows, cols = param_eller_tcs
    r_walls, d_walls = maze.generate_maze(rows, cols)
    # print()
    # maze.print_maze()
    assert check_maze(rows, cols, r_walls, d_walls) == c.PERFECT


# eller algorithm exceptions tests
eller_exeption_tcs = [(-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]


def idfn_eller_exception_tc(tc):
    return f"""rows={tc[c.ROW]},cols={tc[c.COL]}"""


@pytest.fixture(scope="module", params=eller_exeption_tcs,
                ids=idfn_eller_exception_tc)
def param_eller_exceptions_tcs(request):
    return request.param


@pytest.mark.eller
def test_eller_exceptions_1(param_eller_exceptions_tcs):
    rows, cols = param_eller_exceptions_tcs
    with pytest.raises(ValueError):
        maze = EllerAlgorithm()
        maze.generate_maze(rows, cols)


def idfn_eller_exception_rows(val):
    return f"""(rows={val})"""


def idfn_eller_exception_cols(val):
    return f"""(cols={val})"""


@pytest.mark.eller
@pytest.mark.parametrize("cols", [-1, 0, 1], ids=idfn_eller_exception_cols)
@pytest.mark.parametrize("rows", [-1, 0, 1], ids=idfn_eller_exception_rows)
def test_eller_exceptions_2(rows, cols):
    if rows <= 0 or cols <= 0:
        with pytest.raises(ValueError):
            maze = EllerAlgorithm()
            maze.generate_maze(rows, cols)


# wave algorithm tests
def get_path_from_line(line):
  line = re.split(r'''[ ,\[\(\)\]\n]''', line.strip('path = '))
  line = list(filter(lambda x: len(x) > 0, line))
  line = list(map(int, line))
  path = []
  for i in range(0, len(line) - 1, 2):
    path.append((line[i], line[i + 1]))
  return path


def get_wave_tc(lines):
    '''Test case from file parser'''
    next(lines)  # ========================================
    name = next(lines).rstrip()
    rows, cols = tuple(map(int, next(lines).split()))
    next(lines)  # right walls:
    r_w = get_walls_matrix(lines, rows, cols)
    next(lines)  # down walls:
    d_w = get_walls_matrix(lines, rows, cols)
    next(lines)  # start:
    start = tuple(map(int, next(lines).split()))
    next(lines)  # finish:
    finish = tuple(map(int, next(lines).split()))
    path = get_path_from_line(next(lines))
    # maze visual representation
    for _ in range(rows + 1):
        next(lines)
    # print({"tc_name": name, "rows": rows, "cols": cols,
    #         "right_walls": r_w, "down_walls": d_w,
    #         "start": start, "finish": finish, "expected_output": path})
    return {"tc_name": name, "rows": rows, "cols": cols,
            "right_walls": r_w, "down_walls": d_w,
            "start": start, "finish": finish, "expected_output": path}


def get_wave_tcs():
    '''Wave algorithm test cases file parser'''
    wave_tcs = []
    with open(wave_tc_file, "r") as file:
        lines = (line.rstrip() for line in file)
        while True:
            try:
                wave_tcs.append(get_wave_tc(lines))
            except StopIteration:
                break
    return wave_tcs


def idfn_wave_tc(tc):
    return f"""{tc["tc_name"]},{tc["rows"]}x{tc["cols"]}"""


@pytest.fixture(scope="module", params=get_wave_tcs(), ids=idfn_wave_tc)
def param_wave_tcs(request):
    return request.param


@pytest.mark.wave
def test_wave(param_wave_tcs):
    tc = param_wave_tcs
    rows = tc["rows"]
    cols = tc["cols"]
    right_walls = tc["right_walls"]
    down_walls = tc["down_walls"]
    solve = WaveAlgorithm(rows, cols, right_walls, down_walls)

    start = tc["start"]
    finish = tc["finish"]
    path = solve.get_path(start, finish)
    assert path == tc["expected_output"]
