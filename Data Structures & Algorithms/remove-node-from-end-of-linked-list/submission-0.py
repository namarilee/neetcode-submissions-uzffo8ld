# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        p1, p2 = temp, head
        count = 0

        while count < n:
            p2 = p2.next
            count += 1
        
        while p2:
            p1 = p1.next
            p2 = p2.next
        
        next_node = p1.next.next
        p1.next = next_node
        return temp.next