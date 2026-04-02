class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #here, we put the defaultdict because we need a default value for the res[tuple(count)] so it won't be running into problems even if we dont initialize it
        for s in strs:
            count = [0] * 26 # count will be maximum of 26 because we only have 26 character from a to z
            for c in s:
                count[ord(c) - ord('a')] +=1 #count the number of freq of each character by getting its ascii values
            res[tuple(count)].append(s) #count is converted to tuple because lists cant be used as the key of the dict but tuples can
        return list(res.values())