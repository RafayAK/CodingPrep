"""
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def find_element_pos(arr, element):

    def helper(arr, element, start, end):
        if end < start:
            return

        mid = start + ((end - start) //2)

        if arr[mid] == element:
            return mid

        if arr[mid] > arr[start]:
            # means the array start->mid is not rotated, completely sorted
            if arr[start] <= element <= arr[mid]:
                # the element must be in lower half
                return helper(arr, element, start, mid-1)
            else:
                # element must be in upper half
                return helper(arr, element, mid+1, end)

        else:
            # elements from mid->end
            # must be sorted
            if arr[mid] <= element <= arr[end]:
                # element in upper half
                return helper(arr, element, mid+1, end)
            else:
                # otherwise, must be in lower half
                return helper(arr, element, start, mid-1)

    return helper(arr, element, start=0, end=len(arr)-1)


if __name__ == '__main__':
    print(find_element_pos([13, 18, 25, 2, 8, 10] , 2))
