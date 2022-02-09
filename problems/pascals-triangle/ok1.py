#!/usr/bin/env python3

'''
https://leetcode.com/problems/pascals-triangle/
'''

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = []
            if i == 0:
                row.append(1)
            else:
                for j in range(i+1):
                    if (j == 0) or (j == i):
                        row.append(1)
                    else:
                        row.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(row)
        return ans

if __name__ == "__main__":
    print(Solution().generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
    print(Solution().generate(1) == [[1]])
