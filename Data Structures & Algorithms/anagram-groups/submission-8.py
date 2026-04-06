class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hashmap to store anagram using defaultdict
        anagrams = defaultdict(list)

        #for every element in strs, sorted and append the same sorted string to the list
        for s in strs:
            #we have to lock the list once we sorted it
            #list can change so we have to use tuple
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())

        
                