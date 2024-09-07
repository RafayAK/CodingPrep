"""
This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional
elevation map where each element is unit-width wall and the integer is the height.
 Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
so we can trap 8 units of water.
"""

# simple idea is to calculate depth from either left_level or right_level
# depending on which is smaller.
def find_holding_capacity(elevation_map: list):
    total_units = 0

    # starting elevation, left and right end
    left_level = elevation_map[0]
    right_level = elevation_map[-1]

    while len(elevation_map) > 2: # can only store water if at least 3 walls
        if left_level <= right_level:

            it = 1 # define iterator
            while elevation_map[it] < left_level:
                # calculate depth
                depth = left_level - elevation_map[it]
                total_units += depth
                it += 1

            # found new left level, when the elevation_map[it] >= left_level
            elevation_map = elevation_map[it:]
            left_level = elevation_map[0]

        else:

            it = -2  # define iterator
            while elevation_map[it] < right_level:
                # calculate depth
                depth = right_level - elevation_map[it]
                total_units += depth
                it += 1

            # found new right level, when the elevation_map[it] >= right_level
            elevation_map = elevation_map[:it+1]
            right_level = elevation_map[-1]

    return total_units


if __name__ == '__main__':
    # elevation_map = [2, 1, 2]  # -> ans=1
    # elevation_map = [3, 0, 1, 3, 0, 5]  # -> ans=8
    # elevation_map = [5, 2, 4]  # -> ans=2
    # elevation_map = [3, 0, 1, 3, 0, 5, 2, 4]  # -> ans=10
    # elevation_map = [3, 0, 1, 3, 5]  # ans=5
    # elevation_map = [3, 0, 1, 3, 0, 5, 2]  # ans=8
    elevation_map = [3, 0, 1, 3, 0, 5, 2, 1] # ans=8
    print(find_holding_capacity(elevation_map))