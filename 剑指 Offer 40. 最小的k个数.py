class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        # arr.sort()
        # return arr[:k]
        result = []
        nums = [0] * 10000
        for num in arr:
            nums[num] += 1
        s = 0
        while (k > 0):
            if nums[s] != 0:
                if nums[s] > k:
                    nums[s] = k
                result += [s] * nums[s]
                k -= nums[s]
            s += 1
        return result

