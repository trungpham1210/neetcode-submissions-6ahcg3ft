class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        # for every string
        for s in strs: 
            # add the string to its anagram
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())
                