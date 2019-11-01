'''
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number),
and a digit string, return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.


For example if {2: [a, b, c], 3: [d, e, f]...}
then 23 should return [ad, ae, af, bd, be, bf, cd, ce, cf]
'''


def all_combos(code, mappings):
    if len(code) == 1:
        return mappings[code]

    prev_combos = all_combos(code[1:], mappings)

    res = []
    for letter in mappings[code[0]]:
        for element in prev_combos:
            res.append(letter + element)

    return res


if __name__ == '__main__':
    mapping = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ["j", "k", "l"],
               '6': ["m", "n", "o"],
               '7': ["p", "q", "r", "s"],
               '8': ["t", "u", "v"],
               '9': ["w", "x", "y", "z"]
               }

    print(all_combos('23', mapping))
    print(all_combos('423', mapping))
    print(all_combos('8', mapping))
    print(all_combos('87', mapping))