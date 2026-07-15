class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water  = 0
        water_flow = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                water_flow = heights[left] * (right-left)
                left += 1
            else:
                water_flow = heights[right] * (right-left)
                right -= 1
                    

            max_water = max(max_water,water_flow)    
        return max_water    

        