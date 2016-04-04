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
        if not root:
            return
            #print '     ', root.cargo
        if root.left and not root.right:
            print (root.cargo,root.left.cargo,'null'),
            self.prtlfs(root.left)
            self.prtlfs(root.right)
        elif root.right and not root.left:
           
            print (root.cargo,'null',root.right.cargo), 
            self.prtlfs(root.left)
            self.prtlfs(root.right)
        elif root.right and  root.left:
            print (root.cargo,root.left.cargo,root.right.cargo), 
            self.prtlfs(root.left)
            self.prtlfs(root.right)
        else:
            print (root.cargo,'null','null'),
            self.prtlfs(root.left)
            self.prtlfs(root.right)
        return

class Solution(object):
    def maxDepth(self,root): 
        
        def dfs(lvl,root,res):        
            if root:
                if lvl > res[0]:
                    res[0] = lvl                            
                dfs(lvl+1,root.left,res)
                dfs(lvl+1,root.right,res)
        res = [0]
        dfs(1,root,res)
                #print '     ', root.cargo11            
        return res[0] 


a = Tree(1,Tree(2,None ,None),Tree(3, None,Tree(5,Tree(7),None)))
#a = Tree(1,Tree(2),Tree(3))
a.prtlfs(a)
b = Solution()
depth = b.maxDepth(a)
print depth
