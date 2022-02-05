#!/usr/bin/env python3

'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/

NG: 問題文と例題をちゃんと試そう。
Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        return [i for i in nums2 if i in nums1_set]

if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect(nums1, nums2) == [2,2])

    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2) == [4,9])
