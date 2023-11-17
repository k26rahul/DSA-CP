# https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n):
        if n == 1:
            return 5
        elif n % 2 == 0:
            c = 20 ** (n/2)
        else:
            c = (20 ** (n-1)/2) * 5
        return int(c % (10 ** 9 + 7))
