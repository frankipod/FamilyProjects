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


class Solution(object):
    def invertTree(self,root):
        if root:
            root.right, root.left = root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root

a = Tree(1,Tree(2,Tree(3),Tree(4)),Tree(3,Tree(4),Tree(5)))
a.prtlfs(a)
b = Solution()
c = b.invertTree(a)
a.prtlfs(a)