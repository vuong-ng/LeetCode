# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #copy to another linked list
        """
        res = ListNode()
        curr = res
        if head == None:
          return res.next
        
        while head!= None:
          if head.val != val:
            curr.next = ListNode()
            curr = curr.next
            curr.val = head.val
            head = head.next
            
          else:
            head = head.next
            continue

        curr = None
        return res.next
        """
        #sentinel node
        sentinel = ListNode(0)
        sentinel.next = head
        curr,prev = head, sentinel

        while curr != None:
          if curr.val == val:
            prev.next = curr.next
          else:
            prev = curr
          curr = curr.next
        return sentinel.next
          
