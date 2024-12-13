class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        N = n
        ans =0 
        dicti = {}
        new = []
        values = [True]*n
        for i in range(n):
            if nums[i] in dicti:
                dicti[nums[i]].append(i)
            else:
                dicti[nums[i]]=[i]
                new.append(nums[i])
        new.sort() 
        i = 0
        m = len(new)
        while(n>0):
            a = dicti[new[i]]
            while(len(a)>0):
                if values[a[0]]==False:
                    a.pop(0)
                else:
                    if a[0]+1<N:
                        if values[a[0]+1]==True:
                            values[a[0]+1]=False 
                            n-=1
                    ans+=nums[a[0]]
                    values[a[0]]=False
                    n-=1
                    if a[0]-1>=0:
                        if values[a[0]-1]==True:
                            values[a[0]-1]=False
                            n-=1
                    a.pop(0)
            i+=1
        return ans


                

        

    