class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        def get_count_map(nums):
            count_map = {}
            for num in nums:
                if num not in count_map:
                    count_map[num] = 0
                count_map[num] += 1
            return count_map
        
        counts_arr = [
            [] for _ in range(len(nums) + 1)
        ]
        
        count_map = get_count_map(nums)
        
        for num, count in count_map.items():
            counts_arr[count].append(num)
        
        top_k = []
        for idx in range(len(counts_arr) - 1, -1, -1):
            for num in counts_arr[idx]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k
                