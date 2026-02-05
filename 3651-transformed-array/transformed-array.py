class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = []

        for i in range(n):
            target = (i + nums[i]) % n
            result.append(nums[target])

        return result
            



        