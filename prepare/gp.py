from enum import enum

class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2



class Node:
    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}
        self.adj_weights = {}

    def __resr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):

        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)

        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, src_key, dst_key, weight=0):
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)            

