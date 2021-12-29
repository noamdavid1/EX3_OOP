from unittest import TestCase

from src.Vertex import Vertex


class TestVertex(TestCase):
    v1 = Vertex(0, (2,4,0))
    v2 = Vertex(1, (5, 9, 0))
    v3 = Vertex(2, (1, 3, 0))


    def test_get_id(self):
        self.assertEqual(0, self.v1.get_id())
        self.assertEqual(1, self.v2.get_id())
        self.assertEqual(2, self.v3.get_id())

    def test_get_pos(self):
        self.assertEqual((2,4,0), self.v1.get_pos())
        self.assertEqual((5, 9, 0), self.v2.get_pos())
        self.assertEqual((1,3,0), self.v3.get_pos())
