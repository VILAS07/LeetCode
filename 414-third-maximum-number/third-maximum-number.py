class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(dict.fromkeys(nums))
        nums.sort()
        if len(nums)>=3:
            return nums[-3]
        elif len(nums)==2 or len(nums)==1:
            return nums[-1]
        elif len(nums)==0:
            return nums


            
            
        