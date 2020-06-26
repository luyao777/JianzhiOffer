class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, res = 1, []

        while i * (i + 1) / 2 < target:
            if not (target - i * (i + 1) / 2) % (i + 1):
                x = int((target - i * (i + 1) / 2) // (i + 1))
                res.append(list(range(x, x + i + 1)))
            i += 1

        return res[::-1]