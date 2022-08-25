class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [
            1  for _ in range(len(nums))
                 ]
        postfix = [
            1 for _ in range(len(nums))
                  ]
        
        for idx in range(1, len(prefix)):
            ptr = idx - 1
            prefix[idx] = nums[ptr] * prefix[ptr]
        
        for idx in range(len(postfix) - 2, -1, -1):
            ptr = idx + 1
            postfix[idx] = nums[ptr] * postfix[ptr]
            
        product = []
        for pre, post in zip(prefix, postfix):
            product.append(pre * post)
        return product