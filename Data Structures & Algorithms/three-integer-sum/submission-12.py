class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res= []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # this is used because if a > 0, the sum will never be 0 against since the numbers will be all positives
            if i > 0 and a == nums[i-1]:#starting from the second index, if the number is equal to the previous number, skip!
                continue
            l, r = i+1, len(nums) - 1 #the left pointer start at i + 1, because i is the index for a
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while r>l and nums[r] == nums[r-1]:
                        r -=1
        return res