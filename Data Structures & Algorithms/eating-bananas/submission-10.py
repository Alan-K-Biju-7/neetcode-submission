import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right
        while left <= right:
            mid = (left +  right) // 2
            total_hrs = 0
            for p in piles:
                total_hrs += math.ceil(float(p) / mid)
            if total_hrs <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result           

            



        