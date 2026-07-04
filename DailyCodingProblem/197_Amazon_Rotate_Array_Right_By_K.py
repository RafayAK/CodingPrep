"""
This problem was asked by Amazon.

Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""



# This is ok, and in-place because we do `array[:]` but takes O(n) extra space
# array[-k:] + array[:-k] <- line creates a new list then assigns it back to the list overwriting it.
# That is:
#   array[-k:]   # new list
#   array[:-k]   # new list
#   array[-k:] + array[:-k]  # another new concatenated list
def rotate_in_place(array: list, k: int) -> None:
    """
    Rotates right by "k" array in-place

    Args:
        array (list):
        k (int):

    Returns:
        None
    """
    if not 0 <= k < len(array):
        raise ValueError("'k' must be between 0 and len(array) - 1.")

    array[:] = array[-k:] + array[:-k]



# This is a better solution as its in-place and O(1) space i.e does not take extra space.
# This intuition behind this solution:
# Given array [1, 2, 3, 4, 5] and k=3
# split the array into 2 parts first n-k = 5-3 = 2 and the rest,
#   A= [1, 2] => 0 to k-1 and,
#   B=[3, 4, 5] => k to n-1
# Why? because we need to rotate the string k=3 steps to the right, and B now contains all the elements that
# will be part of the right rotation.
# 1. let's reverse the whole first => reverse(AB) = BA => [5, 4, 3, 2, 1]
# Now both at least both the part are in the right spot B comes before A when rotating right.
# But the internal elements are also reversed, we need to bring them back to original spots.
# So just reverse the internal parts of B and A.
# 2. reverse B => [3, 4, 5, 2, 1]
# 3. reverse A => [3, 4, 5, 1, 2]
# TADA!!! Now both internal parts og B and A are in their correct internal orientation and we
# have rotated the list in-place by k=3 steps.
def rotate_in_place_constant_space(array:list, k:int) -> None:

    n = len(array)

    if n == 0:
        raise ValueError("Can't be an empty list.")

    if not 0 < k < n:
        raise ValueError(f"'k' must be between 0 and {n}")

    # in-place reverse helper
    def reverse(left:int, right:int):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    # first reverse the whole list
    reverse(0, n-1)
    # reverse first part
    reverse(0, k-1)
    # reverse 2nd part
    reverse(k, n-1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    rotate_in_place(array=arr, k=3)
    assert arr == [3, 4, 5, 1, 2]  # original arr should now match the rotated array


    arr = [1, 2, 3, 4, 5]
    rotate_in_place_constant_space(array=arr, k=3)
    assert arr == [3, 4, 5, 1, 2]  # original arr should now match the rotated array


