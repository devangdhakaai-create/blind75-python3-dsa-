class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        f = sum(i * nums[i] for i in range(1,n)) # F(0) calculate karo → har index × value
        max_f = f

        for k in range(1,n):
#har rotation pe F ki value:
# + total → har element ka index +1 hota hai
# - n * nums[n-k] → last element front pe aata hai → index 0 ho jata hai
            f = f + total - n * nums[n-k]
            max_f = max(max_f,f)

        return max_f