# class EllerAlgorithm
# в окончательной версии:
#  - удалить методы распечатки лабиринта
#  - в методе __init__ убрать выброс исключения, если из фронта
#    точно придёт валидный запрос на генерацию лабиринта?

from random import choice
import maze_constants as c


EMPTY_SET = 0


class EllerAlgorithm:

    '''Maze generation Eller's algorithm'''

    @staticmethod
    def maze_representation(rows, cols, right_walls, down_walls):
        '''Maze representation static method'''
        for i in range(cols):
            print(' _', end='')
        print()
        for i in range(rows):
            print('|', end='')
            for j in range(cols):
                print(('_' if down_walls[i][j] == c.WALL else ' '), end='')
                print(('|' if right_walls[i][j] == c.WALL else ' '), end='')
            print()

    def print_maze(self):
        '''Maze representation method'''
        self.maze_representation(self.rows, self.cols, self.right_walls,
                                 self.down_walls)

    def generate_maze(self, rows, cols) -> tuple:
        '''Perfect maze generation by Eller's algorithm method

        Return tuple of two matrices. Each matrix contains data about walls:
        right (vertical) walls and down (horizontal) walls
        '''
        self.__initial_data_validation(rows, cols)
        self.rows = rows
        self.cols = cols
        self.right_walls, self.down_walls = self.__walls_matrices_init()
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

    def __initial_data_validation(self, rows, cols):
        if rows < 1 or cols < 1:
            raise ValueError('Maze must has positive value dimensions')

    def __walls_matrices_init(self):
        right_walls = [[c.PASS if i < self.cols - 1 else c.WALL
                        for i in range(self.cols)] for _ in range(self.rows)]
        down_walls = [[c.PASS for _ in range(self.cols)]
                      if i < self.rows - 1 else
                      [c.WALL for _ in range(self.cols)]
                      for i in range(self.rows)]
        return right_walls, down_walls

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
                self.right_walls[row][col] = c.WALL
            else:
                self.right_walls[row][col] = choice([c.PASS, c.WALL])

            if self.right_walls[row][col] == c.PASS and \
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
            self.down_walls[row][col] = choice([c.PASS, c.WALL])
            if self.down_walls[row][col] == c.PASS:
                sets_info[set_]['pass'] = True
            else:
                sets_info[set_]['walls'].append(col)

        for set_, info_ in sets_info.items():
            if info_['pass'] is False:
                col = choice(info_['walls'])
                self.down_walls[row][col] = c.PASS

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
                self.right_walls[row][col] = c.PASS
                line = list(map((lambda x: line[col] if x == line[col + 1]
                                 else x), line))
            else:
                self.right_walls[row][col] = c.WALL


if __name__ == "__main__":
    print(EllerAlgorithm.__doc__)
