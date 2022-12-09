from enum import Enum  # Python 2 users: Run pip install enum34


class State(Enum):

    unvisited = 0
    visiting = 1
    visited = 2


class Node:

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:

    def __init__(self):
        self.nodes = {}  # Key = key, val = Node

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, src_key, dst_key, weight=0):
        if src_key is None or dst_key is None:
            raise TypeError('key cannot be None')
        self.add_edge(src_key, dst_key, weight)
        self.add_edge(dst_key, src_key, weight)
        
        
        
       import unittest


class TestGraph(unittest.TestCase):

    def create_graph(self):
        graph = Graph()
        for key in range(0, 6):
            graph.add_node(key)
        return graph

    def test_graph(self):
        graph = self.create_graph()
        graph.add_edge(0, 1, weight=5)
        graph.add_edge(0, 5, weight=2)
        graph.add_edge(1, 2, weight=3)
        graph.add_edge(2, 3, weight=4)
        graph.add_edge(3, 4, weight=5)
        graph.add_edge(3, 5, weight=6)
        graph.add_edge(4, 0, weight=7)
        graph.add_edge(5, 4, weight=8)
        graph.add_edge(5, 2, weight=9)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[3].key], 4)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[4].key], 5)
        self.assertEqual(graph.nodes[3].adj_weights[graph.nodes[5].key], 6)
        self.assertEqual(graph.nodes[4].adj_weights[graph.nodes[0].key], 7)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[4].key], 8)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[2].key], 9)

        self.assertEqual(graph.nodes[0].incoming_edges, 1)
        self.assertEqual(graph.nodes[1].incoming_edges, 1)
        self.assertEqual(graph.nodes[2].incoming_edges, 2)
        self.assertEqual(graph.nodes[3].incoming_edges, 1)
        self.assertEqual(graph.nodes[4].incoming_edges, 2)
        self.assertEqual(graph.nodes[5].incoming_edges, 2)

        graph.nodes[0].remove_neighbor(graph.nodes[1])
        self.assertEqual(graph.nodes[1].incoming_edges, 0)
        graph.nodes[3].remove_neighbor(graph.nodes[4])
        self.assertEqual(graph.nodes[4].incoming_edges, 1)

        self.assertEqual(graph.nodes[0] < graph.nodes[1], True)

        print('Success: test_graph')

    def test_graph_undirected(self):
        graph = self.create_graph()
        graph.add_undirected_edge(0, 1, weight=5)
        graph.add_undirected_edge(0, 5, weight=2)
        graph.add_undirected_edge(1, 2, weight=3)

        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[1].key], 5)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[0].key], 5)
        self.assertEqual(graph.nodes[0].adj_weights[graph.nodes[5].key], 2)
        self.assertEqual(graph.nodes[5].adj_weights[graph.nodes[0].key], 2)
        self.assertEqual(graph.nodes[1].adj_weights[graph.nodes[2].key], 3)
        self.assertEqual(graph.nodes[2].adj_weights[graph.nodes[1].key], 3)

        print('Success: test_graph_undirected')


def main():
    test = TestGraph()
    test.test_graph()
    test.test_graph_undirected()


if __name__ == '__main__':
    main() 
