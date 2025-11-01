class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=[]
        for key,value in d.items():
            s.append([key,d[key]])

        sorted_data = sorted(s, key=lambda x: x[1], reverse=True)
        n=len(sorted_data)

        res=""
        for i in range(n):
            temp=sorted_data[i][0]*sorted_data[i][1]
            res+=temp
        return res
            
            