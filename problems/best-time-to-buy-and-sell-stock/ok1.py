#!/usr/bin/env python3

'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = prices[0]
        max_num = 0
        ans = 0
        is_continue = False
        for current in prices[1:]:
            if current >= min_num:
                max_num = max(max_num, current)
                is_continue = True
            else:
                if is_continue:
                    ans = max(ans, max_num - min_num)
                max_num, min_num, is_continue = current, current, False
        if is_continue:
            ans = max(ans, max_num - min_num)
        return ans

if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4]) == 5)
    print(Solution().maxProfit([7,6,4,3,1]) == 0)
