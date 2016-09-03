# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
from flow.graph import Graph, Vertex

class GraphUt(unittest.TestCase):
    '''complex query test driver for user DAO'''
    def setUp(self):
        self._digraph = Graph()
        a = Vertex('A', is_start=True)
        g = Vertex('G', is_end=True)
        self._digraph.addEdge(a, Vertex('B'))
        self._digraph.addEdge(Vertex('B'), g)
        self._digraph.addEdge(a, Vertex('C'))
        self._digraph.addEdge(Vertex('C'), Vertex('D'))
        
        self._digraph.addEdge(Vertex('D'), Vertex('E'))
        self._digraph.addEdge(Vertex('D'), Vertex('F'))
        self._digraph.addEdge(Vertex('E'), Vertex('D'))
        self._digraph.addEdge(Vertex('F'), g)
        
    def test_dumpEdges(self):
#         expected = {'E': ['A', 'B'], 'D': ['A'], 'G': ['D', 'E'], 'F': ['C'], 'I': ['J'], 'H': ['G', 'F'], 'J': ['A', 'B']}
        print 'dumpEdges()=>', self._digraph.dumpEdges()
#         self.assertEquals(self._digraph.dumpEdges(), expected, 'failed')
        
    def test_dumpVertexes(self):
        expected = set(['A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'J'])
        print 'dumpVertexes()=>', self._digraph.dumpVertexes()
#         self.assertEquals(self._digraph.dumpVertexes(), expected, 'failed')