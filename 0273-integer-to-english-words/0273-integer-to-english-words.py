class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        one_map = {
            1:'One',
            2:'Two',
            3:'Three',
            4:'Four',
            5:'Five',
            6:'Six',
            7:'Seven',
            8:'Eight',
            9:'Nine',
            10:'Ten',
            11:'Eleven',
            12:'Twelve',
            13:'Thirteen',
            14:'Fourteen',
            15:'Fifteen',
            16:'Sixteen',
            17:'Seventeen',
            18:'Eighteen',
            19:'Nineteen'
        }

        tens_map = {
            20:'Twenty',
            30:'Thirty',
            40:'Forty',
            50:'Fifty',
            60:'Sixty',
            70:'Seventy',
            80:'Eighty',
            90:'Ninety'
        }

        def tri(digits):
            temp = []
            hundred = digits//100
            last_two = digits%100
            if hundred:
                temp.append(one_map[hundred] + " Hundred")
            if last_two >= 20:
                tens,ones = last_two//10,last_two%10
                temp.append(tens_map[tens*10])
                if ones:
                    temp.append(one_map[ones])
            elif last_two:
                temp.append(one_map[last_two])
            return " ".join(temp)
        postfix = ["", " Thousand"," Million"," Billion"]
        i = 0
        res = []
        while num:
            digits = num % 1000
            s = tri(digits) 
            if s:
                res.append(s + postfix[i])
            i+=1
            num = num //1000
        res.reverse()
        return " ".join(res)


        