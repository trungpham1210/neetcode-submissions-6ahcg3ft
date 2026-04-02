class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initialize the res array to be all 1s and have the same length as nums

        prefix = 1
        for i in range(len(nums)): #loop through nums and store the prefix to res
            res[i] = prefix
            prefix *= nums[i] #update the prefix as we go, it will be equal to the curr prefix multiply by the number in nums at that index
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #loop backward by 1 and stop by -1 because we want to include index 0
            res[i] *= postfix #since the res already has the values from the prefix, we simply multiply the current res with the postfix to overwrite it
            postfix *= nums[i] #update the postfix as we go, same way we did with the prefix
        return res 
            
