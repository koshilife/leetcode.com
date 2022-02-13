#!/usr/bin/env python3

'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# refs: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/1765377/Python3-or-easiest-solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res+= [root.val]
            res+= self.preorderTraversal(root.left)
            res+= self.preorderTraversal(root.right)
        return res

if __name__ == "__main__":
    root = TreeNode([1,None,2,3])
    print(Solution().preorderTraversal(root))
    root = TreeNode([])
    print(Solution().preorderTraversal(root))
    root = TreeNode([1])
    print(Solution().preorderTraversal(root))
