"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100,
the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.
"""


def centuryFromYear(year):
    def get_century(digits: int, last_greater_than_Zero=False):
        return digits+1 if last_greater_than_Zero else digits

    if year < 1:
        return None

    year_str = str(year)
    if len(year_str) == 4:
        return get_century(int(year_str[0] + year_str[1]), int(year_str[-1] + year_str[-2]) > 0)
    elif len(year_str) == 3:
        return get_century(int(year_str[0]), int(year_str[-1] + year_str[-2]) > 0)
    else:
        return 1


if __name__ == '__main__':
    assert centuryFromYear(1700) == 17
    assert centuryFromYear(1) == 1
    assert centuryFromYear(1701) == 18
    assert centuryFromYear(100) == 1
    assert centuryFromYear(201) == 3
    assert centuryFromYear(220) == 3
    assert centuryFromYear(299) == 3
    assert centuryFromYear(0) is None
    assert centuryFromYear(101) is not 1

