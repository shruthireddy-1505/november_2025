class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        res=0
        n=len(s)
        i=0
        while i<n:
            if i!=n-1:
                ch1=s[i]
                ch2=s[i+1]
                if d[ch1]<d[ch2]:
                    temp=d[ch2]-d[ch1]
                    res+=temp
                    i+=2
                else:
                    res+=d[ch1]
                    i+=1
            else:
                ch3=s[i]
                res+=d[ch3]
                i+=1
        return res