# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        cur = head
        
        while cur:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
        return prev
        
    #with new space
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        cur = head
        
        while cur:
            newCur = ListNode(cur.val)
            newCur.next = prev
            prev = newCur
            cur = cur.next
        return prev
    #recursive
        
    def reverse(self,pre,cur): 
        if cur == None:
            return pre
        
        curNext = cur.next
        cur.next = pre
        return self.reverse(cur,curNext)
        
