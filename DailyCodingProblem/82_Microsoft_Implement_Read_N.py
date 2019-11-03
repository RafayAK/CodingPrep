"""
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content "Hello world", three read7() returns "Hello w", "orld" and then "".
"""

char_ptr = 0  # pointer to a char in text for read7()


def read7(text):
    global char_ptr
    res = text[char_ptr:char_ptr+7]
    char_ptr +=7

    return res


char_buffer = ""  # char_buffer for readN()


def readN(text, n):
    global char_buffer

    while len(char_buffer) < n:
        seven_chars = read7(text)
        if seven_chars == "":
            break
        char_buffer += seven_chars

    res = char_buffer[:n]
    char_buffer = char_buffer[n:]
    return res


if __name__ == '__main__':
    text = "Hello world"
    print("-------Read-7---------")
    print(read7(text))
    print(read7(text))
    print(read7(text))

    print("-------Read-2---------")
    char_buffer = ""
    char_ptr = 0
    for _ in range(7):
        print(readN(text, 2))  # 'He', 'll', 'o ', 'wo', 'rl', 'd', ''

    print("-------Read-8---------")
    char_buffer = ""
    char_ptr = 0
    for _ in range(3):
        print(readN(text, 8))  # 'hello wo', 'rld', ''

    print("-------Read-4---------")
    char_buffer = ""
    char_ptr = 0
    for _ in range(4):
        print(readN(text, 4))  # 'hello wo', 'rld', ''