class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        max_fre = 0
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1

            if num_dict[i] > max_fre:
                max_fre = num_dict[i]
                max_num = i
        return max_num