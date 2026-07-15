class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '{' or  i == '['  or i == '(':
                stack.append(i)
            elif len(stack) == 0:
                return False    
            elif i == '}' or i == ']' or i == ')':
                x = stack.pop()
                if i == '}' and not x == '{':
                    return False
                elif i == ']' and not x == '[':
                    return False
                elif i == ')' and not x == '(':
                    return False  
        if len(stack) == 0:
            return True
        else:
            return False            
                  
                     
                     


        