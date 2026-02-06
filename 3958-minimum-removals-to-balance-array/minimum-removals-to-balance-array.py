class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        l = 0
        max_keep = 1

        for i in range(n):
            while nums[i] > nums[l] * k:
                l += 1
            max_keep = max(max_keep, i - l + 1)

        ans = n - max_keep
        return ans
        