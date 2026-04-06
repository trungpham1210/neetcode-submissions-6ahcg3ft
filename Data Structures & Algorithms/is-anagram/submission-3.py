class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #count the occurences of each char in s
        freqS = defaultdict(int) #using defaultdict because we need a default of 0 for the occurences of the char
            #increment by one for each char
        for char in s:
            freqS[char] = freqS[char] + 1 

        #count the occurences of each char in t
        freqT = defaultdict(int)
            #increment by one for each char
        for char in t:
            freqT[char] = freqT[char] + 1        
        #compare the two freq list and return   
        return freqS == freqT