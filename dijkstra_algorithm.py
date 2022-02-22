# Implementation of Dijkstra's Algorithm
# search algorithm that solves the single-source shortest path problem
# for a graph with non-negative edge path costs, producing a shortest path tree

# Conditions for implementing Dijkstra's Algorithm
# 1. Both directed and undirected graphs
# 2. Edges with non-negative weights
# 3. Connected Graph
import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        # making sure the graph is symmetrical
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node,False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def value(self, node1, node2):
        # returning the value of an edge between 2 nodes
        return self.graph[node1][node2]

    def get_outgoing_edges(self, node):
        # returning the neighbours of a node
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # storing the cost of visiting each node in a dict and updating every time we move along the graph
    shortest_path = {}

    # storing the shortest known path to a node found so far
    previous_nodes = {}

    # setting the max size to initialize infinity for the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    # starting node's value is set to 0
    shortest_path[start_node] = 0

    # continuing algorithm until all nodes are visited
    while unvisited_nodes:
        # keeping track of the lowest cost for every node
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # retriving the current node's neighbours and updating the distance
        neighbours = graph.get_outgoing_edges(current_min_node)
        for neighbour in neighbours:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbour)
            if tentative_value < shortest_path[neighbour]:
                shortest_path[neighbour] = tentative_value

                # updating the best path to current node
                previous_nodes[neighbour] = current_min_node
        # after visiting all its neighbours, marking that node as 'visited'
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        # adding the start node
        path.append(start_node)

        print(" Single Source Shortest Path with minimum cost : {}." .format(shortest_path[target_node]))
        print('->'. join(reversed(path)))

if __name__ == '__main__':
    nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

    init_graph = {}
    for node in nodes:
        init_graph[node] = {}

    init_graph["Reykjavik"]["Oslo"] = 5
    init_graph["Reykjavik"]["London"] = 4
    init_graph["Oslo"]["Berlin"] = 1
    init_graph["Oslo"]["Moscow"] = 3
    init_graph["Moscow"]["Belgrade"] = 5
    init_graph["Moscow"]["Athens"] = 4
    init_graph["Athens"]["Belgrade"] = 1
    init_graph["Rome"]["Berlin"] = 2
    init_graph["Rome"]["Athens"] = 2

    graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Reykjavik")
    print_result(previous_nodes, shortest_path, start_node="Reykjavik", target_node="Belgrade")
