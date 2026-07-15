import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse = True)
            n1 = stones[0]
            n2 = stones[1]
            result = abs(n2-n1)
            stones.remove(n1)
            stones.remove(n2)
            stones.append(result)
        return stones[0]    



1,7,3,1
3,1,6,
2,6
4

