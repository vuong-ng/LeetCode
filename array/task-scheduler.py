class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ### redo 1
        timeTask = Counter(tasks)
        timeTask = [-t for t in timeTask.values()]
        heapq.heapify(timeTask)
        queue = []
        curT = 0

        while timeTask or queue:
            curT += 1
            if timeTask:
                task = heapq.heappop(timeTask)
                if task+1:
                    queue.append((task+1, curT+n))
            
            if queue and curT == queue[0][1]:
                freq, time = queue.pop(0)
                # freq = freq + 1
                if freq: 
                    heapq.heappush(timeTask, freq)

        return curT












        # timesTask = Counter(tasks)
        # timesTask = [-t for t in timesTask.values()]
        # heapq.heapify(timesTask)
        # queue = collections.deque()
        # curTime = 0
        # while len(timesTask) != 0 or len(queue) != 0:
        #     curTime +=1 
        #     if timesTask:
        #         item = heapq.heappop(timesTask)
        #         if item+1:
        #             queue.append((item+1, curTime+n))
        #     if queue and queue[0][1] == curTime:
        #             task = queue.popleft()[0]
        #             #task += 1 
        #             if task != 0:
        #                 heapq.heappush(timesTask, task)
        # return curTime








