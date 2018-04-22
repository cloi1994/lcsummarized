# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # [1,2,3,4,5] k = 2
        # prev the node before 4, which is 3
        
        if not head or k == 0:
            return head
        
        n = 1
        
        root = ListNode(1)
        root.next = head
        pre = end = head
        
        while end.next:
            n += 1
            end = end.next
            
        steps = n - k % n
          

        for i in range(steps-1):
            pre = pre.next
            
        
        
        end.next = root.next
        root.next = pre.next
        pre.next = None
        
        
        return root.next
            
            
        
        
        
