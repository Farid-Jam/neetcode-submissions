# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        reverse = None
        while second:
            temp = second.next
            second.next = reverse
            reverse = second
            second = temp
        
        while head and reverse:
            temp1 = head.next
            temp2 = reverse.next

            head.next = reverse
            reverse.next = temp1

            head = temp1
            reverse = temp2