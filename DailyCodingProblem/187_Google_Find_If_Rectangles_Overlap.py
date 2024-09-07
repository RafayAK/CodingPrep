"""
This problem was asked by Google.

You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
"""

from itertools import combinations

def is_overlapping(rec1, rec2):
    top_left_x = max(rec1["top_left"][0], rec2["top_left"][0])
    top_left_y = min(rec1["top_left"][1], rec2["top_left"][1])

    bottom_right_x = min(rec1["top_left"][0] + rec1["dimensions"][0], rec2["top_left"][0] + rec2["dimensions"][0])
    bottom_right_y = max(rec1["top_left"][1] - rec1["dimensions"][1], rec2["top_left"][1] - rec2["dimensions"][1])

    if top_left_x > bottom_right_x or bottom_right_y > top_left_y:
        return False
    elif (bottom_right_x - top_left_x) * (top_left_y - bottom_right_y) == 0:
        # intersection area is zero. Only on edge on top an other
        return False

    return True

def check_overlapping_pair(rectangles):
    for rec1, rec2 in combinations(rectangles, 2):
        if is_overlapping(rec1, rec2):
            return True

    return False

if __name__ == '__main__':
    rectangels= [
        {
            "top_left": (1, 4),
            "dimensions": (3, 3)  # width, height
        },
        {
            "top_left": (-1, 3),
            "dimensions": (2, 1)  # width, height
        },
        {
            "top_left": (0, 5),
            "dimensions": (4, 3)  # width, height
        }
    ]

    assert check_overlapping_pair(rectangels) == True