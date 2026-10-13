class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counts = {}

        for number in nums:
            frequency_counts[number] = frequency_counts.get(number, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for number, frequency in frequency_counts.items():
            buckets[frequency].append(number)

        top_numbers = []

        for frequency in range(len(nums), 0, -1):
            for number in buckets[frequency]:
                top_numbers.append(number)

                if len(top_numbers) == k:
                    return top_numbers
        