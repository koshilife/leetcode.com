#!/usr/bin/env python3

'''
https://leetcode.com/problems/reshape-the-matrix/
'''

import math
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ans = []
        ans_row = []
        total = r * c
        lines = math.ceil(c / r)
        cnt = 0
        is_break = False
        for row in mat:
            for i in row:
                if cnt >= total:
                    is_break = True
                    break
                ans_row.append(i)
                if len(ans_row) == lines or len(ans_row) == c:
                    ans.append(ans_row.copy())
                    ans_row = []
                cnt += 1
            if is_break:
                break
        print(ans)
        return ans

if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    print(Solution().matrixReshape(mat, r, c) == [[1,2,3,4]])
    print('----')
    mat = [[1,2],[3,4]]
    r = 2
    c = 4
    print(Solution().matrixReshape(mat, r, c) == [[1,2],[3,4]])
    print('----')
    mat = [[1,2],[3,4]]
    r = 4
    c = 1
    print(Solution().matrixReshape(mat, r, c) == [[1],[2],[3],[4]])
    print('----')
    mat = [[1,2,3,4]]
    r = 2
    c = 2
    print(Solution().matrixReshape(mat, r, c) == [[1,2],[3,4]])
    print('----')
