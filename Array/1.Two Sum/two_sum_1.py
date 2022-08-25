class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx in range(len(nums)):
            current_num = nums[idx]
            diff = target - current_num
            seen[current_num] = idx
            if diff in seen:
                return [seen[diff], idx]