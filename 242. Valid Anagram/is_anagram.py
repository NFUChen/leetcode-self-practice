class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for idx in range(len(s)):
            if s[idx] not in s_count:
                s_count[s[idx]] = 0
            s_count[s[idx]] += 1
            
            if t[idx] not in t_count:
                t_count[t[idx]] = 0
            t_count[t[idx]] += 1
            
        for char, count in s_count.items():
            if char not in t_count:
                return False
            
            if t_count[char] != count:
                return False
        
        return True