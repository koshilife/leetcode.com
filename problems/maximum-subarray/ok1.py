# https://leetcode.com/problems/maximum-subarray/

# refs https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# Solution - III (Dynamic Programming - Memoization)

class Solution:
    def maxSubArray(self, nums):
        inf = 1000000
        memo = {}
        def solve(i, must_pick):
            if (i, must_pick) in memo:
                return memo[(i, must_pick)]
            if i >= len(nums):
                _ans =  0 if must_pick else -inf
            else:
                _ans = max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
            memo[(i, must_pick)] = _ans
            return _ans
        return solve(0, False)
