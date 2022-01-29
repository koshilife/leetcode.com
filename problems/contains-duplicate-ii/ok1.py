# https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_len = len(nums)
        check_dic = {}

        # initialize check_dic
        for i in range(k+1):
            if i >= nums_len:
                break
            new = nums[i]
            if new in check_dic:
                return True
            check_dic[new] = True

        for i in range(k+1, nums_len):
            old = nums[i - k - 1]
            new = nums[i]
            del(check_dic[old])
            if new in check_dic:
                return True
            check_dic[new] = True
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
