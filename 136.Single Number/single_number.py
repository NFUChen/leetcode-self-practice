class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                unique.remove(num)
        
        return list(unique).pop()
            