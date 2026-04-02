class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a graph problem, where each course is a node, that is connected to all of it's
        # prerequisites (digraph)
        # We only need to track each node's neighbors (prereqs) so we can use a hashmap (int -> list(int))
        # to store the info we need

        # Once we create this graph/map, we need to loop through each node, and check if its possible
        # we know it is possible if it has no prereqs (list is empty) so we DFS through each child
        # and once we know that the child is possible, we can pop it from the list, and continue until
        # the list is empty (we know that since all prereqs are possible, the course is possible)

        # Also for each DFS we need a visit set, to track cycles within the graph
        # In the outer loop, check each node, if it's prereq list is empty, we know it is possible,
        # if not, try DFS and in DFS we check for cycles -> that's when it can return False
        

        # First, lets create our map that stores (int: list(int))
        courseMap = {}
        for i in range(numCourses):
            courseMap[i] = []
        
        
        for prereqPair in prerequisites:
            course, prereq = prereqPair
            courseMap[course].append(prereq)
        # (0: [], 1: [0, 2], 2: [])
        
        # now our DFS function:
        visit = set()
        def dfs(course) -> bool:
            # base cases
            # when a loop exists
            if course in visit:
                return False
            # when the course has no prereqs
            if not courseMap[course]:
                return True
            
            visit.add(course)

            while courseMap[course]:
                prereq = courseMap[course].pop()
                if not dfs(prereq):
                    return False
            
            visit.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        # courseMap = {0: [1], 1: []}
        # visit = {0}




