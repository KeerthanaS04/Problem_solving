from typing import List
from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for course, prerequisite in prerequisites:
            graph[course].append(course)
            in_degree[course]+=1
        
        result = []
        queue = deque([course for course, degree in enumerate(in_degree) if degree==0])

        while queue:
            curr_course = queue.popleft()
            result.append(curr_course)

            # for each course that depends on the curr course
            for dependent_course in graph[curr_course]:
                in_degree[dependent_course]-=1
                if in_degree[dependent_course]==0:
                    queue.append(dependent_course)
        return result if len(result)==numCourses else []