class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")
        n = len(a)
        m = len(b)
        if n<m:
            while(len(a)<len(b)):
                a.append(0)
        else:
            while(len(a)>len(b)):
                b.append(0)
        n = len(a)
        for i in range(n):
            if int(a[i])>int(b[i]):
                return 1 
            if int(a[i])<int(b[i]):
                return -1 
        return 0

        