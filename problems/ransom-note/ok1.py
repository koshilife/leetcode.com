#!/usr/bin/env python3

'''
https://leetcode.com/problems/ransom-note/
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_dic = {}
        for s in magazine:
            if s not in count_dic:
                count_dic[s] = 0
            count_dic[s] += 1
        for s in ransomNote:
            if s not in count_dic:
                return False
            if count_dic[s] == 0:
                return False
            count_dic[s] -= 1
        return True

if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"
    print(Solution().canConstruct(ransomNote, magazine) == False)
    ransomNote = "aa"
    magazine = "ab"
    print(Solution().canConstruct(ransomNote, magazine) == False)
    ransomNote = "aa"
    magazine = "aab"
    print(Solution().canConstruct(ransomNote, magazine) == True)
    ransomNote = "aab"
    magazine = "baa"
    print(Solution().canConstruct(ransomNote, magazine) == True)
