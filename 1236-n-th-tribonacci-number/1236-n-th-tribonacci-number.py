class Solution:
    def tribonacci(self, n: int) -> int:
        a = [0,1,1]
        if n==0:
            return 0
        for i in range(3,n+1):
            a.append(a[i-1]+a[i-2]+a[i-3])
        return a[-1]
        