class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0 
        if k != 0:
            Dict = {}
            for i in nums:
                Dict[i]=1
            for i in Dict:
                if i+k in Dict:
                    ans+=1 
            return ans
        else:
            Dict = {}
            for i in nums:
                if i in Dict:
                    Dict[i]+=1
                    if Dict[i]==2:
                        ans+=1
                else:
                    Dict[i]=1 
            return ans                
        