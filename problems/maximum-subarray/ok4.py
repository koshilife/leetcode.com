# https://leetcode.com/problems/maximum-subarray/

# refs https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# Solution - V (Kadane's Algorithm)

class Solution:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -100000
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now
