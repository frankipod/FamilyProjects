# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 08:21:24 2016

@author: yaoxia

"""
class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)
        
    def prtlfs(self,root):
        if root:
            if root.left and root.right:
                print '     ', root.cargo
                print root.left.cargo,'         ',     root.right.cargo,'\n'
                self.prtlfs(root.left)
                self.prtlfs(root.right)
        return

count = 1
class Solution(object):
    def maxDepth(self,root): 
        global count
        if root:
              
            if root.left:
                self.maxDepth(root.left)
                count += 1
                if root.right:
                    self.maxDepth(root.right)
                    count += 1
        return count




a = Tree(1,Tree(2,None ,None),Tree(3, None,Tree(5)))
a.prtlfs(a)
b = Solution()
depth = b.maxDepth(a)
print depth
