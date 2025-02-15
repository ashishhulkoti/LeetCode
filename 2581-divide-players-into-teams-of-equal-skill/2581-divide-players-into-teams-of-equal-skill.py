class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skill_sum=skill[0]+skill[-1]
        chemistry=skill[0]*skill[-1]
        l,r=1,len(skill)-2
        while l<r:
            if (skill[l]+skill[r])==skill_sum:
                chemistry+=skill[l]*skill[r]
            else:
                return -1
            l+=1
            r-=1
        return chemistry