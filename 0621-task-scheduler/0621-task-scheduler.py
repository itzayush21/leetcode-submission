class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        '''count=Counter(tasks)
        maxheap=[-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        s=deque()
        t=0
        while maxheap or s:
            t+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt:
                    s.append([cnt,t+n])
                if s and s[0][1]==t:
                    heapq.heappush(maxheap,s.popleft()[0])
        return t'''
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_tasks_count = sum(freq == max_freq for freq in task_counts.values())
        idle_time = (max_freq - 1) * (n + 1)
        min_length = idle_time + max_freq_tasks_count
        return max(len(tasks), min_length)