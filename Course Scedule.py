from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    # Step 1: Build graph and calculate indegrees
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for dest, src in prerequisites:
        graph[src].append(dest)
        indegree[dest] += 1
    
    # Step 2: Initialize queue with courses having no prerequisites (indegree = 0)
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    processed_courses = 0
    
    # Step 3: Perform topological sort (Kahn's Algorithm)
    while queue:
        course = queue.popleft()
        processed_courses += 1
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 4: Check if all courses were processed
    return processed_courses == numCourses

