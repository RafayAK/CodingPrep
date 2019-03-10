"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def two_sum(array, k): # O(n)
    other_number_dict = {}  # dictionary to store (K - (current_item)) i.e other number to make K

    for item in array:
        if item in other_number_dict:
            # found the other number that add with item to make K
            return True

        other_number_dict[k-item] = True  # True here is just a placeholder, actually just need the key

    return False


if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    k = 17

    print(two_sum(arr, k))