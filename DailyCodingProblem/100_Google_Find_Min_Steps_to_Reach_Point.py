"""
This problem was asked by Google.

You are in an infinite 2D grid where you can move in any of the 8 directions:

    (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

# One way to reach form a point (x1,y1) to (x2, y2) is to move abs(x2-x1)
# steps in horizontal direction and abs(y2-y1) steps in vertical direction,
# but this is not the shortest path to reach (x2,y2).
# The best way would be to cover the maximum possible distance in diagonal direction
# and remaining in horizontal or vertical direction. If we look closely this just
# reduces to maximum of abs(x2-x1) and abs(y2-y1).
#
# Example
# x1 = 5, y1= 20
# x2 = 15, y2 = 15
#
# we first move diagonally to reach (10,15) this takes 5 steps and then we move 5 units in x direction,
# which again takes 5 steps. In total this is 10 steps which is equal to MAX(abs(15-5), abs(15-20))



def find_min_steps(sequence):

    min_steps = 0
    a = sequence[0]
    for b in sequence[1:]:
        min_steps += max(abs(b[0]-a[0]), abs(b[1] - a[1]))
        a = b

    return min_steps



if __name__ == '__main__':
    print(find_min_steps([(0, 0), (1, 1), (1, 2)]))  # 2
    print(find_min_steps([(4, 6), (1, 2), (4, 5), (10, 12)]))  # 14