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
        def search(_node, current_sum):
            current_sum += _node.val
            if current_sum == target_sum:
                return True
            if _node.left and search(_node.left, current_sum):
                return True
            if _node.right and search(_node.right, current_sum):
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

    print(Solution().hasPathSum(root, 22))
