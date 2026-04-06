class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [-1] * 128
        l = 0
        r = 0
        result = 0
        while r < len(s):
            ch = ord(s[r])
            if arr[ch] >= l:
                l = arr[ch] + 1
            arr[ch] = r
            result = max(result, r - l + 1)
            r+=1
        return result