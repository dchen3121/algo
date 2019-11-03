class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0, i1, i2 = 0, 0, len(nums) - 1
        
        count = 0
        while count <= i2:
            if nums[count] == 0:
                nums[i0], nums[count] = nums[count], nums[i0]
                i0 += 1
                count += 1
            elif nums[count] == 2:
                nums[i2], nums[count] = nums[count], nums[i2]
                i2 -= 1
            else:
                count += 1
                

# Difficulty: medium
# Key points:
# Just coming up with an algorithm. One pass constant space through array        
