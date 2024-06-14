class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=0
        for i in jewels:
            for j in range(len(stones)):
               if(i==stones[j]):
                   a=a+1

        return a