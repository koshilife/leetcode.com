# https://leetcode.com/problems/merge-sorted-array/

from typing import List

# refs: https://leetcode.com/problems/merge-sorted-array/discuss/1744677/Python3-or-Faster-Solution-or-Easiest-or-3-Line-Code
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
