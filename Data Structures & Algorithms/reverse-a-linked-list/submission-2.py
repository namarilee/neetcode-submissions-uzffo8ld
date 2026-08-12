# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next #store next node
            curr.next = prev #point curr to prev (this is where the reverse happens)
            prev = curr #move prev up
            curr = temp #move curr up

        return prev
