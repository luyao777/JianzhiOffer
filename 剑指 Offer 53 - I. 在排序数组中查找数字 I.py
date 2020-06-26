class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if abs(target - nums[0]) < abs(target - nums[-1]):
            for i in range(len(nums)):
                if nums[i] == target:
                    break
            cnt = 0
            while (nums[i] == target and i < len(nums)):
                cnt += 1
                i += 1
            return cnt
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == target:
                    break
            cnt = 0
            while (nums[i] == target and i > -1):
                cnt += 1
                i -= 1
            return cnt
