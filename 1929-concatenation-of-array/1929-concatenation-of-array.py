class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)*2
        ans=[0]*n
        for i in range(len(ans)):
            if i<len(nums):
                ans[i]=nums[i]
            else:
                temp=i-len(nums)
                ans[i]=nums[temp]
        return ans        