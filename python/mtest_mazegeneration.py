import eller_algorithm


def print_matrix(matrix) -> None:
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end=' ')
        print()
    print()


rows, cols = map(int, input().split())
new_maze = eller_algorithm.EllerAlgorithm()
right_walls, down_walls = new_maze.generate_maze(rows, cols)
# print_matrix(right_walls)
# print_matrix(down_walls)
new_maze.print_maze()
