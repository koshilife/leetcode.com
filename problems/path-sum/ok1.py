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

# refs: https://leetcode.com/problems/path-sum/discuss/1774185/Python-Simple-solution-or-Find-sum-of-every-possible-path
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        def check(node, tmp):
            if node:
                if node.left:
                    node.left.val += node.val
                    check(node.left, tmp)
                if node.right:
                    node.right.val += node.val
                    check(node.right, tmp)
                elif not node.left:
                    tmp.append(node.val)
            return tmp

        if target_sum in check(root, []):
            return True
        else:
            return False

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

