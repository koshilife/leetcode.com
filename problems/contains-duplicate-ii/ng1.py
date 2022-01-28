class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for _j in range(1, k + 1):
                j = i + _j
                if j > len(nums) - 1:
                    break
                if nums[i] == nums[j]:
                    return True
        return False
