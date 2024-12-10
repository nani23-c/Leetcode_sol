class Solution:
    def maximumLength(self, s: str) -> int:
        dictionary = {}
        temp = s[0]
        dictionary[s[0]]=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                dictionary[temp]+=1
                #dictionary[s[i]]+=1
                temp+=s[i]
                if temp in dictionary:
                    dictionary[temp]+=1
                else:
                    dictionary[temp]=1
            else:
                temp = s[i]
                if temp in dictionary:
                    dictionary[temp]+=1
                else:
                    dictionary[temp]=1
        ans = -1 
        for i in dictionary:
            if len(i)>=3:
                ans = max(ans,len(i)-2)
            if dictionary[i]>=3:
                ans = max(ans,len(i))
        return ans

            
            
        
        