class Solution:
    def reverseParentheses(self, s: str) -> str:
        arr=[""]
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                arr.append("")
            elif s[i]==")":
                temp=arr.pop(-1)
                arr[-1] = temp[::-1]+arr[-1]
            else:
                arr[-1] = s[i]+arr[-1]
        return arr[-1][::-1]
            

        