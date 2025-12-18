class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tot = 0
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                temp = stack.pop()
                temp2 = stack.pop()
                if i == "+":
                    stack.append((int(temp2)+int(temp)))
                elif i == "-":
                    stack.append((int(temp2)-int(temp)))
                elif i == "*":
                    stack.append((int(temp)*int(temp2))) 
                else:
                    stack.append(int(int(temp2)/int(temp)))
            else:
                stack.append(i)
            
        return int(stack[0])
