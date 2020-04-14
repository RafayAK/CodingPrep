"""
This problem was asked by LinkedIn.

Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
return [(0, 0), (3, 1)].


"""


def k_nearest(points, central, k):
    squared_l2_norm = lambda p1, p2 : (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    distances = {p: squared_l2_norm(p, central) for p in points}

    # return the k nearest points after sorting based on distances of points
    return [p for p,_ in sorted(distances.items(), key=lambda item: item[1])][:k]


if __name__ == '__main__':
    print(k_nearest([(0, 0), (5, 4), (3, 1)], (1, 2), 2))