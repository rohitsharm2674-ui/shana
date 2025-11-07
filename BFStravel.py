
# Name:- Piyush Arun Khandekar
# Div:-  SE-A
# Roll no :- 52





from collections import deque


location = ['A', 'B', 'C', 'D']
location_index = {name: idx for idx, name in enumerate(location)}


adj_matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]


def DFS_matrix(start):
    visited = [False] * len(location)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(location[node])
        for neighbour in range(len(adj_matrix)):
            if adj_matrix[node][neighbour] == 1 and not visited[neighbour]:
                dfs(neighbour)

    dfs(location_index[start])
    return result


def BFS_list(adj_list, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in adj_list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return result


adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def menu():
    while True:
        print("======menu=====")
        print("1. BFS")
        print("2. DFS")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            start = input("Enter starting node for BFS: ").strip().upper()
            if start not in adj_list:
                print(f"Node {start} does not exist in the graph.")
            else:
                s = BFS_list(adj_list, start)
                print("BFS traversal:", s)

        elif choice == '2':
            start = input("Enter starting node for DFS: ").strip().upper()
            if start not in location_index:
                print(f"Node {start} does not exist in the graph.")
            else:
                s = DFS_matrix(start)
                print("DFS traversal:", s)

        elif choice == '3':
            print("Exit")
            break

        else:
            print("Invalid choice.")

menu()

