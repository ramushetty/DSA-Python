# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.


from typing import List

class Solution:
    def fib(self, n: int) -> int:
        # a = 0
        # b = 1
        # if n == 0:
        #     return a
        # elif n == 1:
        #     return b
        # else:
        #     for i in range(1,n):
        #         a,b = b,a+b
            
        #     return b

        if n == 0:
             return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        


n = 2
solution = Solution()
print(solution.fib(n))