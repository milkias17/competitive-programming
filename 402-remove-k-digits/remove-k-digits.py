class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removables = set()

        for i, digit_s in enumerate(num):
            digit = int(digit_s)

            while stack and digit < int(num[stack[-1]]):
                removables.add(stack.pop())
                k -= 1
                if k == 0:
                    break
            
            if k == 0:
                break

            stack.append(i)
        
        while k > 0 and stack:
            removables.add(stack.pop())
            k -= 1
            
        new_num = []
        for i, digit in enumerate(num):
            if i in removables or (digit == "0" and len(new_num) == 0):
                continue
            new_num.append(digit)


        if new_num:
            return "".join(new_num)
        else:
            return "0"