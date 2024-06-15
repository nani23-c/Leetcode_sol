class Solution:
    def frequencySort(self, s: str) -> str:
        dicti = {}
        ans = ""
        for i in range(len(s)):
            if s[i] in dicti:
                dicti[s[i]] +=1 
            else:
                dicti[s[i]] = 1
        ndict = sorted(dicti.items(), key=lambda item: item[1])
        for key,value in ndict:
            for i in range(value):
                ans = key+ans 

        return ans
    