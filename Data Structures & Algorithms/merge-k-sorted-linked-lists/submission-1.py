# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        idx = 0
        heap = []

        for l in lists:
            if l:
                heap.append((l.val, idx, l))
                idx += 1 
        
        heapq.heapify(heap)
        while heap:
            val, i, l = heapq.heappop(heap)
            curr.next = l
            curr = curr.next

            l = l.next
            if l:
                heapq.heappush(heap, (l.val, idx, l))
                idx += 1
        
        return dummy.next
            