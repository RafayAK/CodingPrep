"""
This problem was asked by Lyft.

Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""
# solved through caterpillar method

def get_contigous_sum(k, arr):
    front = 0
    total = 0

    for back in range(len(arr)):
        while front < len(arr) and total + arr[front] <= k:
            total += arr[front]
            front += 1

        if total == k:
            return arr[back:front]

        total -= arr[back]

    return None


if __name__ == '__main__':
    print(get_contigous_sum(9, [1, 2, 3, 4, 5]))  # [2, 3, 4]
    print(get_contigous_sum(12, [6, 2, 7, 4, 1, 3, 6]))  # [7, 4, 1]