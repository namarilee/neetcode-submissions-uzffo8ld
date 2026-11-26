# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #midpoint will be at slow
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd half of array
        second = slow.next
        prev = None
        slow.next = None #break the link of the midpoint
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #prev points to last element in 2nd list
        first, second = head, prev
        #move pointers to rearrange the list
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2