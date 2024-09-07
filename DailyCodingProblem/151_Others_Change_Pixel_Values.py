"""
Given a 2-D matrix representing an image, a location of a pixel in
the screen and a color C, replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
"""

# key idea : flood-fill algo with 8 connectivity components

connectivity = [
    (-1, 0), # North
    (-1, 1), # North-East
    (0, 1), # East
    (1, 1), # South-East
    (1, 0), # South
    (1, -1), # South-West
    (0, -1), # West
    (-1, -1), # North-West
]

def my_flood_fill(mat, loc, new_color):
    r,c = loc
    curr_color = mat[r][c]
    mat[r][c] = new_color
    for row, col in connectivity:
        if -1 < r+row < len(mat) and -1 < c+col < len(mat[1]) and mat[r+row][c+col] == curr_color:
                my_flood_fill(mat, (r+row, col+c), new_color)

if __name__ == '__main__':
    mat = [
        ['B', 'B', 'W'],
        ['W', 'W', 'W'],
        ['W', 'W', 'W'],
        ['B', 'B', 'B']
    ]

    print(*mat, sep='\n', end='\n'+'---'*5+'\n')

    my_flood_fill(mat, (2,2), 'G')

    print(*mat, sep='\n', end='\n'+'---'*5+'\n')