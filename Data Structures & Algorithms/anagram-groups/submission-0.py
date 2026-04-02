class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list) #instead of using {} this makes res[tuple(count)] =[] instead of having to initialize it.
        for s in strs:
            count = [0] * 26 # from a to z there are a total of 26 characters
            for c in s:
                count[ord(c) - ord('a')] +=1 # get the ascii value of the character and increment to count the number of times we encounter in the count
            res[tuple(count)].append(s) #count is converted to a tuple because lists cannot be a dict key but tuples can
        return list(res.values())
