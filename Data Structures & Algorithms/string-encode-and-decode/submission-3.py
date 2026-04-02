class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s)) + "#" + s #the length of s will be first, but have to convert to str to add to res, then the delimiter, and then the string
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i #add the second pointer to help with looping through the string
            while s[j] != "#":
                j += 1 #increment j until it reach the delimiter
            length = int(s[i:j]) #here s[0:1] will return the 0 index, but it will be a str type so we have to convert it into int because this represent length
            res.append(s[j + 1 : j + 1 + length]) # here, we append the string, so from j+1 because j is at the delimiter and after it is the word, to j+length+1, because we have to get the whole word
            i = j + 1 + length # reset the i position so it can move to the next word
        return res
        