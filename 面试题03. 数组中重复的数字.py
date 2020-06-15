class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while(nums[i] != nums[i+1] and i != len(nums)-1):
            i += 1
        return nums[i]