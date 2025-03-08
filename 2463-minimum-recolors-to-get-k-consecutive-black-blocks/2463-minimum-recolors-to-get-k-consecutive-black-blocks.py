class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r=0,k
        w=0
        b=0
        minR=float("inf")
        for i in range(k):
            if blocks[i]=="W":
                w+=1
            else:
                b+=1
        
        while r<len(blocks):
            if w<minR:
                minR=w
            if blocks[l]=="W":
                w-=1
            else:
                b-=1
            if blocks[r]=="W":
                w+=1
            else:
                b+=1
            l+=1
            r+=1
        if w<minR:
            return w
        return minR
        