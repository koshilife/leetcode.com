#!/usr/bin/env python3

'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        longer, shorter = (nums1, nums2) if len(nums1) > len(nums2) else (nums2, nums1)

        val_dic = {}
        for i, val in enumerate(longer):
            if val not in val_dic:
                val_dic[val] = []
            val_dic[val].append(i)

        ans = []
        for val in shorter:
            if (val not in val_dic) or (not val_dic[val]):
                continue
            ans.append(val)
            val_dic[val].pop()
        return ans

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect(nums1, nums2) == [2,2])

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2) == [4,9])
