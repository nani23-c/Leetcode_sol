class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dicti={}
        for i in matches:
            if i[0] in dicti:
                dicti[i[0]][0]+=1
                dicti[i[0]][1]+=1 
            else:
                dicti[i[0]]=[1,1]
            if i[1] in dicti:
                dicti[i[1]][0]+=1
            else:
                dicti[i[1]]=[1,0]
        ans = [[],[]]
        for i in dicti:
            if (dicti[i][0]==dicti[i][1]):
                ans[0].append(i)
            elif (dicti[i][0]-dicti[i][1]==1):
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans

        