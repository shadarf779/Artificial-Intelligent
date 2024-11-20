def CreateGraph(graph):
    n = int(input("please enter number of nodes:"))
    for i in range(n):
        node = input("please enter the node and its childs in the form of node:child1, child2,...")
        l = node.split(':')
        graph[l[0]] = l[1].split(',')
    return graph

def BFS(graph, start, goal):
    result = ['impossible', list()]
    reached = list()
    Frontier = list()
    Frontier.append(start)
    reached.append(start)
    while Frontier:
        currentNode = Frontier.pop(0)
        if currentNode not in graph.keys():
            continue
  
        for node in graph[currentNode]:
            if node not in graph.keys():
                continue
            if node == goal:
                result[0] = 'Possible'
                reached.append(node)
                break 
            if node not in reached:
                reached.append(node)
                Frontier.append(node)
        if result[0] == 'Possible':
            break

    result[1] = reached
    return result

graph = dict()
graph = CreateGraph(graph)
start = input('please enter the start node')
goal  = input('please enter the goal node')
result = BFS(graph, start, goal)
print(result[0])
print(result[1])
