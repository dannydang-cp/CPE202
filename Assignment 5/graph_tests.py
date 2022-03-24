import unittest
from graph import *


class TestList(unittest.TestCase):
    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_add_vertex(self):
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex('v9.1'), None)
        g.add_vertex('v9.1')
        self.assertNotEqual(g.get_vertex('v9.1'), None)
        vertices = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9', 'v9.1']
        self.assertEqual(g.get_vertices(), vertices)
        g.add_vertex('v9.1')
        self.assertEqual(g.get_vertices(), vertices)

    def test_add_edge(self):
        g = Graph('test1.txt')
        self.assertEqual(g.vertex_dict['v6'].adjacent_to, ['v7', 'v8'])
        g.add_edge('v7', 'v6')
        self.assertEqual(g.vertex_dict['v6'].adjacent_to, ['v7', 'v8', 'v7'])


if __name__ == '__main__':
    unittest.main()
