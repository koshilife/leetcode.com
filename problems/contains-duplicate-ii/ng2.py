class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            j = i + k + 1
            if j > len(nums) - 1:
                j = len(nums)
            _nums = nums[i:j]
            if not len(set(_nums)) == len(_nums):
                return True
        return False


if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    print('test1', Solution().containsNearbyDuplicate(nums, k))
    nums = [1,0,1,1]
    k = 1
    print('test2', Solution().containsNearbyDuplicate(nums, k))
    nums = [1,2,3,1,2,3]
    k = 2
    print('test3', Solution().containsNearbyDuplicate(nums, k))
