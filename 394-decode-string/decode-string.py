class Solution:
    def decodeString(self, s: str) -> str:
        queue = deque()
        cur = []
        num_digits = []

        for char in s:
            if char.isdigit():
                num_digits.append(char)
            elif char == "[":
                if cur:
                    queue.append(cur)
                    cur = []
                queue.append(int("".join(num_digits)))
                num_digits = []
            elif char == "]":
                num = queue.pop()
                cur *= num
                while queue and type(queue[-1]) is list:
                    cur = queue.pop() + cur
            else:
                cur.append(char)
        
        return "".join(cur)