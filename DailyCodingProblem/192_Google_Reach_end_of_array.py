""""
This problem was asked by Google.

You are given an array of nonnegative integers.
Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.


For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

"""


# this is slow for large inputs as the solution is recursive
def can_reach_end(input_array):
    goal_idx = len(input_array) - 1
    def check(arr, start_idx, end_idx, path_arr):
        if start_idx == end_idx:
            return True, path_arr + [end_idx]
        steps = arr[start_idx]

        for i in range(steps, -1, -1):
            if i == 0:
                return False, path_arr

            if start_idx+i > end_idx:
                continue

            flag, path = check(arr, start_idx + i, end_idx, path_arr + [start_idx])
            if flag:
                return flag, path

    reached_end, path = check(input_array, 0, goal_idx, [])
    print(*path, sep="->")
    return reached_end


def can_reach_end_redux(input_array):
    # keeps track of the furthest index we can reach as we iterate through the array.
    furthest_idx_reached = 0
    goal_idx = len(input_array) - 1
    for idx, step in enumerate(input_array):
        
        # If at any point idx is greater than furthest_idx_reached,
        # it means we are stuck and cannot proceed further, hence return False.
        if idx > furthest_idx_reached:
            return False

        furthest_idx_reached = max(furthest_idx_reached, idx + step)
        
        # If furthest_idx_reached is greater than or equal to the last index of the array, return True.
        if furthest_idx_reached >= goal_idx:
            return True

    return False


if __name__ == '__main__':
    # assert can_reach_end([1, 3, 1, 2, 0, 1])
    # assert not can_reach_end([1, 2, 1, 0, 0])
    # assert can_reach_end([2, 3, 1, 1, 4])
    # assert not can_reach_end([3, 2, 1, 0, 4])
    # assert can_reach_end([3])
    # assert can_reach_end([0])
    # assert not can_reach_end([0, 1, 2])
    # assert not can_reach_end([1, 0, 2])
    # assert can_reach_end([2, 0, 1])
    # assert can_reach_end([100, 0, 1])
    # assert can_reach_end([1,2,3])
    # assert can_reach_end([2,0])

    assert can_reach_end_redux([1, 3, 1, 2, 0, 1])
    assert not can_reach_end_redux([1, 2, 1, 0, 0])
    assert can_reach_end_redux([2, 3, 1, 1, 4])
    assert not can_reach_end_redux([3, 2, 1, 0, 4])
    assert can_reach_end_redux([3])
    assert can_reach_end_redux([0])
    assert not can_reach_end_redux([0, 1, 2])
    assert not can_reach_end_redux([1, 0, 2])
    assert can_reach_end_redux([2, 0, 1])
    assert can_reach_end_redux([100, 0, 1])
    assert can_reach_end_redux([1, 2, 3])
    assert can_reach_end_redux([2, 0])
    assert can_reach_end_redux([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,
                                8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,
                                1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])