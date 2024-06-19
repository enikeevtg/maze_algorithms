import eller_algorithm


def print_matrix(matrix) -> None:
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            print(matrix[row][col], end=' ')
        print()
    print()


height, width = map(int, input().split())
new_maze = eller_algorithm.EllerAlgorithm(height, width)
right_walls = []
down_walls = []
right_walls, down_walls = new_maze.generate_maze()
# print_matrix(right_walls)
# print_matrix(down_walls)
new_maze.print_maze()
