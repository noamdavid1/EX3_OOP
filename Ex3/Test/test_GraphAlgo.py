from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        graph = DiGraph()
        for i in range(7):
            graph.add_node(i)
        graph.add_edge(0, 1, 2.3)
        graph.add_edge(0, 3, 3.1)
        graph.add_edge(1, 2, 1.9)
        graph.add_edge(2, 3, 5.2)
        graph.add_edge(2, 6, 8.4)
        graph.add_edge(3, 0, 2.0)
        graph.add_edge(3, 6, 5.4)
        graph.add_edge(4, 3, 2.7)
        graph.add_edge(4, 5, 3.6)
        graph.add_edge(5, 4, 4.8)
        graph_algo = GraphAlgo(graph)
        self.assertEqual(graph, graph_algo.get_graph())

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        g = DiGraph()
        graph = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 5)
        self.assertEqual((5, [0, 1]), graph.shortest_path(0, 1))

    def test_tsp(self):
        graph= DiGraph()
        graph.add_node(0, (1, 1, 1))
        graph.add_node(1, (2, 2, 2))
        graph.add_node(2, (3, 3, 3))
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 0, 10)
        ag = GraphAlgo(graph)
        lst = [0, 1, 2]
        self.assertEqual(ag.TSP(lst), ([0, 1, 2], 4))

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()