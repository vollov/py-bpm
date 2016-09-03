# -*- coding: utf-8 -*-

class Vertex:
    def __init__(self, name, is_start=False, is_end=False):
        self._name = name
        self.visited = False
        self.is_start = is_start
        self.is_end = is_end
        
    def __str__(self):
        return self.__unicode__(self).encode('utf-8')
    
    def __unicode__(self):
        return "<Vertex('%s')>" % (self.name)
     
class Graph:
    '''represent a directed graph by adjacent list'''
    
    def __init__(self):
        '''use a table to store edges,
        the key is the vertex name, value is vertex list 
        '''
        self._edge_table = {}
        self._vertex_set = set()
        
    def __addVertex(self, vertex):
        self._vertex_set.add(vertex)
    
    def addEdge(self, start_vertex, end_vertex):
        if not self._edge_table.has_key(start_vertex):
            self._edge_table[start_vertex] = []
        self._edge_table[start_vertex].append(end_vertex)
        # populate vertex set
        self.__addVertex(start_vertex)
        self.__addVertex(end_vertex)
        
    def dumpEdges(self):
        '''return list for vertex names by edge for debugging'''
        edge_table = {}
        for key in self._edge_table:
            if not edge_table.has_key(key): 
                edge_table[key._name] = []
            edge_table[key._name] = [v._name for v in self._edge_table[key]]
        return edge_table
    
    def dumpVertexes(self):
        return self._vertex_set
    
    def bfs_path(self, start, end):
        '''Breadth-First-Search'''