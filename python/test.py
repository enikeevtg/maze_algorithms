import maze

# a = [[-1 for j in range(3)] for i in range(3)]
# b = [0, 2]
# print(a == b)
# print(a)

# width, height = map(int, input().split())
# length_map = [[i * width + j for j in range(width)] for i in range(height)]
# length_map = [[-1 for i in range(width)] for i in range(height)]
# for row in length_map:
#     print(row)

# start = [int(el) for el in input().split()]
# length_map[start[0]][start[1]] = 0
# for row in length_map:
#     print(row)

# lst = [[1, 2], [3, 4], [5]]
# for i in range(3):
#     lst[i] = ''.join(map(str, lst[i]))
# print(lst[0][1])
# print(lst)


width, height = map(int, input().split())
right_walls = []
down_walls = []
for i in range(height):
    right_walls.append(list(map(int, input().split())))
for i in range(height):
    down_walls.append(list(map(int, input().split())))

solution = maze.Maze(width, height, right_walls, down_walls)

start = tuple(map(int, input().split()))
finish = tuple(map(int, input().split()))
print('start =', start)
print('finish =', finish)
print(solution.find_path(start, finish))


# drow = [-1, 0, 1, 0]
# dcol = [0, 1, 0, -1]
# a = (1, 1)
# b = []
# for i in range(4):
#     b.append((a[0] + drow[i], a[1] + dcol[i]))
# for i in range(4):
#     print(max(a, b[i]), '-', min(a, b[i]))
