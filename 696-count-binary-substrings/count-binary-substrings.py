class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group =[]
        temp=1
        n = len(s)
        ans = 0
        for i in range(1,n):
            if s[i-1]!=s[i]:
                group.append(temp)
                temp = 1
            else:
                temp +=1
        group.append(temp)
        for i in range(len(group)-1):
            ans += min(group[i],group[i+1])
        return ans
        