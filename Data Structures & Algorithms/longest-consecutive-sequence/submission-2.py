class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert org list to set
        numSet = set(nums) #remove duplicates, O(1) search 
        longest = 0
        for n in numSet: 
            if(n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

                