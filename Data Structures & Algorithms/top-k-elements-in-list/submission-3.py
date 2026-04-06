class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the freq list to count the occurences
        freq = defaultdict(int)

        for n in nums: 
            freq[n] = freq[n] + 1

        # create the buckets

        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in (freq.items()): 
            freq_buckets[c].append(n)
        
        #create the result list
        res = []
        for i in range(len(freq_buckets) - 1, 0 , -1):
            for n in freq_buckets[i]: 
                res.append(n) 
                if len(res) == k:
                    return res
