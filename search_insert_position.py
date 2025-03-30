class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for n in range(len(nums)):
            if target < nums[n]:
                return index
            elif target == nums[n]:
                break
            index += 1
        return index
