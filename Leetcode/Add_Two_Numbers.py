# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pr_q = 0
        add_node = ListNode()
        add_num = add_node
        while l1 and l2: # 둘 다 None이 아닐 때,
            q, r = divmod(pr_q + l1.val + l2.val, 10)
            add_node.val = r
            
            pr_q = q
            l1 = l1.next
            l2 = l2.next
            
            if l1 or l2:
                add_node.next = ListNode()
                add_node = add_node.next
        
        bigger_num = l1 if l1 else l2
        while bigger_num:
            q, r = divmod(pr_q + bigger_num.val, 10)
            add_node.val = r
            
            pr_q = q
            bigger_num = bigger_num.next
            if bigger_num:
                add_node.next = ListNode()
                add_node = add_node.next
        
        if pr_q:
            add_node.next = ListNode(pr_q)
        
        return add_num