class Solution:
    def canFinish(self, n, prerequisites):
        graph = [[] for _ in range(n)]
        in_degree=[0]*n

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
            in_degree[course]+=1
        
        queue = [course for course, degree in enumerate(in_degree) if degree==0]

        # process courses using topological sort
        for curr_course in queue:
            n-=1
            for dependent_course in graph[curr_course]:
                in_degree[dependent_course]-=1

                if in_degree[dependent_course]==0:
                    queue.append(dependent_course)
        return n==0