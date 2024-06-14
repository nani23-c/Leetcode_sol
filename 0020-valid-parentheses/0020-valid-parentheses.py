class Solution:
    def isValid(self, s: str) -> bool:
        a="({["
        A=")}]"
        b=[]
        B=[]
        if(len(s)==1):
            return False
        for i in s:
            if(i in a):
                b.append(i)
            if(len(b)==0 and (i in A)):
                return False
            if(i==')' and b[-1]=='('):
                b.pop()
            elif(i==')' and b[-1]!='('):
                B.append(i)
            if(i=='}' and b[-1]=='{'):
                b.pop()
            elif(i=='}' and b[-1]!='{'):
                B.append(i)
            if(i==']' and b[-1]=='['):
                b.pop()
            elif(i==']' and b[-1]!='['):
                B.append(i)
        if(len(b)==0 and len(B)==0):
            return True
        else:
            return False
            