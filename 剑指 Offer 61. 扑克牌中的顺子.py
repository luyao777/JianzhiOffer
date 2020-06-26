class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        kings_num = 0

        for num in nums:
            if num == 0:
                kings_num += 1
        for _ in range(kings_num):
            nums.remove(0)

        min_num = min(nums)
        max_num = max(nums)

        check_num = max_num - min_num + 1

        miss_num = 0
        for i in range(min_num, max_num + 1):
            if i not in nums:
                miss_num += 1

        # print(nums, miss_num, check_num, kings_num)

        if miss_num > kings_num:
            return False

        kings_num -= miss_num

        if (5 - check_num) > kings_num:
            return False

        return True
