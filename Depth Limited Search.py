def createGraph(graph):
    n = int(input("please enter the number of nodes of the graph"))
    for i in range(n):
        node = input("enter nodes and connected nodes in the following format \n node:neighbor1, neighbor2,...").split(":")
        graph[node[0]] = node[1].split(',')
    return graph

def dfs(graph, start, dest,dl):
    result = ["Not reachable", list()]
    visited = list()
    queue = list()
    queue.append(start)
    counter = 0
    while queue:
        currentNode = queue.pop()
        print(counter)
        counter = counter + 1
        if currentNode not in graph.keys():
            continue

        if currentNode not in visited:
            visited.append(currentNode)
        if currentNode == dest:
            result[0] = "Reachable"
            break
        if  (graph[currentNode] == ['']):
            counter -= 2
        if counter <= dl:
            for node in graph[currentNode]:
                if node not in graph.keys():
                    continue
                queue.append(node)
        else:
            counter -= 1
 
    result[1] = visited
    return result

graph = dict()
graph = createGraph(graph)
start = input("Please input the initial state:")
goal = input("Please determine the goal state")
dl = int(input("Please enter the depth limit"))
result = dfs(graph, start, goal,dl)
print("Result = ", result[0])
print("The path is ", result[1])
