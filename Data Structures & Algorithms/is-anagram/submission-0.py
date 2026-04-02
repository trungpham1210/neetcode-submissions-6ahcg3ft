class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def char_freq(s):
            freq = {}
            for char in s:
                freq[char] = freq.get(char,0) + 1
            return freq
        return char_freq(s) == char_freq(t)