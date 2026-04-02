class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0) # counting the number of times of each numbers in the list
        for n, c in count.items():
            freq[c].append(n) #adding the number to the freq list, the count.items will get the number as a key and the count as the count/freq
        res = []
        for i in range(len(freq) - 1, 0, -1): #loop through the freq with i as index
            for n in freq[i]:#loop through each number in the freq list, the index will be i
                res.append(n) # adding one by one from the back to the front and return if the length of result = k meaning we reach the goal
                if len(res) == k:
                    return res
 