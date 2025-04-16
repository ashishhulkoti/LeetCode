class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys=set()
        visited=set()
        norooms=len(rooms)
        keys.add(0)
        currq=[0]
        nextq=[]

        while currq:
            r = currq.pop(0)
            if r in visited:
                pass
            else:
                nextq.extend(rooms[r])
                visited.add(r)
                keys.add(r)
                if len(keys) == norooms:
                    return True
            
            if not currq:
                currq = nextq
                nextq=[]
        return False
        

        
            
