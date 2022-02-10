#!/usr/bin/env python3

'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''

# from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        single = {}
        dup = {}
        for i, c in enumerate(s):
            if c in dup:
                continue
            if c in single:
                del single[c]
                dup[c] = True
            else:
                single[c] = i
        if len(single) == 0:
            return -1
        return single[list(single.keys())[0]]


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().firstUniqChar(s) == 0)
    s = "loveleetcode"
    print(Solution().firstUniqChar(s) == 2)
    s = "aabb"
    print(Solution().firstUniqChar(s) == -1)
