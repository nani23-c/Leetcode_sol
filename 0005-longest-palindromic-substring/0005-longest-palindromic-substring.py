class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = 0 
        temp = ''
        out = ''
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp = temp+s[j]
                if temp == temp[::-1] and len(temp)>lenth:
                    lenth = len(temp)
                    out  = temp 
            temp = ""
        return out
        