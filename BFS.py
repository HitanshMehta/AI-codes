def bfs(graph, start):
    visited = []
    queue = []

    if start not in visited:
        visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            queue.append(neighbor)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

graph = {}
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter the start node: ")
visited_nodes = bfs(graph, start_node)

print("\nVisited Nodes:")
for node, edges in graph.items():
    if node in visited_nodes:
        print(node, "was visited")
    else:
        print(node, "was not visited")

print("\nOrder of visitation was:", " ".join(visited_nodes))
