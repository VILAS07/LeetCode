class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
        for i in l:
            a=i
        return a
        