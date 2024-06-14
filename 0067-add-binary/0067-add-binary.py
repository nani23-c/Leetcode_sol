class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=str(a)
        b=str(b)
        an=0
        bn=0
        a1=len(a)-1
        b1=len(b)-1
        for i in range(a1,-1,-1):
            k=int(a[a1-i])
            an=an+k*(2**i)
        for i in range(b1,-1,-1):
            k=int(b[b1-i])
            bn=bn+k*(2**i)
        c=an+bn
        return bin(c).replace("0b","")
            
