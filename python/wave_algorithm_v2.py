# class WaveAlgorithm
# Добавлена структура Point вместо использования кортежа

NOT_VISITED = -1
WALL = 1
# ROW = 0
# COL = 1

class Point:
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def __str__(self):
        return f"""({self.row}, {self.col})"""

    def __repr__(self):
        return f"""({self.row}, {self.col})"""


class WaveAlgorithm:
    '''
    Класс поиска пути в лабиринте с помощью волнового алгоритма
    '''

    def __init__(self, width: int, height: int, right_walls: list,
                 down_walls: list) -> list:
        '''
        Конструктор класса
        '''        

        self.rows = height
        self.cols = width
        self.right_walls = right_walls
        self.down_walls = down_walls

    def find_path(self, start: Point, finish: Point):
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

        self.wave = [start]
        self.wave_step = 0
        self.length_map[start.row][start.col] = 0
        has_reached = False 
        while len(self.wave) > 0 and not has_reached:
            self.wave_step += 1
            has_reached = self.__wave_step(finish)


        path = []
        if has_reached:
            path = self.__backtracking(finish)

        # lst = [['#' for j in range(self.cols)] for i in range(self.rows)]
        # for p in path:
        #     lst[p.row][p.col] = ' '
        # for i in range(self.rows):
        #     lst[i] = ''.join(map(str, lst[i]))
        # for row in lst:
        #     print(row)
        # print()

        return path

    def __wave_step(self, finish: Point) -> bool:
        '''
        Функция обработки текущей волны и формирования новой
        Возвращает сигнал достижения точки финиша
        '''

        next_wave = []
        for pt in self.wave:
            # up direction
            if pt.row > 0 and self.down_walls[pt.row - 1][pt.col] != WALL\
               and self.length_map[pt.row - 1][pt.col] == NOT_VISITED:
                next_wave.append(Point(pt.row - 1, pt.col))
                self.length_map[pt.row - 1][pt.col] = self.wave_step

            # right direction
            if self.right_walls[pt.row][pt.col] != WALL\
               and self.length_map[pt.row][pt.col + 1] == NOT_VISITED:
                next_wave.append(Point(pt.row, pt.col + 1))
                self.length_map[pt.row][pt.col + 1] = self.wave_step

            # down direction
            if self.down_walls[pt.row][pt.col] != WALL\
               and self.length_map[pt.row + 1][pt.col] == NOT_VISITED:
                next_wave.append(Point(pt.row + 1, pt.col))
                self.length_map[pt.row + 1][pt.col] = self.wave_step

            # left direction
            if pt.col > 0 and self.right_walls[pt.row][pt.col - 1] != WALL\
               and self.length_map[pt.row][pt.col - 1] == NOT_VISITED:
                next_wave.append(Point(pt.row, pt.col - 1))
                self.length_map[pt.row][pt.col - 1] = self.wave_step
            
            if self.length_map[finish.row][finish.col] != NOT_VISITED:
                return True

        self.wave = next_wave
        return False

    def __backtracking(self, finish: Point) -> list:
        '''
        Функция сборки пути
        Возвращает список точек от начала до финиша в формате
        [(row0, col0), ...]
        '''

        path = [finish]
        wave_step = self.length_map[finish.row][finish.col]
        while wave_step > 0:
            # print(wave_step)
            wave_step -= 1
            cur_pt = path[-1]

            # up direction
            if cur_pt.row > 0\
               and self.down_walls[cur_pt.row - 1][cur_pt.col] != WALL\
               and self.length_map[cur_pt.row - 1][cur_pt.col] ==\
                   wave_step:
                path.append(Point(cur_pt.row - 1, cur_pt.col))

            # right direction
            elif self.right_walls[cur_pt.row][cur_pt.col] != WALL\
                 and self.length_map[cur_pt.row][cur_pt.col + 1] ==\
                     wave_step:
                path.append(Point(cur_pt.row, cur_pt.col + 1))

            # down direction
            elif self.down_walls[cur_pt.row][cur_pt.col] != WALL\
                 and self.length_map[cur_pt.row + 1][cur_pt.col] ==\
                 wave_step:
                path.append(Point(cur_pt.row + 1, cur_pt.col))

            # left direction
            else:
                path.append(Point(cur_pt.row, cur_pt.col - 1))
            # print(path)

        path.reverse()
        return path

    def __point_validation(self, point: Point) -> bool:
        '''
        Функция проверки расположения точки внутри поля лабиринта
        '''

        return 0 <= point.row < self.rows and 0 <= point.col < self.cols


if __name__ == '__main__':
    pass
