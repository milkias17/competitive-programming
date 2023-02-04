from typing import List

"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead,
be stored in the input character array chars. Note that group lengths
that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        left_pointer = 0

        while left_pointer < len(chars):
            right_pointer = left_pointer + 1
            count = 1
            if (
                right_pointer >= len(chars)
                or chars[right_pointer] != chars[left_pointer]
            ):
                left_pointer = right_pointer
                continue
            while (
                right_pointer < len(chars)
                and chars[right_pointer] == chars[left_pointer]
            ):
                chars.pop(right_pointer)
                count += 1
            if count > 1:
                if count >= 10:
                    for char in str(count):
                        chars.insert(right_pointer, char)
                        right_pointer += 1
                    right_pointer -= 1
                else:
                    chars.insert(right_pointer, str(count))
            left_pointer = right_pointer + 1

        return len(chars)
