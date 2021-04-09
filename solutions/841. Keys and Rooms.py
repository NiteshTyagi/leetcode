class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        size = len(rooms)
        visited_room = [False for room in range(size)]
        stack =[0]
        visited_room[0]=True
        while stack:
            ele = stack.pop()
            for adj in rooms[ele]:
                if not visited_room[adj]:
                    stack.append(adj)
                    visited_room[adj]=True
        return all(visited_room)
        
