class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        array=[]
        prevChar=s[0]
        count=0
        i=0
        while i<len(s):
            # print(array,i,prevChar,count)
            if s[i]==prevChar:
                count+=1
                i+=1
            else:
                if count%k==0:
                    if array:
                        prevChar,count=array.pop()
                    else:
                        prevChar,count=s[i],0
                else:
                    array.append([prevChar,count%k])
                    prevChar=s[i]
                    count=1
                    i+=1
        if count%k!=0:
            array.append([prevChar,count])
        ans=""
        for char,count in array:
            ans=ans+(char*count)
        return ans
        