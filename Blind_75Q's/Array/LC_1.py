class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {} # val: index

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in visited:
                return [visited[diff], i]
            else:
                visited[nums[i]] = i

        
