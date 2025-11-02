class Solution:
    def maxDepth(self, s: str) -> int:
        max_len=0
        count=0
        for i in s:
            if i=="(":
                count+=1
            elif i==")":
                count-=1
            if count>max_len:
                max_len=count
        return max_len
