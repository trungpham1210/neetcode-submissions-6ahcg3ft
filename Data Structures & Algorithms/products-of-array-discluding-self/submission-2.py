class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Init pref, suff, and res
        n = len(nums)
        res = [0] * n
        pref = [1] * n
        suf = [1] * n

        #cal prefix up to the current element
        for i in range(1, n):
            #prefix[curr] = prefix[curr - 1] * nums[curr]
            pref[i] = pref[i - 1] * nums[i-1]
        #cal suffix up to the current element
        for i in range(n - 2, -1, -1):
            #suffix[curr] = suffix[curr + 1] * nums[curr + 1]
            suf[i] = suf[i + 1] * nums[i + 1]

        #calculate the res by multiply pref and suf
        for i in range(n):
            res[i] = pref[i] * suf[i]

        return res