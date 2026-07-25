class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        number_map = {}

        for right, num in enumerate(numbers):
            if (target - num) in number_map:
                return [number_map[target-num], right+1]

            number_map[num] = right+1