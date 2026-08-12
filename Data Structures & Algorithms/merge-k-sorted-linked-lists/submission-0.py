# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        if k == 0:
            return None

        minheap = []

        for i in range(k):
            if lists[i]:
                heapq.heappush(minheap, [lists[i].val, i, lists[i]]) #[head's val, index, actual node]
        
        temp = ListNode()
        curr = temp

        while minheap:
            value, i, node = heapq.heappop(minheap)
            curr.next = node #point curr to node
            curr = curr.next #curr is now node
            node = node.next 
            if node: 
                heapq.heappush(minheap, [node.val, i, node])
        
        return temp.next