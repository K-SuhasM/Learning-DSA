'''Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
                        Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1
                        Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16
                        Example 3:
Input: n = 3
Output: false'''

# def pow(n):
#     if n <= 0:
#         return False

#     if n == 1:
#         return True

#     if n % 2 != 0:
#         return False

#     return pow(n // 2)

# print(pow(16))

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        return (n % 2 == 0) and self.isPowerOfTwo(n // 2)

