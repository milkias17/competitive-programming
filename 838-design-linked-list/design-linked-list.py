class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.size = 0
    
    def _get(self, index):
        cur = self.head
        while cur is not None and index > 0:
            cur = cur.next
            index -= 1
        
        if index == 0:
            return cur
        
        return None

    def get(self, index: int) -> int:
        node = self._get(index + 1)
        return node.val if node is not None else -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        node = self._get(index)
        if node is None:
            return
        
        new_node = Node(val, node.next)
        node.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
            
        node = self._get(index)
        if node is None:
            return
        
        node.next = node.next.next if node.next else None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)