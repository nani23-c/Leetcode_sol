class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lens = len(s)
        ds = { }
        dt = { }
        for i in range(lens):
            if s[i] in ds:
                ds[s[i]].append(i)
            else:
                ds[s[i]] =[i]
            if t[i] in dt:
                dt[t[i]].append(i)
            else:
                dt[t[i]]=[i]
        return list(ds.values())==list(dt.values())

            
            



        