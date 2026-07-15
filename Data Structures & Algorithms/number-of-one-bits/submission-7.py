class Solution:
    def hammingWeight(self, n: int) -> int:
        t = bin(n)
        count = 0
        for i in t:
            if i == "1":
                count +=1
        return count        
        