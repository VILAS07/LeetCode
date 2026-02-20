class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        #11011000
        if len(s)<=2:
            return s
        count=0
        start=0
        substring=[]
        for i in  range(len(s)):
            if s[i]=='1':
                count+=1
            else:
                count-=1
            if count==0:
                inside=self.makeLargestSpecial(s[start+1:i])
                substring.append('1'+inside+'0')
                start=i+1
        substring.sort(reverse=True)
        return ''.join(substring)
        
        