from wave_algorithm import WaveAlgorithm

width, height = map(int, input().split())
right_walls = []
down_walls = []
for i in range(height):
    right_walls.append(list(map(int, input().split())))
for i in range(height):
    down_walls.append(list(map(int, input().split())))

solution = WaveAlgorithm(width, height, right_walls, down_walls)

start = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))
print('start =', start)
print('finish =', finish)
print(solution.get_path(start, finish))


# from wave_algorithm import WaveAlgorithm, Point

# width, height = map(int, input().split())
# right_walls = []
# down_walls = []
# for i in range(height):
#     right_walls.append(list(map(int, input().split())))
# for i in range(height):
#     down_walls.append(list(map(int, input().split())))

# solution = WaveAlgorithm(width, height, right_walls, down_walls)

# row, col = tuple(map(int, input().split()))
# start = Point(row, col)
# row, col = map(int, input().split())
# finish = Point(row, col)
# print('start =', start)
# print('finish =', finish)
# print(solution.find_path(start, finish))
