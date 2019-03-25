'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

dp_dict = {}

def find_largest_number(arr):
    if tuple(arr) in dp_dict:
        return dp_dict[tuple(arr)]

    if len(arr) == 1:
        dp_dict[tuple(arr)] = str(arr[0])
        return str(arr[0])
    #temp_arr = []
    max_number = '0'
    for i in range(len(arr)):
        num = str(arr[i]) + str(find_largest_number(arr[:i] + arr[i+1:]))
        if int(max_number) <= int(num) : # equal to for the '100'/'1000'... type cases
            max_number = num
    dp_dict[tuple(arr)] = max_number # dp_dict[tuple(arr)] = max(temp_arr)
    return dp_dict[tuple(arr)]

# better version
# order the the converted nums strings in the following order:
# input: [2, 10, 3] -> ['2', '10', '3'] ->  ['3', '2', '10'] -> '3210'
# compare as follows:
# eg. let first element be 2, then
#          1- '23' > '32' return -1
#          2- '210' > '102' return 1
# Then next element is 10
#          3- '103' > '310' return -1


class LargerNumber(str): #inherit str
    def __lt__(self, other):
        return self + other > other + self # checks lexicographical order


def largestNumber(arr): # O(nlog(n))
    largest_num = ''.join(sorted(map(str, arr), key = LargerNumber))

    return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    test = [0,0] # [3,30,34,5,9] # [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
    print(largestNumber(test))
    #print(find_largest_number(test))