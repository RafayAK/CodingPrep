"""
This problem was asked by Amazon.

Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

moves = [
    # row, col
    (0, 1),  # west
    (0, -1),  # east
    (1, 0),  # south
    (-1, 0), # north

    (1,1), # south-west
    (1, -1), # south-east
    (-1, 1), # north-west
    (-1, -1) # north-east

]

def mark_island(row, col, land_map, marker):

    if row < 0 or col<0 or row>=len(land_map) or col >= len(land_map[0]):
        return land_map

    if land_map[row][col]== 0:
        return land_map

    if land_map[row][col]== marker:
        return land_map

    if land_map[row][col] == 1:
        land_map[row][col] = marker

    for r,c in moves:
        land_map = mark_island(row+r, col+c, land_map, marker)

    return land_map


def find_num_of_islands(land_map):
    islands_found = 0

    for i in range(len(land_map)):
        for j in range(len(land_map[0])):
            if land_map[i][j] == 1:
                islands_found+= 1
                land_map = mark_island(i, j, land_map, marker='i')

    # print(*land_map, sep='\n')
    return islands_found



if __name__ == '__main__':
    land_map = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    print(find_num_of_islands(land_map))   #  4

    land_map = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1],
    ]

    print(find_num_of_islands(land_map))  # 7