# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = curr = ListNode()
        while head:
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            
            curr.next, head.next, head = head, curr.next, head.next
            
            if head and curr.val > head.val:
                curr = sorted_head
                
        return sorted_head.next