# https://leetcode.com/problems/two-sum/

from typing import List

# Solution: HashMap.
# The time complexity is O(n).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}
        for i, num in enumerate(nums):
            if num not in num_dic:
                num_dic[num] = []
            num_dic[num].append(i)

        for a in num_dic.keys():
            b = target - a
            if b not in num_dic:
                continue
            indexes = num_dic[b]
            if a == b:
                if len(indexes) > 1:
                    ans = indexes[0:2]
                else:
                    continue
            else:
                ans = [num_dic[a][0], indexes[0]]
            ans.sort()
            return ans
        raise 'there is no answer'


if __name__ == '__main__':
    nums = [2,7,11,15]
    t = 9
    print('---- test1', Solution().twoSum(nums, t))

    nums = [3,2,4]
    t = 6
    print('---- test2', Solution().twoSum(nums, t))

    nums = [3,3]
    t = 6
    print('---- test3', Solution().twoSum(nums, t))

    nums = [0,4,3,0]
    t = 0
    print('---- test4', Solution().twoSum(nums, t))

    nums = [-10,7,19,15]
    t = 9
    print('---- test5', Solution().twoSum(nums, t))
