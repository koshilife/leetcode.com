# https://leetcode.com/problems/merge-sorted-array/

from typing import List

# NG理由: 問題文をよく読みましょう。returnではなく、元々のnums1を破壊的変更しましょうという意味
"""
>The final sorted array should not be returned by the function,but instead be stored inside the array nums1.
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        ans = [*nums1[0:m], *nums2[0:n]]
        ans.sort()
        return ans

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(Solution().merge(nums1, m, nums2, n) == [1,2,2,3,5,6])

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(Solution().merge(nums1, m, nums2, n) == [1])

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n) == [1])

