class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            index_j = 0
            for j in nums: 
                index_k = 0
                for k in nums: 
                    if j+k == target and (j != k or index_k != index_j):
                        return [index_j, index_k]
                    index_k += 1
                index_j +=1
