class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        distance = 0
        binary=bin(n)[2:]
        i = 0
        j = 1
        while j <len(binary):
            if binary[j] != '1':
                j+=1
                continue
            if binary[j] == '1':
                distance = max(distance, j-i)
                i=j
                j+=1
        return distance

        