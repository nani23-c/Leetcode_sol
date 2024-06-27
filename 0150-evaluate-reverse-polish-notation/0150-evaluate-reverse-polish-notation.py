class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        for i in range(n):
            if tokens[i]=="*":
                a = stack.pop()
                b = stack.pop()
                temp = a*b
            elif tokens[i]=="+":
                a = stack.pop()
                b = stack.pop()
                temp = a+b
            elif tokens[i]=="/":
                a = stack.pop()
                b = stack.pop()
                temp = b/a
                temp = int(temp)
            elif tokens[i]=="-":
                a = stack.pop()
                b = stack.pop()
                temp = b-a
            else:
                temp = int(tokens[i])
            print(temp)
            stack.append(temp)
        return stack[0]

            