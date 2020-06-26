class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        content = s.rstrip().lstrip().split(' ')
        content.reverse()
        result = content[0]
        if len(content) == 1:
            return result
        for c in content[1:]:
            if c == '':
                continue
            result += ' ' + c
        return result