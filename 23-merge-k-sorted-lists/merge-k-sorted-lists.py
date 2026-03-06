# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        res = new_head

        while True:
            cur_min = None
            idx = None
            for i, node in enumerate(lists):
                if node and (cur_min is None or node.val < cur_min.val):
                    cur_min = node
                    idx = i
            
            if cur_min is None:
                break
            res.next = cur_min
            res = res.next
            lists[idx] = lists[idx].next
        
        return new_head.next