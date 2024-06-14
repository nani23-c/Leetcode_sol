class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=s.split(" ")
        i=-1
        a=0
        while(a<1):
            if(len(k[i])==0):
               i=i-1
            else:
                a=3
        

        a=k[i]
        b=len
        return len(a)