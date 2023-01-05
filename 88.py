class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        abc = [11]
        
        
        
        
        """
        
        for i in nums2:
            nums1.remove(0)
            nums1.append(i)
        print(nums1.sort())
        
        
------------APPROACH 2 --------------
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[0:]
        nums1.sort()
