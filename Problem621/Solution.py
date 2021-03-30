import heapq
from collections import deque, Counter
from typing import List

"""

Problem 621: Task Scheduler (Medium)

Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any 
order. Each task is done in one unit of time. For each unit of time, the 
CPU could complete either one task or just be idle. However, there is a 
non-negative integer n that represents the cooldown period between two same
tasks (the same letter in the array), that is that there must be at least n 
units of time between any two same tasks. Return the least number of units 
of times that the CPU will take to finish all the given tasks.

Intuition: a compressed way of modeling the tasks is to track for each
character in the array, what is it's task frequency.

Approach (for below): Best way to execute tasks (with a greedy approach) is
in descending frequency order. Use a heap to push/pop tasks in priority order
then use a queue to store the tasks under cooldown, keep executing tasks for
a corresponding character until that task frequency is set to 0. If no 
elements in the heap then count this cycle as idle time. Each iteration is a
cpu cycle in our algorithm and keep iterating until the heap and queue have
no remaining tasks left. 

(better approach in anotherAltSolution.py that takes advantage of us returning
the count instead of simulating the scheduling algo itself).

let freq of tasks be <= A (some constant)
m := number of tasks (nonunique)
Runtime Complexity: O(mlogm)
Space Complexity: O(m+n)
Runtime: 936 ms, faster than 6.42%
Space: 14.7 MB, less than 70.85%
"""


class Task:
    def __init__(self, task_char, freq):
        self.task_char = task_char
        self.freq = freq

    def decrement_task_freq(self):
        self.freq -= 1
        
    def get_task_freq(self):
        return self.freq

    def __lt__(self, other):
        return self.freq > other.freq


class Solution:
    """
    freq := how many times do we need to execute a certain task (so far)
    get task freq from lin search O(m)
    get highest task freq that isn't within the cooldown period
    decrement task freq for this task, and set cooldown
    move task to cooldown (to pop later)
    pop a task from cooldown queue
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count task frequency
        task_freq_dict = Counter(tasks)

        # Create heap / priority queue for unique tasks
        task_freq_tuple_list = task_freq_dict.most_common()
        task_pqueue = []
        heapq.heapify(task_pqueue)
        for task_freq_tuple in task_freq_tuple_list:
            task = Task(task_freq_tuple[0], task_freq_tuple[1])
            heapq.heappush(task_pqueue,task)

        tasks_in_cooldown = 0
        cooldown = deque([None]*n)
        cpu_cycles = 0

        while(len(task_pqueue) > 0 or tasks_in_cooldown > 0):
            if len(task_pqueue) > 0:
                next_task = heapq.heappop(task_pqueue)
            else:
                next_task = None

            # TODO: refactor conditional below if possible
            if next_task is not None:
                # print(next_task.task_char, " : ", next_task.freq)
                next_task.decrement_task_freq()
                if next_task.get_task_freq() > 0:
                    cooldown.append(next_task)
                    tasks_in_cooldown += 1
                else:
                    cooldown.append(None)
            else:
                # print("idle")
                cooldown.append(None)
                
            ready_task = cooldown.popleft()
            if ready_task is not None:
                tasks_in_cooldown -= 1
                heapq.heappush(task_pqueue, ready_task)

            cpu_cycles += 1

        return cpu_cycles

if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    solver = Solution()
    result = solver.leastInterval(tasks, n)
    print(result)