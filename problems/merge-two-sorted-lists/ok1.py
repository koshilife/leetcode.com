#!/usr/bin/env python3

'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''

from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# refs: https://leetcode.com/problems/merge-two-sorted-lists/discuss/1767277/Python-Simple-Python-Solution-With-Two-Approach
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()
        newlistptr = newlist
        while l1 and l2:
            if l1.val <= l2.val:
                newlistptr.next = l1
                l1 = l1.next
            else:
                newlistptr.next = l2
                l2 = l2.next
            newlistptr = newlistptr.next
        if l1 != None:
            newlistptr.next = l1
        else:
            newlistptr.next = l2
        return newlist.next


