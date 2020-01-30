"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.

"""

def get_square_root(num):
    # returns square root to 4 dp

    def increment_root(root_num:str, pos:float):
        return str(float(root_num) + pos)

    def decrement_root(root_num:str, pos:float)
        return str(float(root_num) - pos)

    root_num = str(num // 2)
    pos = 1.0

    while len(root_num.split('.')[1]) != 4:
        if float(root_num) ** 2 == num:
            return float(root_num)
        elif float(root_num) ** 2 > num:
            root_num = increment_root(root_num, pos)
        else:
            # decrement root
            root_num = decrement_root(root_num, pos)

    return float(root_num)
