class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split(" ")
        k=''
        o=''
        h=len(s)
        for i in  range(h+1):
            k=k+'a'
        b=[]
      
        for i in  range(len(s)):
            a=s[i]
            if(a[0]=='A' or a[0]=='E' or a[0]=='I'or a[0]=='O' or a[0]=='U' or a[0]=='a' or a[0]=='e' or a[0]=='i'or a[0]=='o' or a[0]=='u' ):
                a=a+'ma'
            else:
                a=a[1:]+a[0]+'ma'
            a=a+k[:i+1]
            if(i!=h-1):
               o=o+a+' '
            else:
                o=o+a
        return o
        