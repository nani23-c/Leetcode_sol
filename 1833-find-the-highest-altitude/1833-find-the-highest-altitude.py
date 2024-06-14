class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        out = [0]
        for i in range(len(gain)):
            out.append(out[-1]+gain[i])
        return max(out)
        