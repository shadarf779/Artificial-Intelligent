def createGraph(graph):
    n = int(input("please enter the number of nodes of the graph: "))
    for i in range(n):
        node = input("enter nodes and connected nodes in the following format \n node:neighbor1, neighbor2,...").split(":")
        graph[node[0]] = node[1].split(',') if node[1] else ['']  # Handle nodes without children
    return graph

def ids(graph, start, dest, dl):

    for depth in range(1, dl):  
        print(f"depth limit: {depth}")
        result = depth_limited_search(graph, start, dest, depth)
        if result[0] == "Reachable":
            return result
    return ["Not reachable", []]

def depth_limited_search(graph, start, dest, dl):

    result = ["Not reachable", list()]
    visited = list()
    queue = list()
    queue.append((start, 0))  

    while queue:
        currentNode, currentDepth = queue.pop()
        print(f"Current Node: {currentNode}, Current Depth: {currentDepth}, Depth Limit: {dl}")

        if currentDepth > dl:  
            continue

        if currentNode not in visited:
            visited.append(currentNode)

        if currentNode == dest:
            result[0] = "Reachable"
            result[1] = visited
            return result

        if graph[currentNode] == ['']: 
            continue

        for node in graph[currentNode]:
            if node not in graph.keys():
                continue
            queue.append((node, currentDepth + 1))

    result[1] = visited
    return result

graph = dict()
graph = createGraph(graph)
start = input("Please input the initial state: ")
goal = input("Please determine the goal state: ")
dl = int(input("Please determine the maximum depth limit: "))
result = ids(graph, start, goal, dl)
print("\nResult = ", result[0])
print("The path is ", result[1])
