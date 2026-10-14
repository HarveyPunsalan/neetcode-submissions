class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            res[i] = left    # store product of everything to the left
            left *= nums[i]  # then include nums[i] for the next index

        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right     # multiply in product of everything to the right
            right *= nums[i]

        return res
        