# WAVE ALGORITHM

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

# drow = [-1, 0, 1, 0]
# dcol = [0, 1, 0, -1]
# a = (1, 1)
# b = []
# for i in range(4):
#     b.append((a[0] + drow[i], a[1] + dcol[i]))
# for i in range(4):
#     print(max(a, b[i]), '-', min(a, b[i]))

# pts = [(0, 0), (0, 1)]
# # pts = [Point(), Point(), Point()]
# pts.insert(0, (3, 3))

# for row, col in pts:
#   print(row, col)

# r, c = pts[0]
# print(pts[0], r, c)

# def tmp(pt: tuple):
#   r, c = pt
#   print(r, c)
  
# tmp(pts[0])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ELLER'S ALGORITHM

import random

# random.seed()
# for _ in range(11):
#     print(random.randint(0, 1))

# width, height = map(int, input().split())
# length_map = [[0 if i < width - 1 else 1 for i in range(width)] \
#               for _ in range(height)]
# for row in length_map:
#     print(row)
# print()
# length_map = [[0 for _ in range(width)] if i < height - 1 else \
#               [1 for _ in range(width)] for i in range(height)]
# for row in length_map:
#     print(row)

# from random import randint, choice
# lst = [randint(0, 9) for _ in range(randint(5, 11))]
# src = choice(lst)
# dest = choice(lst)
# print(src, dest)
# print(lst)
# # ЗАМЕНА ЭЛЕМЕНТОВ СПИСКА РАВНЫХ src НА dest
# lst = list(map(lambda x: dest if x == src else x, lst))
# print(lst)


# sets_info = {}
# for col in range(15):
#   key = randint(1, 5)
#   sets_info[key] = sets_info.get(key, {'pass': False, 'walls': []})
#   sets_info[key]['pass'] = choice([True, False])
#   sets_info[key]['walls'].append(col)
# for k, v in sets_info.items():
#   print(f'''{k}: {v}''')
