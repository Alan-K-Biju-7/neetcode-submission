class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        
       
        while n != 1 and  n not in seen:
            result = 0
            seen.add(n)
            while n != 0:
               d = n % 10 
               result += d*d
               n = n // 10
            n = result   
        return n == 1       
            