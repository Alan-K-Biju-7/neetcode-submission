
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
       
        nums = [item for row in matrix for item in row]
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False                
        