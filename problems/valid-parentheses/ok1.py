#!/usr/bin/env python3

'''
https://leetcode.com/problems/valid-parentheses/

(memo)
スタックを用いて、現在オープンしている括弧種別を管理する。
1文字列づつ走査して、オープンならスタックに積み、クローズなら直前のオープンされている括弧に対応する括弧か判定し
合致していたら、スタックからポップして、最後まで行い、最終的にオープンスタックがなければOK.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        def is_open(c):
            return c in ['(', '{', '[']
        def is_close(c):
            return c in [')', '}', ']']
        def expected_close_bracket(c):
            if c == '(': return ')'
            if c == '{': return '}'
            if c == '[': return ']'
            raise

        opening = []
        for c in s:
            if is_open(c):
                opening.append(c)
                continue
            if is_close(c):
                length = len(opening)
                if length == 0:
                    return False
                expected = expected_close_bracket(opening[length-1])
                if c != expected:
                    return False
                opening.pop()
                continue
            raise
        return len(opening) == 0


if __name__ == "__main__":
    s = '()'
    print(Solution().isValid(s) == True)
    s = '()[]{}'
    print(Solution().isValid(s) == True)
    s = '(]'
    print(Solution().isValid(s) == False)
