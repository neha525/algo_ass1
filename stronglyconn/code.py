# scc_finder.py
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack=None, component=None):
        visited[v] = True
        if component is not None:
            component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack, component)
        if stack is not None:
            stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    def kosaraju(self):
        stack = []
        visited = [False] * (self.V + 1)

        # Step 1: Fill stack with finishing times
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Step 2: Transpose graph
        gr = self.transpose()

        # Step 3: Process vertices in order of stack
        visited = [False] * (self.V + 1)
        sccs = []
        while stack:
            i = stack.pop()
            if not visited[i]:
                component = []
                gr.dfs(i, visited, component=component)
                sccs.append(component)
        return sccs

def main():
    g = Graph(5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.add_edge(4, 5)

    sccs = g.kosaraju()

    print("Strongly Connected Components:")
    for comp in sccs:
        print(comp)

    with open("scc_output.txt", "w") as f:
        f.write("Strongly Connected Components:\n")
        for comp in sccs:
            f.write(f"{comp}\n")

if __name__ == "__main__":
    main()