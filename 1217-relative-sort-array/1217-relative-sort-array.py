class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out1 = []
        out2 = []
        for i in arr2:
            for j in arr1:
                if i==j:
                    out1.append(i)
        for i in arr1:
            if i not in out1:
                out2.append(i)
        out2.sort()
        return out1+out2
        