import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int: 
        o = n+m-2 
        n = n-1 
        m = m-1 
        o = math.factorial(o)
        n = math.factorial(n)
        m = math.factorial(m)
        k = n*m 
        o = int(o/k)
        return o
        

        