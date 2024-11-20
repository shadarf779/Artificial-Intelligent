def createGraph(graph):
    n = int(input("please enter the number of nodes of the graph: "))
    for i in range(n):
        node = input("enter nodes and connected nodes in the following format \n node:neighbor1, neighbor2,...").split(":")
        graph[node[0]] = node[1].split(',') if node[1] else []
    return graph

def dfs(graph, start, dest):
    result = ["Not reachable", list()]
    visited = list()
    queue = list()
    queue.append(start)
    while queue:
        currentNode = queue.pop()
        if currentNode not in graph.keys():
            continue

        if currentNode not in visited:
            visited.append(currentNode)
        if currentNode == dest:
            result[0] = "Reachable"
            break
        for node in graph[currentNode]:
            if node not in graph.keys():
                continue
            queue.append(node)
 
    result[1] = visited
    return result

# Main execution starts here
if __name__ == "__main__":
    graph = dict()
    graph = createGraph(graph)
    start = input("Please input the initial state: ")
    goal = input("Please determine the goal state: ")
    result = dfs(graph, start, goal)
    print("Result = ", result[0])
    print("The path is ", result[1])
