"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times
except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""


# 1st method
def find_single(arr : list):

    first_occurrence = 0
    second_occurrence = 0

    for i in arr:
        second_occurrence = second_occurrence | (first_occurrence & i)
        first_occurrence = first_occurrence ^ i
        neutralize = ~(first_occurrence & second_occurrence)
        first_occurrence = first_occurrence & neutralize
        second_occurrence = second_occurrence & neutralize


    return first_occurrence


# 2nd method
# O(32*n) = O(n)
def find_single_2(arr):
    STORE_LEN = 32  # assuming that the largest int can be stored in a 32 bit in

    final_result = 0
    for i in range(0, STORE_LEN):
        count = 0
        # check if i'th bit is set
        checking_var = 1 << i
        for num in arr:
            if num & checking_var:
                count+=1

        if count % 3 == 1:
            final_result = final_result | checking_var

    return final_result



if __name__ == '__main__':
    # a = [1,2,1,1]
    # a = [13, 19, 13, 13]
    # a = [6, 1, 3, 3, 3, 6, 6]
    a = [1, 1, 3, 1]
    #print(find_single(a))
    print(find_single_2(a))



