class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for digit in digits:
             num = num * 10 + digit
        num +=  1
        lis = []
        while num:
            digit = num % 10
            lis.append(digit)
            num = num // 10
        lis.reverse()      
        return lis

        


