"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
"""

def order_into_three(arr, pivot):
    res = []  # new resultant arr
    lesser_idx, greater_idx = 0, 0  # indices to the front of the part where elements are less than pivot and greater than, respectively

    for num in arr:
        if num < pivot:   # num less than pivot
            res.insert(lesser_idx, num)
            lesser_idx += 1
            greater_idx += 1
        elif num > pivot:  # num greater than pivot
            res.insert(greater_idx, num)
            greater_idx += 1
        else:  # num equal to pivot
            res.insert(lesser_idx, num)
            greater_idx += 1

    return res



if __name__ == '__main__':
    print(order_into_three([9, 12, 3, 5, 14, 10, 10], 10))

