class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q=deque([0])
        visit=set()
        visit.add(0)

        while q:
            room=q.popleft()
            for k in rooms[room]:
                if k in visit:
                    continue
                
                q.append(k)
                visit.add(k)

        return len(visit)==len(rooms)

        