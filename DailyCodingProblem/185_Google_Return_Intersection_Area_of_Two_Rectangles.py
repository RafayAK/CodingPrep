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

    print(rec_1_points.intersection(rec_2_points))

    intersection_points = rec_1_points.intersection(rec_2_points)

    if len(intersection_points) == 0:
        return "No overlap"

    intersection_points = list(intersection_points)
    intersection_points.sort(key=lambda point: point[1], reverse=True)
    print(intersection_points)
    intersection_points.sort(key=lambda point: point[0], reverse=False)
    print(intersection_points)
    top_left = intersection_points[0]
    bottom_right = intersection_points[-1]

    width = abs(top_left[0] - bottom_right[0])
    height = abs(top_left[1] - bottom_right[1])

    return width * height

if __name__ == '__main__':
    r1 = {
        "top_left": (1, 4),
        "dimensions": (3, 3)  # width, height
    }

    r2 = {
        "top_left": (0, 5),
        "dimensions": (4, 3)  # width, height
    }

    print(intersection_area(r1, r2))