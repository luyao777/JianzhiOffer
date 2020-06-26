class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return matrix
        width = len(matrix[0])
        height = len(matrix)
        nums = width * height
        i, j = 0, 0
        result = [matrix[0][0]]
        matrix[0][0] = 's'
        direct = 'right'
        while (1):
            if len(result) == nums:
                break
            if direct == 'right' and j + 1 < width and matrix[i][j + 1] != 's':
                j += 1
            elif direct == 'right' and (j + 1 == width
                                        or matrix[i][j + 1] == 's'):
                direct = 'down'
                continue
            elif direct == 'down' and i + 1 < height and matrix[i +
                                                                1][j] != 's':
                i += 1
            elif direct == 'down' and (i + 1 == height
                                       or matrix[i + 1][j] == 's'):
                direct = 'left'
                continue
            elif direct == 'left' and j - 1 > -1 and matrix[i][j - 1] != 's':
                j -= 1
            elif direct == 'left' and (j - 1 == -1 or matrix[i][j - 1] == 's'):
                direct = 'up'
                continue
            elif direct == 'up' and i - 1 > -1 and matrix[i - 1][j] != 's':
                i -= 1
            elif direct == 'up' and (i - 1 == -1 or matrix[i - 1][j] == 's'):
                direct = 'right'
                continue

            result.append(matrix[i][j])
            matrix[i][j] = 's'

        return result
