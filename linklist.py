# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 13:37:56 2016

@author: yaoxia
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def CrtList(self,head):
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
        
        
    def CreatLinkList(self,nums):
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
        
    def rmListVal(self,lst,val):
        if all(num != val for num in lst):
            return lst
        else:
            lst.remove(val)
        self.rmListVal(lst,val)
        return lst
        