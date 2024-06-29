# class WaveAlgorithm


import maze_constants as c


class WaveAlgorithm:

    '''Maze pathfinding class using the wave algorithm'''

    def __init__(self, rows: int, cols: int,
                 right_walls: list, down_walls: list):
        '''WaveAlgorithm class constructor'''
        self.__initial_data_validation(rows, cols, right_walls, down_walls)
        self.rows = rows
        self.cols = cols
        self.right_walls = right_walls
        self.down_walls = down_walls

    def get_path(self, start: tuple, finish: tuple):
        '''Maze pathfinding method

        Return list of points from start to finish: [(row0, col0), ...]
        Empty list if path [start...finish] not exist
        One elemnt list if (start == finish)
        '''
        if self.__point_validation(start) is False:
            raise ValueError('Starting point is outside the maze')
        if self.__point_validation(finish) is False:
            raise ValueError('Finish point is outside the maze')
        if start == finish:
            return [start]

        self.length_map = [[c.NOT_VISITED for j in range(self.cols)]
                           for i in range(self.rows)]

        self.wave = [start]
        self.wave_step = 0
        self.length_map[start[c.ROW]][start[c.COL]] = 0
        while len(self.wave) > 0:
            self.wave_step += 1
            if self.__wave_step(finish):
                break

        return self.__backtracking(finish)

    def __initial_data_validation(self, rows, cols, right_walls, down_walls):
        '''Initial data (rows, cols, walls) checking function'''
        if rows < 1 or cols < 1:
            raise ValueError('Maze must has positive value dimensions')
        if self.__walls_array_validation(right_walls, rows, cols) is False:
            raise ValueError(f'Vertical walls array has incorrect dimesions')
        if self.__walls_array_validation(down_walls, rows, cols) is False:
            raise ValueError(f'Horizontal walls array has incorrect dimesions')

    def __walls_array_validation(self, matrix, rows, cols):
        '''Walls array dimensions checking function'''
        if len(matrix) != rows:
            return False
        for row in matrix:
            if len(row) != cols:
                return False        
        return True

    def __wave_step(self, finish: tuple) -> bool:
        '''
        Current wave processing method

        Change self.wave list to next wave list
        Return finish point reached bool signal
        '''
        f_row, f_col = finish
        next_wave = []
        for row, col in self.wave:
            # up direction:
            if row > 0 and self.down_walls[row - 1][col] != c.WALL and \
               self.length_map[row - 1][col] == c.NOT_VISITED:
                next_wave.append((row - 1, col))
                self.length_map[row - 1][col] = self.wave_step
            # right direction:
            if self.right_walls[row][col] != c.WALL and \
               self.length_map[row][col + 1] == c.NOT_VISITED:
                next_wave.append((row, col + 1))
                self.length_map[row][col + 1] = self.wave_step
            # down direction:
            if self.down_walls[row][col] != c.WALL and \
               self.length_map[row + 1][col] == c.NOT_VISITED:
                next_wave.append((row + 1, col))
                self.length_map[row + 1][col] = self.wave_step
            # left direction:
            if col > 0 and self.right_walls[row][col - 1] != c.WALL and \
               self.length_map[row][col - 1] == c.NOT_VISITED:
                next_wave.append((row, col - 1))
                self.length_map[row][col - 1] = self.wave_step

            if self.length_map[f_row][f_col] != c.NOT_VISITED:
                return True

        self.wave = next_wave
        return False

    def __backtracking(self, finish: tuple) -> list:
        '''
        Path formation method

        Return list of points from start to finish: [(row0, col0), ...]
        '''
        row, col = finish

        # finish not reached
        if self.length_map[row][col] == c.NOT_VISITED:
            return []

        # finish reached
        path = [finish]
        wave_step = self.length_map[row][col]
        while wave_step > 0:
            wave_step -= 1
            row, col = path[-1]

            # up direction:
            if row > 0 and \
                    self.down_walls[row - 1][col] != c.WALL and \
                    self.length_map[row - 1][col] == wave_step:
                path.append((row - 1, col))
            # right direction:
            elif self.right_walls[row][col] != c.WALL and \
                    self.length_map[row][col + 1] == wave_step:
                path.append((row, col + 1))
            # down direction:
            elif self.down_walls[row][col] != c.WALL and \
                    self.length_map[row + 1][col] == wave_step:
                path.append((row + 1, col))
            # left direction:
            else:
                path.append((row, col - 1))

        path.reverse()
        return path

    def __point_validation(self, point: tuple) -> bool:
        '''Point validation method'''
        return 0 <= point[c.ROW] < self.rows and 0 <= point[c.COL] < self.cols


if __name__ == '__main__':
    print(WaveAlgorithm.__doc__)
