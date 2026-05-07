class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=nz=0
        while z<len(nums):
            if nums[z]!=0:
                nums[z],nums[nz]=nums[nz],nums[z]
                nz+=1
            z+=1
        return nums