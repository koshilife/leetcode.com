#!/usr/bin/env python3

'''
https://leetcode.com/problems/path-sum/
'''

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        def search(_node, current_sum, depth=0):
            current_sum += _node.val
            if current_sum == target_sum and (not _node.left and not _node.right):
                return True
            if _node.left and search(_node.left, current_sum, depth+1):
                return True
            if _node.right and search(_node.right, current_sum, depth+1):
                return True
            return False
        return search(root, 0) if root else False

if __name__ == '__main__':
    # ex1
    root = TreeNode(5)
    node4 = TreeNode(4)
    node11 = TreeNode(11)
    node7 = TreeNode(7)
    node2 = TreeNode(2)

    node8 = TreeNode(8)
    node13 = TreeNode(13)
    node4 = TreeNode(4)
    node1 = TreeNode(1)

    root.left = node4
    root.right = node8
    node4.left = node11
    node11.left = node7
    node11.right = node2
    node8.left = node13
    node8.right = node4
    node4.right = node1
    print(Solution().hasPathSum(root, 22) == True)

    # ex2
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().hasPathSum(root, 5) == False)

    # ex3
    print(Solution().hasPathSum(None, 0) == False)

    # ex4
    root = TreeNode(1, TreeNode(2))
    print(Solution().hasPathSum(root, 1) == False)

    # ex5
    root = TreeNode(1)
    print(Solution().hasPathSum(root, 1) == True)

    # ex6
    root = TreeNode(1)
    print(Solution().hasPathSum(root, 0) == False)

