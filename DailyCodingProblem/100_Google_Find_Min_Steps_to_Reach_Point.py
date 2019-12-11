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

# idea: use euclidean distance to see if you have moved close to the point or away

def squared_euclidean_dist(point_A, point_B):
    return (point_A[0]-point_B[0])**2 + (point_A[1] - point_B[1])**2

moves = [
    (+1, 0),
    (-1, 0),
    (0, +1),
    (0, -1),
    (-1, -1),
    (+1, +1),
    (-1, +1),
    (+1, -1)
]


def find_min_steps(sequence):
    def helper(point_a, point_b, prev_dist, min_steps=0):
        if prev_dist == 0:
            return min_steps

        current_dist = squared_euclidean_dist(point_a, point_b)
        if current_dist > prev_dist:
            return float('inf')


        # try all moves select the shortest move
        steps = []
        for move in moves:
            temp_point = (point_a[0]+move[0], point_b[1]+point_b[1])
            steps = helper(temp_point, point_b, current_dist, min_steps+1)

        return min(steps)


    min_steps = 0
    a = sequence[0]
    for b in sequence[1:]:
        # find shortest_path from a to b
        min_steps += helper(point_a=a, point_b=b, prev_dist=squared_euclidean_dist(a, b))
        a = b

    return min_steps



if __name__ == '__main__':
    print(find_min_steps([(0, 0), (1, 1), (1, 2)]))