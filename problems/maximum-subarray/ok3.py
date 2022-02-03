# https://leetcode.com/problems/maximum-subarray/

# refs https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# Solution - IV (Dynamic Programming - Tabulation)

'''
We can actually do away with just 1 row as well. We denoted dp[1][i] as the maximum subarray sum ending at i.
We can just store that row and calculate the overall maximum subarray sum at the end by choosing the maximum of all max subarray sum ending at i.
'''

class Solution:
    def maxSubArray(self, nums):
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

if __name__ == '__main__':
    print(Solution().maxSubArray([1,-2,3,-4,5]))

