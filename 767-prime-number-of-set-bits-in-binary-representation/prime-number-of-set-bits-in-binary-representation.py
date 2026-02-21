class Solution(object):
    def countPrimeSetBits(self, left, right):
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        count = 0
        
        for i in range(left, right + 1):
            binary = format(i, 'b')
            n = binary.count('1')
            if is_prime(n):
                count += 1
        
        return count