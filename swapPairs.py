# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 14:14:02 2016

@author: yaoxia
"""
import linklst as ll
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

#    def swap (self,head):
##        if head.next:
##            if head.next.next:
#        node1 = head.next
#        node2 = head.next.next
#        node1.next = head.next.next.next
#        node2.next = node1
#        head.next = node2    
##                return head
##            return head
#        return head
 
    
    def swapPairs(self, head):
        dum = ListNode(1)
        dum.next = head
        def swap (head):
                node1 = head.next
                node2 = head.next.next
                node1.next = head.next.next.next
                node2.next = node1
                head.next = node2    
                return head
        
        while dum.next.next:
            print ll.CrtList(head), 'Start'  
   
            dum = swap(dum)
            dum = dum.next.next
            print ll.CrtList(head) ,'Finish'   
        return head
    
def swap (head):
    if head.next:
        if head.next.next:
            node1 = head.next
            node2 = head.next.next
            node1.next = head.next.next.next
            node2.next = node1
            head.next = node2


            return head
    return head

dum =  ListNode(0)
        
lst = [1,2,3,4,5,6,7]
a = ll.CreatLinkList(lst)
dum.next = a

#print ll.CrtList(dum.next)
#print ll.CrtList(swap(dum).next)


b = Solution()
c = b.swapPairs(a)
#
##
print ll.CrtList(c), 'Results'


