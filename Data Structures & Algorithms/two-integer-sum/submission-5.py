class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict = {}
        for i,j in enumerate(nums):
            hash_dict[j] = i
        print(hash_dict)
        for i in range(len(nums)):
            req = target - nums[i]
            print(req)
            if req in hash_dict and i!=hash_dict[req]:
                return [i, hash_dict[req]]

        