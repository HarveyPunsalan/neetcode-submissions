class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_indices = {}

        for current_index, current_number in enumerate(nums):
            needed_number = target - current_number

            if needed_number in number_indices:
                return [number_indices[needed_number], current_index]

            number_indices[current_number] = current_index
        