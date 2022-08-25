class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []
            anagram_map[sorted_word].append(word)
        
        return [
            anagrams for anagrams in anagram_map.values()
        ]