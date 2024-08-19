# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        currA = headA
        currB = headB
        while currA != currB:
            if currA == None:
                currA=headB
            else: currA=currA.next
            
            if currB == None:
                currB = headA
            else: currB = currB.next
        return currA
        #hash table
        """
        nodes={}
        while headB != None:
            nodes[headB] = 1
            headB=headB.next
        while headA != None:
            if headA in nodes:
                return headA
            headA= headA.next
        return headA
        """

            