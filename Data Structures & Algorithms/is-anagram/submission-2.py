class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        #Count the occurences of character in s using the hashmap
        freqS = defaultdict(int)
        freqT = defaultdict(int)
            
        #for every character in s
        for char in s: 
            #count the occurence of each character
            freqS[char] = freqS[char] + 1
        #for every character in t
        for char in t: 
            #count the occurence of each character
            freqT[char] = freqT[char] + 1
        
        # compare to the occurences of each character in t
        return freqS == freqT