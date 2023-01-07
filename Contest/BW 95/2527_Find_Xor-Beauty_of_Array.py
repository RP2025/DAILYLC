class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        lst = 0
        for i in range(0,len(nums)):
            lst ^= nums[i]
        return lst
