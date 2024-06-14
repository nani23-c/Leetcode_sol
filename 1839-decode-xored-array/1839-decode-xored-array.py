class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        n = len(encoded)
        for i in range(n):
            ans.append(ans[i]^encoded[i])
        return ans

        