class Solution:
    def climbStairs(self, n: int) -> int:
        a=[0,1]
        for i in range(n):
            b=a[0]
            a[0]=a[1]
            a[1]=b+a[1]
        return a[1]