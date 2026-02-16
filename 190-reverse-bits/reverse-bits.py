class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binaryN = format(n, 'b').zfill(32)
        return int(binaryN[::-1], 2)
        