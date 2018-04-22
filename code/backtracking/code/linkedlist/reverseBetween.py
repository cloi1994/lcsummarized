# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(1)
        
        root.next = head
        
        head  = root
        
        for i in range(m-1):
            head = head.next
        
        pre = head.next 
        cur = pre.next

        for i in range(n-m):
            curNext = cur.next
            cur.next = pre
            pre = cur
            cur = curNext
        
        head.next.next = cur
        head.next = pre
        
        return root.next
        
