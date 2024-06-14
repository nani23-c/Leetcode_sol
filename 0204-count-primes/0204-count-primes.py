class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = isPrime[1] =False

        for i in range(2, int(n**0.5) + 1):
            if isPrime[i] == True:
                for j in range(i*i, n, i):
                    isPrime[j] = False 
        if n<=2:
            count=0 
        else:
            count=1

        for i in range(3,n,2):
            if isPrime[i] == True:
                count += 1

        return count
        