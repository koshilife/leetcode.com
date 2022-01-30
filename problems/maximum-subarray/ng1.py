# dp[i][j] = 始点iからjまでの間での部分和の最大値
# 漸化式の定義
# 一般化:
#  if i == j:
#    dp[i][j] = nums[i]
#  else:
#    dp[i][j] = max(dp[i][j-1], sum(nums[i,j]))
#

# https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _min = -100000
        ans = _min
        nums_len = len(nums)
        dp = [[_min] * nums_len for i in range(nums_len)]

        for i in range(nums_len):
            for j in range(i, nums_len):
                if j == i:
                    dp[i][j] = nums[i]
                else:
                    _total= sum(nums[i:j+1])
                    if dp[i][j-1] > _total:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = _total
            _ans = dp[i][nums_len-1]
            if _ans > ans:
                ans = _ans
        # check dp table:
        # for i in range(nums_len):
        #     print(i, dp[i])
        return ans

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print('test1', Solution().maxSubArray(nums))
    nums = [1]
    print('test2', Solution().maxSubArray(nums))
    nums = [5,4,-1,7,8]
    print('test3', Solution().maxSubArray(nums))
