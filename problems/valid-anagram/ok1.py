#!/usr/bin/env python3

'''
https://leetcode.com/problems/valid-anagram/
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t) == True)
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t) == False)
