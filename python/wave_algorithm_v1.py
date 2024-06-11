# class WaveAlgorithm

NOT_VISITED = -1
WALL = 1
ROW = 0
COL = 1

class WaveAlgorithm:

    '''Класс поиска пути в лабиринте с помощью волнового алгоритма'''

    def __init__(self, width: int, height: int, right_walls: list,
                 down_walls: list) -> list:
        '''Конструктор класса'''
        self.rows = height
        self.cols = width
        self.right_walls = right_walls
        self.down_walls = down_walls

    def get_path(self, start: tuple, finish: tuple):
        '''
        Функция поиска пути в лабиринте
        Возвращает список координта точек в формает [(row0, col0), ...]:
        0. пустой - точки не связаны
        1. единичной длины - точка начала и конца совпадают
        2. длина больше единицы - путь найден
        '''

        if self.__point_validation(start) is False:
            raise ValueError('Точка старта за пределами лабиринта')
        if self.__point_validation(finish) is False:
            raise ValueError('Точка финиша за пределами лабиринта')
        if start == finish:
            return [start]

        self.length_map = [[NOT_VISITED for j in range(self.cols)]
                           for i in range(self.rows)]

        self.points_queue = [start]
        self.wave_step = 0
        self.length_map[start[ROW]][start[COL]] = 0
        has_reached = False
        while len(self.points_queue) > 0 and not has_reached:
            self.wave_step += 1
            has_reached = self.__wave_step(finish)


        path = []
        if has_reached:
            path = self.__backtracking(start, finish)

        # lst = [['#' for j in range(self.cols)] for i in range(self.rows)]
        # for p in path:
        #     lst[p[ROW]][p[COL]] = ' '
        # for i in range(self.rows):
        #     lst[i] = ''.join(map(str, lst[i]))
        # for row in lst:
        #     print(row)
        # print()

        return path

    def __wave_step(self, finish) -> bool:
        '''
        Функция обработки текущей волны и формирования новой
        Возвращает сигнал достижения точки финиша
        '''

        next_queue = []
        for p in self.points_queue:
            # up direction
            if p[ROW] > 0 and self.down_walls[p[ROW] - 1][p[COL]] != WALL\
               and self.length_map[p[ROW] - 1][p[COL]] == NOT_VISITED:
                next_queue.append((p[ROW] - 1, p[COL]))
                self.length_map[p[ROW] - 1][p[COL]] = self.wave_step

            # right direction
            if self.right_walls[p[ROW]][p[COL]] != WALL\
               and self.length_map[p[ROW]][p[COL] + 1] == NOT_VISITED:
                next_queue.append((p[ROW], p[COL] + 1))
                self.length_map[p[ROW]][p[COL] + 1] = self.wave_step

            # down direction
            if self.down_walls[p[ROW]][p[COL]] != WALL\
               and self.length_map[p[ROW] + 1][p[COL]] == NOT_VISITED:
                next_queue.append((p[ROW] + 1, p[COL]))
                self.length_map[p[ROW] + 1][p[COL]] = self.wave_step

            # left direction
            if p[COL] > 0 and self.right_walls[p[ROW]][p[COL] - 1] != WALL\
               and self.length_map[p[ROW]][p[COL] - 1] == NOT_VISITED:
                next_queue.append((p[ROW], p[COL] - 1))
                self.length_map[p[ROW]][p[COL] - 1] = self.wave_step
            
            if self.length_map[finish[ROW]][finish[COL]] != NOT_VISITED:
                return True

        self.points_queue = next_queue
        return False

    def __backtracking(self, start, finish: tuple) -> list:
        '''
        Функция сборки пути
        Возвращает список точек от начала до финиша в формате
        [(row0, col0), ...]
        '''

        path = [finish]
        wave_step = self.length_map[finish[ROW]][finish[COL]]
        while wave_step > 0:
            # print(wave_step)
            wave_step -= 1
            cur_point = path[-1]

            # up direction
            if cur_point[ROW] > 0\
               and self.down_walls[cur_point[ROW] - 1][cur_point[COL]] != WALL\
               and self.length_map[cur_point[ROW] - 1][cur_point[COL]] ==\
                   wave_step:
                path.append((cur_point[ROW] - 1, cur_point[COL]))

            # right direction
            elif self.right_walls[cur_point[ROW]][cur_point[COL]] != WALL\
                 and self.length_map[cur_point[ROW]][cur_point[COL] + 1] ==\
                     wave_step:
                path.append((cur_point[ROW], cur_point[COL] + 1))

            # down direction
            elif self.down_walls[cur_point[ROW]][cur_point[COL]] != WALL\
                 and self.length_map[cur_point[ROW] + 1][cur_point[COL]] ==\
                 wave_step:
                path.append((cur_point[ROW] + 1, cur_point[COL]))

            # left direction
            else:
                path.append((cur_point[ROW], cur_point[COL] - 1))
            # print(path)

        path.reverse()
        return path

    def __point_validation(self, point: tuple) -> bool:
        '''
        Функция проверки расположения точки внутри поля лабиринта
        '''

        # return point[self.__row_dir] < self.rows
        # and point[self.__col_dir] < self.cols
        return 0 <= point[ROW] < self.rows and 0 <= point[COL] < self.cols


if __name__ == '__main__':
    pass
