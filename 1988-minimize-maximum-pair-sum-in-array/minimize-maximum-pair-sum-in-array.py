class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        start=0
        end=len(nums)-1
        maxpair=0
        pairsum=0
        while start<end:
            pairsum=nums[start]+nums[end]
            if pairsum > maxpair:
                maxpair = pairsum
            start+=1
            end-=1
        return maxpair