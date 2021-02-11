"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.


"""

# naive solution: generate set of points that compose the two rectangles, the intesenction of points is the
#                 overlapping part, find the height and width of the overlapping part and calculate the area.

def generate_all_points(top_left, dims):
    width, height = dims

    points = set()

    curr_point = top_left
    for y in range(height+1):
        for x in range(width+1):
            points.add((curr_point[0]+x, curr_point[1]-y))  # width increases to the left, height increases down

    return points


def intersection_area(rec_1, rec_2):
    rec_1_points = generate_all_points(rec_1["top_left"], rec_1["dimensions"])

    rec_2_points = generate_all_points(rec_2["top_left"], rec_2["dimensions"])

    # print(rec_1_points.intersection(rec_2_points))

    intersection_points = rec_1_points.intersection(rec_2_points)

    if len(intersection_points) == 0:
        return 0

    intersection_points = list(intersection_points)
    intersection_points.sort(key=lambda point: point[1], reverse=True)
    # print(intersection_points)
    intersection_points.sort(key=lambda point: point[0], reverse=False)
    # print(intersection_points)
    top_left = intersection_points[0]
    bottom_right = intersection_points[-1]

    width = abs(top_left[0] - bottom_right[0])
    height = abs(top_left[1] - bottom_right[1])

    return width * height


# better solution: find the right-most left border and the bottom-most top border this will be the top left corner
#                  of the intersecting rectangle. Then find the top-most bottom border and the left-most right
#                  border this will be the bottom-right corner.
#                  If the top-left x is greater than the bottom-right x then does not intersect, similarly
#                  If the bottom-right y is greater than the top-right y then also does not intersect.

def intersection_area_redux(rec_1, rec_2):
    top_left_x = max(rec_1["top_left"][0], rec_2["top_left"][0])
    top_left_y = min(rec_1["top_left"][1], rec_2["top_left"][1])

    bottom_right_x = min(rec_1["top_left"][0] + rec_1["dimensions"][0], rec_2["top_left"][0] + rec_2["dimensions"][0])
    bottom_right_y = max(rec_1["top_left"][1] - rec_1["dimensions"][1], rec_2["top_left"][1] - rec_2["dimensions"][1])

    if top_left_x > bottom_right_x or bottom_right_y > top_left_y:
        return 0

    return (bottom_right_x - top_left_x) * (top_left_y- bottom_right_y)

if __name__ == '__main__':
    r1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    }

    r2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3)  # width, height
    }

    assert intersection_area(r1, r2) == 6
    assert intersection_area_redux(r1, r2) ==6

    r1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    }

    r2 = {
        "top_left": (0, 8),
        "dimensions": (4, 3)  # width, height
    }

    assert intersection_area(r1, r2) == 0
    assert intersection_area_redux(r1, r2) == 0