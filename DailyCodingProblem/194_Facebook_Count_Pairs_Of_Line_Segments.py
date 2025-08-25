"""
This problem was asked by Facebook.

Suppose you are given two lists of n points,
one list p1, p2, ..., pn on the line y = 0 and
the other list q1, q2, ..., qn on the line y = 1.

Imagine a set of n line segments connecting each point pi to qi.
Write an algorithm to determine how many pairs of the line segments intersect.
"""

def number_of_intersecting_line_segments(P, Q):

    points = []
    for p,q in zip(P, Q):
        points.append((p,q))

    points.sort(key=lambda x: x[0])  # Sort by p

    count_intersecting_line_segments = 0
    for i,(p_1, q_1) in enumerate(points):
        for p_2,q_2 in points[i+1:]:
            # we have an intersection if q1 bigger than q2
            if q_1 > q_2:
                count_intersecting_line_segments += 1

    return count_intersecting_line_segments






if __name__ == '__main__':
    print(number_of_intersecting_line_segments(P=[6, 2, 4, 3, 5, 1], Q=[1, 6, 5, 2, 3, 4]))
    print(number_of_intersecting_line_segments(P=[1, 2, 3], Q=[2, 3, 1]))
    print(number_of_intersecting_line_segments(P=[1, 2, 3], Q=[2, 1, 3]))
    print(number_of_intersecting_line_segments([1, 2, 3, 4], [4, 3, 2, 1]))

































# def number_of_intersecting_line_segments(P, Q):
#     PQ = []
#     for p, q in zip(P, Q):
#         PQ.append((p, q))
#
#     PQ = sorted(PQ, key= lambda t:t[0])
#     print(PQ)
#
#     intersections = 0
#     for i, (p1, q1) in enumerate(PQ):
#         for p2, q2 in PQ[i:]:
#             if q2 < q1:
#                 intersections += 1
#     return intersections