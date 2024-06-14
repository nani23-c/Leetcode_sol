class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dicti = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        a=[]
        if len(digits)==0:
            return a
        def combo(emptysting,digit):
            if len(digit)==0:
                a.append(emptysting)
            else:
                if digit[0] == '7' or digit[0] == '9':
                    combo(emptysting+dicti[digit[0]][0],digit[1:])
                    combo(emptysting+dicti[digit[0]][1],digit[1:])
                    combo(emptysting+dicti[digit[0]][2],digit[1:])
                    combo(emptysting+dicti[digit[0]][3],digit[1:])
                else:
                    combo(emptysting+dicti[digit[0]][0],digit[1:])
                    combo(emptysting+dicti[digit[0]][1],digit[1:])
                    combo(emptysting+dicti[digit[0]][2],digit[1:])
        e = ''
        combo(e,digits)
        return a




        