class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if(low%2==0 and high%2==0):
            return int((high-low)/2)
        elif((low%2==0 and high%2==1) or (low%2==1 and high%2==0)):
            return int((high-low+1)/2)
        else:
            return int(((high-low)/2)+1)