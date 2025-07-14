class Graphs:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        str_graph = ""
        for key, value in self.adj_list.items():
            str_graph += f"{key} -> {value}\n"
        return str_graph

    def dfs(self):
        ...

    def bfs(self, start, goal=None):
        """"We use QUEUES(fifo) IN BFS,  AND STACK(lifo) FOR DFS, as helping data structures"""""
        visited = set()
        # set of visited nodes
        queue = [(start, [start])]
        # nodes to be processed, with path taken so far
        order = []  # Our result in order, which is traversal order

        while queue:  # while we still have elements to process
            node, path = queue.pop(0)  # get the elements to process in fifo way
            print(f"Exploring room: {node}, Path so far: {path}")

            if node == goal:
                print("\n🎯 Theseus found the Minotaur!")
                return path

            if node not in visited:
                # first add it to the visited nodes
                visited.add(node)
                order.append(node)  # append it to our resulting list

                # Then get all the neighbours of this node, use our available function
                neighbours = self.obtain_members(node)

                # then iterate through them
                for neighbour in neighbours:
                    # means we have a weighted connection not just individual value
                    if isinstance(neighbour, tuple):
                        neighbour = neighbour[0]  # just take the value and leave the weight

                    # if neighbour is not visited, append it to queue
                    if neighbour not in visited:
                        queue.append((neighbour, path + [neighbour]))

        return order

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists!")

    def add_edge(self, from_node, to_node, weighted=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weighted is None:
            self.adj_list[from_node].add(to_node)

            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add((to_node, weighted))

            if not self.directed:
                self.adj_list[to_node].add((from_node, weighted))

    def obtain_members(self, key_node):
        return self.adj_list.get(key_node, set())

    def adj_matrix(self):
        pass


if __name__ == '__main__':
    graphObj = Graphs()
    graphObj.add_edge("A", "B")
    graphObj.add_edge("A", "C")
    graphObj.add_edge("B", "D")
    graphObj.add_edge("C", "D")
    graphObj.add_edge("D", "E")

    print(graphObj)
    traversal = graphObj.bfs("A", goal="E")
    print("Traversal result:", traversal)
