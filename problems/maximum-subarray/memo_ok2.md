# https://leetcode.com/problems/maximum-subarray/

# refs https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer

> Solution - IV (Dynamic Programming - Tabulation)

```py
class Solution:
    def maxSubArray(self, nums):
        dp = [[0]*len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]
```

# なぜこのDPがワークするのかシミュレーション

- シミュレーションして計算が合うことは理解。

- 漸化式:
  - dp[1][i] index-iまで nums[i]を含む場合の最大値 (nums[i]のみ、nums[i]まで全ての和)
  - dp[0][i] index-iまで nums[i]を含まない場合の最大値 (i-1まででの i-1を含まない場合、含む場合が大きい方の最大値)

