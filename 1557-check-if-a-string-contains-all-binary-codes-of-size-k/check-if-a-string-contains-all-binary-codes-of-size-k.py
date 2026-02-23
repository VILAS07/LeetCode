class Solution(object):
    def hasAllCodes(self, s, k):
        hashset = set()

        for i in range(len(s) - k + 1):
            hashset.add(s[i : i + k])

        return len(hashset) == (2 ** k)