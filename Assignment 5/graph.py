from queue_array import *
from stack_array import *


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False
        self.colored = None


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.vertex_dict = {}
        self.vertex_list = []
        file = open(filename, 'r')
        for line in file:
            vertices = line.split()
            for vertex in vertices:
                self.add_vertex(vertex)
            self.add_edge(vertices[0], vertices[1])
        file.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        if self.vertex_dict.get(key) is None:
            vertex = Vertex(key)
            self.vertex_dict[key] = vertex
            self.vertex_list.append(key)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        return self.vertex_dict.get(key)

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        self.vertex_dict[v1].adjacent_to.append(v2)
        self.vertex_dict[v2].adjacent_to.append(v1)

    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        return sorted(self.vertex_list)

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        connected = []

        all_visited = False
        index = 0
        while not all_visited:
            stack = Stack(len(self.vertex_list))
            connections = []
            found = False
            while not found:
                if index == len(self.vertex_list):
                    return connected
                elif self.vertex_dict[self.vertex_list[index]].visited is False:
                    stack.push(self.vertex_list[index])
                    self.vertex_dict[self.vertex_list[index]].visited = True
                    found = True
                else:
                    index += 1
            while not stack.is_empty():
                vertex = stack.pop()
                connections.append(vertex)
                for node in self.vertex_dict[vertex].adjacent_to:
                    if self.vertex_dict[node].visited is False:
                        stack.push(node)
                        self.vertex_dict[node].visited = True
            connected.append(sorted(connections))
            connected = sorted(connected, key=lambda x: x[0])

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        index = 0
        bipartite = True
        while bipartite:
            queue = Queue(len(self.vertex_list))
            found = False
            while not found:
                if index == len(self.vertex_list):
                    return True
                elif self.vertex_dict[self.vertex_list[index]].colored is None:
                    queue.enqueue(self.vertex_list[index])
                    self.vertex_dict[self.vertex_list[index]].colored = "Green"
                    found = True
                else:
                    index += 1
            color = "Green"
            opposite_color = "Red"
            while not queue.is_empty():
                vertex = queue.dequeue()
                color = self.vertex_dict[vertex].colored
                if color == "Green":
                    opposite_color = "Red"
                else:
                    opposite_color = "Green"

                for adj in self.vertex_dict[vertex].adjacent_to:
                    if self.vertex_dict[adj].colored == color:
                        return False
                    elif self.vertex_dict[adj].colored is None:
                        self.vertex_dict[adj].colored = opposite_color
                        queue.enqueue(adj)
                color, opposite_color = opposite_color, color
