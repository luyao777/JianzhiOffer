class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = 0
        j = len(matrix[0]) - 1
        while (matrix[i][j] != target):
            _i, _j = i, j
            if matrix[i][j] > target:
                if j > 0:
                    j -= 1
            if matrix[i][j] < target:
                if i < len(matrix) - 1:
                    i += 1
            if _i == i and _j == j:
                break
        return True if matrix[i][j] == target else False
