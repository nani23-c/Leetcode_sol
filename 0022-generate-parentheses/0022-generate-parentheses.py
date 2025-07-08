class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(lp,rp,valid):
            if lp==n and rp==n:
                ans.append(valid)
                return
            if lp<n:
                generate(lp+1,rp,valid+"(")
            if rp<n and rp<lp:
                generate(lp,rp+1,valid+")")
        ans = []
        generate(0,0,"")
        return ans 
                