class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count the occurences of each element in nums 
        freq = defaultdict(int)
        #for every element in num
        for n in nums:
            freq[n] = freq[n] + 1
        #convert hashmap to list 
        l = list(freq.items())
        l.sort(key = lambda x: x[1])
        return [x[0] for x in l[-k: ]]