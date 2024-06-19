# class EllerAlgorithm
from random import randint, choice

PASS = 0
WALL = 1
EMPTY_SET = 0


class EllerAlgorithm:

    '''Maze generation Eller's algorithm'''

    def __init__(self, h: int, w: int) -> None:
        '''EllerAlgorithm class constructor'''
        if h < 1 or w < 1:
            raise ValueError('Maze must has non-zero dimensions')

        self.rows = h
        self.cols = w
        self.right_walls = [[PASS if i < w - 1 else WALL for i in range(w)]
                            for _ in range(h)]
        self.down_walls = [[PASS for _ in range(w)] if i < h - 1 else
                           [WALL for _ in range(w)] for i in range(h)]

    @staticmethod
    def maze_representation(rows, cols, right_walls, down_walls):
        '''Maze representation static method'''
        for i in range(cols):
            print(' _', end='')
        print()
        for i in range(rows):
            print('|', end='')
            for j in range(cols):
                print(('_' if down_walls[i][j] == WALL else ' '), end='')
                print(('|' if right_walls[i][j] == WALL else ' '), end='')
            print()

    def print_maze(self):
        '''Maze representation method'''
        self.maze_representation(self.rows, self.cols, self.right_walls,
                                 self.down_walls)

    def generate_maze(self) -> tuple:
        '''Perfect maze generation by Eller's algorithm method

        Return tuple of two matrices. Each matrix contains data about walls:
        right (vertical) walls and down (horizontal) walls
        '''
        # if user request maze one of dimenseions of which equals 1
        if self.rows == 1 or self.cols == 1:
            return (self.right_walls, self.down_walls)

        line = [EMPTY_SET for _ in range(self.cols)]
        self.__set_number = EMPTY_SET + 1

        for row in range(self.rows - 1):
            line = self.__empty_cells_filling(line)
            line = self.__right_walls_generator(row, line)
            self.__down_walls_generator(row, line)
            line = self.__cells_cleaning(row, line)

        line = self.__empty_cells_filling(line)
        self.__bottom_line_generator(line)

        return (self.right_walls, self.down_walls)

    def __empty_cells_filling(self, line) -> list:
        '''Empty cells in current line filling by unique number'''
        for i in range(self.cols):
            if line[i] == 0:
                line[i] = self.__set_number
                self.__set_number += 1
        return line

    def __right_walls_generator(self, row, line) -> list:
        '''Right walls in the row generating method'''
        for col in range(self.cols - 1):
            if line[col] == line[col + 1]:
                self.right_walls[row][col] = WALL
            else:
                self.right_walls[row][col] = choice([PASS, WALL])

            if self.right_walls[row][col] == PASS and \
               line[col] != line[col + 1]:
                line = self.__cells_union(line[col + 1], line[col], line)

        return line

    def __cells_union(self, src, dest, line) -> list:
        '''Connected cells sets union'''
        # for col in range(self.cols):
        #     if line[col] == src:
        #         line[col] = dest
        # return line
        return list(map((lambda x: dest if x == src else x), line))

    def __down_walls_generator(self, row, line) -> None:
        '''Down walls under the row generating method'''
        sets_info = dict()  # {col: {'pass': True/False, 'walls': []}}

        for col in range(self.cols):
            set_ = line[col]
            sets_info[set_] = sets_info.get(set_, {'pass': False, 'walls': []})
            self.down_walls[row][col] = choice([PASS, WALL])
            if self.down_walls[row][col] == PASS:
                sets_info[set_]['pass'] = True
            else:
                sets_info[set_]['walls'].append(col)

        for set_, info_ in sets_info.items():
            if info_['pass'] is False:
                col = choice(info_['walls'])
                self.down_walls[row][col] = PASS

    def __cells_cleaning(self, row, line) -> list:
        '''Cells with walls under it cleaning method'''
        for col in range(self.cols):
            if self.down_walls[row][col] == 1:
                line[col] = EMPTY_SET
        return line

    def __bottom_line_generator(self, line):
        '''Maze bottom line generation method'''
        row = self.rows - 1
        for col in range(self.cols - 1):
            if line[col] != line[col + 1]:
                self.right_walls[row][col] = PASS
                line = list(map((lambda x: line[col] if x == line[col + 1]
                                 else x), line))
            else:
                self.right_walls[row][col] = WALL


if __name__ == "__main__":
    pass
