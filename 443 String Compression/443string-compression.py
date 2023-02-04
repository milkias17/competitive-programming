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
