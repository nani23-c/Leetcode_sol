class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        a = sentence.split(" ")
        A = len(a)
        for i in range(A):
            for j in dictionary:
                k = len(j)
                if a[i][:k]==j:
                    a[i]=j
                
        return ' '.join(a)
        