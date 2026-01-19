class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ' and c > 0:
                break
            if s[i] != ' ':
                c += 1
        return c


        