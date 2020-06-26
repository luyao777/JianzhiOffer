class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums
        left = 0
        right = len(nums)-1
        while(left != right):
            if (nums[right] % 2 == 1) and (nums[left] % 2 == 0):
                nums[right], nums[left] = nums[left], nums[right]
            if nums[right] % 2 == 0:
                right -= 1
            elif nums[left] % 2 == 1:
                left += 1
        return nums