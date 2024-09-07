"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word,
write a function that returns whether the word can be found in
the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the
leftmost column. Similarly, given the target word 'MASS',
you should return true, since it's the last row.

    c|1    2    3    4
 r  __________________
 1  |'F', 'A', 'C', 'I'|
 2  |'O', 'B', 'Q', 'P'|
 3  |'A', 'N', 'O', 'B'|
 4  |'M', 'A', 'S', 'S'|

"""


def get_row_word(matrix, from_row, skip, word_length):
    return "".join(matrix[from_row][skip:skip + word_length])


def get_col_word(matrix, from_col, skip, word_length):
    chars = [row[from_col] for row in matrix]
    return "".join(chars[skip: skip+word_length])

def find_word(matrix, word):
    word_len = len(word)
    start_letter = word[0]
    num_rows = matrix

    # function to get indexes i=of multiple occurrences of value in they exist
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]

    # loop through rows find start_letter from there look
    # across and look down
    for row in range(len(num_rows)):
        indexes = get_indexes(start_letter, matrix[row])

        for idx in indexes:
            # look across
            possibleword = get_row_word(matrix, row, skip=idx, word_length=word_len)
            if possibleword == word:
                return True

            #look down
            possibleword = get_col_word(matrix, idx, skip=row, word_length=word_len)
            if possibleword == word:
                return True

    return False







if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
              ['O', 'B', 'Q', 'P'],
              ['A', 'N', 'O', 'B'],
              ['M', 'A', 'S', 'S']]

    print(find_word(matrix, "FOAM"))
    print(find_word(matrix, "NO"))
    print(find_word(matrix, "FOAMS"))
