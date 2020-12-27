'''
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


'''



def map_exists(s1:str, s2:str):
    if len(s1) != len(s2):
        return False

    char_map={}

    for char1, char2 in zip(s1, s2):
        if char1 not in char_map:
            char_map[char1] = char2
        elif char_map[char1] != char2:
            # char1 is already in the char_map
            # check if its assigned to char2, otherwise return False
            return False

    return True


if __name__ == '__main__':
    print(map_exists('abc', 'bcd'))
    print(map_exists('foo', 'bar'))