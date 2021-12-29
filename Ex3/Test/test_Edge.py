from unittest import TestCase

from src.Edge import Edge
from src.Vertex import Vertex



class TestEdge(TestCase):
    e0 = Edge (0,1 ,3)
    e1 = Edge (1, 2, 5)
    e2= Edge (2,0,8)


    def test_get_src(self):
        self.assertEqual(0, self.e0.get_src())
        self.assertEqual(1, self.e1.get_src())
        self.assertEqual(2, self.e2.get_src())

    def test_get_dest(self):
        self.assertEqual(1, self.e0.get_dest())
        self.assertEqual(2, self.e1.get_dest())
        self.assertEqual(0, self.e2.get_dest())

    def test_get_w(self):
        self.assertEqual(3, self.e0.get_w())
        self.assertEqual(5, self.e1.get_w())
        self.assertEqual(8, self.e2.get_w())
