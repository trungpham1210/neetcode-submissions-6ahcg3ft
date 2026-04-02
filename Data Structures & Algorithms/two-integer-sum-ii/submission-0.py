class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) -1 #create two pointers
        while l<r:
            curSum = numbers[l] + numbers[r] #get the current sum of the pointers
            if curSum > target: 
                r -=1 # if the current sum is larger than the target, decrement the right pointer
            elif curSum < target:
                l+=1 #if the current sum is smaller than the target, increment the left pointer
            else:
                return [l+1, r+1] #if the current sum is equal to the target, return the index of the pointer, but since it is based 1, we have to add an additional index to the current index
        return []