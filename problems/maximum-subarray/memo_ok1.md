# https://leetcode.com/problems/maximum-subarray/

# refs https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer
# Solution - III (Dynamic Programming - Memoization)

```py
class Solution:
    def maxSubArray(self, nums):
        inf = 1000000
        memo = {}
        def solve(i, must_pick):
            if (i, must_pick) in memo:
                return memo[(i, must_pick)]
            if i >= len(nums):
                _ans =  0 if must_pick else -inf
            else:
                _ans = max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
            memo[(i, must_pick)] = _ans
            return _ans
        return solve(0, False)
```

# なぜこの再帰がワークするのかシミュレーション

```
nums:[1,-2,3,-4]
i:0, False
(1番目を選びません)
max(1 + f(1, True), f(1, False)) => max(2, 3) => 3
 - i:1, True
   - max(-2 + f(2, True), 0) => max(1, 0) => 1
     - i:2, True
       max(3 + f(3, True), 0) => max(3, 0) => 3
       - i:3, True
       max(-4 + f(4, True), 0) => max(-4, 0) => 0
       - i:4, True
       return 0
 - i:1, False
   - max(-2 + f(2, True), f(2, False))) => max(-1, 3) => 3
     - i:2, True => 1
     - i:2, False
       max(3 + f(3, True), f(3, False)) => max(3, -4) => 3
       - i:3, True => 0
       - i:3, False
         max(-4 + f(4, True), f(4, False)) => max(-4, -INF) => -4
         - i:4, True => 0
         - i:4, False => -INF
```

感想:
must_pick の変数名がしっくりこないが、やっている内容は理解。
DPを考えるのが苦手ならメモ化再帰を検討する。
