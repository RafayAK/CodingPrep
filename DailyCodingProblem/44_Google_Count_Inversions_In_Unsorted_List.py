"""

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.

"""

# idea: use merge sort to count the number of inversions:
#       Runtime of merge sort is O(n*log(n)) which is less than O(n^2)


def merge(list_a_with_inv_tuple, list_b_with_inv_tuple):
    merged_list = []

    list_a, invs_in_a = list_a_with_inv_tuple
    list_b, invs_in_b = list_b_with_inv_tuple

    len_a = len(list_a)
    len_b = len(list_b)

    inversions = invs_in_a + invs_in_b
    iter_a, iter_b = 0, 0
    while iter_a < len_a and iter_b < len_b:
        if list_a[iter_a] < list_b[iter_b]:
            merged_list.append(list_a[iter_a])
            iter_a += 1
        else:
            merged_list.append(list_b[iter_b])
            # the num "list_b[iter_b]" must be less than all the values list_a[iter_a:]
            inversions += len(list_a[iter_a:])
            iter_b += 1

    # append the remaining number to the list
    while iter_a < len_a:
        merged_list.append(list_a[iter_a])
        iter_a += 1

    while iter_b < len_b:
        merged_list.append(list_b[iter_b])
        iter_b += 1

    return merged_list, inversions


def merge_sort(list):
    # if list only contains one number than just return the list and 0 inversions
    if len(list) == 1:
        return list, 0

    # otherwise, divide list into two and run merge sort on tow smaller lists
    mid = len(list)//2
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


def count_inversions(list):
    _, inversions = merge_sort(list)
    return inversions


if __name__ == '__main__':
    assert count_inversions(list=[2, 4, 1, 3, 5]) ==3
