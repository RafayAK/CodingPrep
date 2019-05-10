"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”,
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

# Recursive approach:
# keep dividing sting into smaller and smaller parts, till either
# 1- both string are empty -> same size, return 0. No need to add additional chars
# 2- One is empty while other is not -> need to add chars size of remaining string return. return len(left_over_str)
#
# add +1 if the individual chars do not match
def min_edit_dist(stringA: str, stringB: str, dist=0):

    if len(stringA) is 0 and len(stringB) is 0:
        return 0

    elif len(stringA) is 0:
        return len(stringB)
    elif len(stringB) is 0:
        return len(stringA)

    char_A = stringA[0]
    char_B = stringB[0]

    dist += min_edit_dist(stringA[1:], stringB[1:], dist)

    if char_A != char_B:
        dist +=1

    return dist

if __name__ == '__main__':

    # print(min_edit_dist("kitten", "sitting")) # ans=3
    # print(min_edit_dist("sitting", "kitten"))  # ans=3
    # print(min_edit_dist("kitten", "cat"))  # ans=5
    # print(min_edit_dist("cat", "kitten"))  # ans=5
    # print(min_edit_dist("black", "white"))  # and=5
    # print(min_edit_dist("top", "dog"))  # and=5
    # print(min_edit_dist("top", ""))  # and=3
    # print(min_edit_dist("top", "top"))  # and=0
    print(min_edit_dist("t", "d"))  # and=1
