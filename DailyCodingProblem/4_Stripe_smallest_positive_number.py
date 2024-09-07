'''
This problem was asked by Stripe.

Find the smallest positive number missing from an unsorted array

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2
'''

def naive_method(ls): # O(nlog(n) + n) time, constant space
    ls.sort()

    smallest = 1
    for i in ls:
        if i <= 0:
            continue
        elif i== smallest:
            smallest+=1
    return smallest


def hash_method(ls): # O(2n) time, O(n) space
    hash_dict = {}
    def helper(ls):
        for i in ls:
            if i <=0:
                continue
            else:
                hash_dict[i] = True

    helper(ls)
    i = 1
    while True:
        if i not in hash_dict:
            return i
        i+=1

# O(n) time, O(1) space
def find_smalled_positive(ls):
    start,end= 0, 0 # start index inclusive, end index exclusive

    def segregate(ls): # positives on the left negatives on the right
        nonlocal end
        for i in range(len(ls)):
            if ls[i] > 0:
                ls[end], ls[i] = ls[i], ls[end]
                end+=1

    segregate(ls)
    print(ls)
    print(end)
    for i in range(start,end):
        if abs(ls[i]) <= end:
            if ls[abs(ls[i])-1] > 0:  # make -ive only if +ive
                ls[abs(ls[i])-1] = -ls[abs(ls[i])-1]
    print(ls)
    for i in range(start,end):
        if ls[i] > 0:
            return i+1

    return end+1





if __name__ == '__main__':
    # ls = [2, 3, 7, 6, 8, -1, -10, 15]
    #find_smalled_positive(ls)
    # ls = [2,3,4,-1,0]
    # ls = [2, 3, 7, 6, 8, -1, -10, 15] # ans =1
    # ls = [2, 3, -7, 6, 8, 1, -10, 15] # ans =4
    # ls = [1, 1, 0, -1, -2] # ans =2
    # ls = [3, 4, -1, 1] # ans = 2
    ls = [1, 2, 0] # ans = 3
    # ls = [0,1,2,3,4,5]
    #ls = [1, -1, -5, -3, 3, 4, 2, 8,5]
    #print(hash_method(ls))
    print(find_smalled_positive(ls))