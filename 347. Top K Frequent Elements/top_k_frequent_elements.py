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
            [] for _ in range(len(nums))
        ]
        
        count_map = get_count_map(nums)
        
        for num, count in count_map.items():
            counts_arr[count - 1].append(num)
        
        top_k = []
        for idx in range(len(counts_arr) - 1, -1, -1):
            while(counts_arr[idx] != []):
                top_k.append(counts_arr[idx].pop())
                if len(top_k) == k:
                    return top_k