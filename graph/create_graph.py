class Graph:

    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list.keys():
            self.adj_list[v] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            edges = self.adj_list[vertex]
            for edge in edges:
                self.adj_list[edge].remove(vertex)
            self.adj_list.pop(vertex)
            return True
        return False


    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")


graph = Graph()

print("----add vertex----")
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
print("----print-----")
graph.print_graph()
print("------add edge--------")
graph.add_edge(1,2)
graph.add_edge(2,3)
graph.add_edge(1,3)
print("------print-----")
graph.print_graph()