#!/usr/bin/python3

""" a method that determines if a given
data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """vaidates a utf-8 encoding"""
    def check(start, size):
        """helperfunction for checking the next values"""
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    start = 0
    while start < len(data):
        first_byte = data[start]
        if (first_byte >> 3) == 0b11110 and check(start, 3):
            start += 4
        elif (first_byte >> 4) == 0b1110 and check(start, 2):
            start += 3
        elif (first_byte >> 5) == 0b110 and check(start, 1):
            start += 2
        elif (first_byte >> 7) == 0:
            start += 1
        else:
            return False
    return True
