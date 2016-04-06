# -*- coding: utf-8 -*-
"""
Created on Tue Apr 05 15:41:45 2016

@author: yaoxia
"""

 #Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

        
def CrtList(head):
    if not head:
        lst = []        
        return lst
    lst = []
    def crtlist(head,lst):
        if head :
            lst.append(head.val) 
            crtlist(head.next,lst)
        return lst
    return crtlist(head,lst)
    
    
def CreatLinkList(nums):
    if not nums:
        a = None
        return a
    lst = []
    for num in nums:
        lst.append(ListNode(num))    
    for i in range(len(lst[:-1])):
        lst[i].next = lst[i+1] 
    a = lst[0]
    return a
def rmListVal(lst,val):
    if all(num != val for num in lst):
        return lst
    else:
        lst.remove(val)
    rmListVal(lst,val)
    return lst
    
class Solution(object):
    def removeElements(self, head ,value):
        headlist = CrtList(head)
        list2 =rmListVal(headlist,value)
        head = CreatLinkList(list2)
        return head

alist = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
print alist
alinklist = CreatLinkList(alist)
alist2 = CrtList(alinklist)

    
b = Solution()
c = b.removeElements(alinklist,9)
print CrtList(c)
