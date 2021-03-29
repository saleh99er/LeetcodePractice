from collections import Counter

"""



"""


# Source: https://leetcode.com/problems/task-scheduler/discuss/1052835/Python-greedy
# 360 ms, faster than 99%
# 14.8 MB, less than 49.54%

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)
        
        taskFreq = Counter(tasks)
        tasksSorted = sorted(taskFreq.items(), key=lambda x: x[1], reverse=True)
        for i, (task, freq) in enumerate(tasksSorted):
            if i == 0:
                maxFreq = freq 
                idleTime = n*(freq-1)
            else:
                idleTime -= min(maxFreq-1, freq)
            if idleTime <= 0:
                break
        return max(len(tasks)+idleTime, len(tasks))