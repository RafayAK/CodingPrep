"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count
and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be ecoded
have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

def encode_string(string):
    encoded_str = ""

    counter = 0
    current_chr = None

    for chr in string:
        if counter == 0: # staring new char
            current_chr = chr
            counter+=1
        elif current_chr == chr:  # found same consecutive char
            counter+=1
        elif current_chr != chr:  # different char, chain broken
            encoded_str = encoded_str + str(counter) + current_chr  # append run length encoded chars
            counter = 1  # set counter to zero to track next set of chars
            current_chr = chr

    # for the final set of chars
    encoded_str = encoded_str + str(counter) + current_chr

    return encoded_str


def decode_string(string):
    decoded_str = ""


    for i in range(1, len(string), 2):
        current_chr = string[i]
        multiplier = int(string[i-1])

        decoded_str = decoded_str + (multiplier * current_chr)

    return decoded_str






if __name__ == '__main__':
    string = "AAAABBBCCDAA"

    print(string)
    print(encode_string(string))

    print(decode_string(encode_string(string)))

    assert(encode_string(string)=="4A3B2C1D2A")
    assert(string == decode_string(encode_string(string)))