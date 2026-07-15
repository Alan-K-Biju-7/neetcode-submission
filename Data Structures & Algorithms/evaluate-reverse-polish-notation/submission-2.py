class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                a = self.stack.pop()
                b = self.stack.pop()
                if i == "+":
                    result = a+b
                elif i == "-":
                    result = b-a
                elif i == "*":
                    result = a*b
                else:
                    result = int(b/a)
                self.stack.append(result)    
            else:
                self.stack.append(int(i))
        return self.stack[-1]                            
        