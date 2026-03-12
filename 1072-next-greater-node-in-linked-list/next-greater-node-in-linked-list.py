# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        stack = []

        cur = head
        i = 0
        while cur:
            answer.append(0)
            while stack and cur.val > stack[-1][0]:
                val, idx = stack.pop()
                answer[idx] = cur.val
            
            stack.append((cur.val, i))
            cur = cur.next
            i += 1
        
        return answer




