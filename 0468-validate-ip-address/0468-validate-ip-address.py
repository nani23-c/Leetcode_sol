class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            queryIp1 = queryIP
            queryIp1 = queryIp1.split(".")
            if len(queryIp1)!=4:
                return "Neither"
            for i in queryIp1:
                try:
                    if len(i)>1:
                        if i[0]=='0':
                            return "Neither"

                    if int(i)<256 and int(i)>-1:
                        ans = True 
                    else:
                        return "Neither"
                except:
                    return "Neither"
            return "IPv4"
        else:
            queryIp1 = queryIP
            queryIp1 = queryIp1.split(":")
            possibilities = ['0','1','2','3','4','5','6','7','8','9','a','A','b','B','c','C','d','D','e','E','f','F']
            if len(queryIp1)!=8:
                return "Neither"
            for i in queryIp1:
                if len(i)>4 or len(i)<1:
                    return "Neither"
                for j in i:
                    if j not in possibilities:
                        return "Neither"
            return "IPv6"




        