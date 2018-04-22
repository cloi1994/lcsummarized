# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head
        
        
        root = pre = ListNode(1)
        pre.next = head
        
        
        while pre.next and pre.next.next:
            cur = pre.next
            curNext = cur.next
            
            cur.next = curNext.next
            curNext.next = cur
            pre.next = curNext
            pre = cur
            
        return root.next
            
