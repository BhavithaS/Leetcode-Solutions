#Approach -1

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 :
            return n
        d = [0]*(n+1)
        d[0] = 0
        d[1] = 1
        d[2] = 2

        for i in range(3,n+1) :
            d[i] = d[i-1] + d[i-2]
        return d[n]
    
#Approach - 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2 : return n

        first = 1
        second = 2
        for i in range(3,n+1) :
            res = first + second
            first , second = second , res
        return res