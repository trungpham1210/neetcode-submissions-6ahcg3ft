class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 #initialize the result
        l, r = 0 , len(heights) - 1
        while l < r:
            area = (r-l) * min(heights[l], heights[r]) #calculate the area
            #res = max(res, area)#update the result based on the max area 
            
            if heights[l] < heights[r]: #if height of left is less than height of right, increment left
                l += 1
            else: #if height of right is less than height of left or equal, increment right
                r-=1
            res = max(res, area)
        return res