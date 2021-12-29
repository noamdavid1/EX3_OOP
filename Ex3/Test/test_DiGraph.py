from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):
    def test_v_size(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        graph.add_node(5, (2, 3))
        self.assertEqual(5, graph.v_size())  # add assertion here


    def test_e_size(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        graph.add_edge(4, 1, 50)
        self.assertEqual(3, graph.e_size())  # add assertion here

    def test_get_all_v(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        graph.add_node(5, (2, 3))
        self.assertEqual(5, len(graph.get_all_v()))

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        graph.add_edge(1, 2, 8)
        graph.add_edge(2, 3, 8)
        graph.add_edge(3, 4, 8)
        self.assertEqual(len(graph.all_in_edges_of_node(2).values()), 1)
        graph.remove_node(1)
        self.assertEqual(len(graph.all_in_edges_of_node(2).values()), 0)


    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        graph.add_edge(1, 2, 8)
        graph.add_edge(2, 3, 8)
        graph.add_edge(2, 4, 8)
        graph.add_edge(3, 4, 8)
        self.assertEqual(len(graph.all_out_edges_of_node(2).values()), 2)
        graph.remove_node(3)
        graph.remove_node(4)
        self.assertEqual(len(graph.all_out_edges_of_node(2).values()), 0)

    def test_get_mc(self):
        graph: DiGraph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_node(4, (2, 3))
        self.assertEqual(4, graph.get_mc())  # add assertion here
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        graph.add_edge(4, 1, 50)
        self.assertEqual(7, graph.get_mc())  # add assertion here

    def test_add_node(self):
        graph = DiGraph()
        graph.add_node(0,(1,2))
        graph.add_node(1,(1,2))
        graph.add_node(2,(1,2))
        self.assertEqual(3, graph.get_mc())
        graph.add_node(2)
        self.assertEqual(3, graph.get_mc())
        graph.remove_node(0)
        self.assertEqual(4, graph.get_mc())
        self.assertEqual(False, graph.add_edge(0, 1, 5))
        graph.add_node(0)
        self.assertEqual(True, graph.add_edge(0, 1, 5))
        self.assertEqual(6, graph.get_mc())


    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        self.assertEqual(False, graph.add_edge(1, 2, 50))
        self.assertEqual(True, graph.add_edge(2, 3, 9))

    def test_remove_node(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(2, graph.e_size())
        graph.remove_node(1)
        self.assertEqual(2, graph.v_size())
        self.assertEqual(0, graph.e_size())


    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3))
        graph.add_node(2, (2, 3))
        graph.add_node(3, (2, 3))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(2, graph.e_size())
        graph.remove_edge(1,2)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(1,graph.e_size())
