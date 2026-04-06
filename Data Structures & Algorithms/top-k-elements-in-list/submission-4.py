class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the freq
        freq = defaultdict(int)
        for n in nums:
            freq[n] = freq[n] + 1

        
        #create the buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in freq.items():
            buckets[c].append(n)

        #create the res list
        res= []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n) 
                if len(res) == k: 
                    return res
