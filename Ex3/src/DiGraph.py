from src.GraphInterface import GraphInterface
from src.Edge import Edge
from src.Vertex import Vertex

from typing import Dict


class DiGraph(GraphInterface):

    def __init__(self):
        self.__vertexs: Dict[int, Vertex] = dict()
        # private HashMap<Integer,NodeData> vertexs=new HashMap<Integer,NodeData>();
        self.__edgesIn: Dict[int, Dict[int, Edge]] = dict()
        self.__edgesOut: Dict[int, Dict[int, Edge]] = dict()
        self.__mc = 0
        self.__countEdge = 0

    def v_size(self) -> int:
        return len(self.__vertexs)

    def e_size(self) -> int:
        return self.__countEdge

    def get_all_v(self) -> dict:
        return self.__vertexs

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.__edgesIn.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.__edgesOut.get(id1)

    def get_mc(self) -> int:
        return self.__mc

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.__vertexs.keys():
            n: Vertex = Vertex(node_id, pos)
            self.__mc+=1
            self.__vertexs.update({node_id: n})
            self.__edgesIn.update({node_id: dict()})
            self.__edgesOut.update({node_id: dict()})
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.__vertexs and id2 in self.__vertexs and (id1 != id2) and id2 not in self.__edgesOut.get(id1):
            self.__countEdge += 1
            self.__mc += 1
            e:Edge = Edge(id1, id2, weight)
            self.__edgesOut.get(id1).update({id2:e})
            self.__edgesIn.get(id2).update({id1:e})
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.__vertexs:
            size_EdgeOut = len(self.all_out_edges_of_node(node_id))
            size_EdgeIn = len(self.all_in_edges_of_node(node_id))
            self.__countEdge -= size_EdgeIn
            self.__countEdge -= size_EdgeOut
            self.__mc += size_EdgeOut + size_EdgeIn
            for id in self.__vertexs.keys():
                if id!=node_id:
                    if node_id in self.__edgesIn.get(id):
                        self.__edgesIn.get(id).pop(node_id)
                    if node_id in self.__edgesOut.get(id):
                        self.__edgesOut.get(id).pop(node_id)
            self.__edgesIn.pop(node_id)
            self.__edgesOut.pop(node_id)
            self.__mc += 1
            self.__vertexs.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 in self.__vertexs and node_id2 in self.__vertexs and (node_id1 != node_id2)):
            self.__countEdge -= 1
            self.__mc += 1
            self.__edgesOut.get(node_id1).pop(node_id2)
            self.__edgesIn.get(node_id2).pop(node_id1)
            return True
        return False

    def __repr__(self):
        return "Graph{ vertexs: %s edgeOut: %s edgeIn: %s VertexsNum: %s EdgeNum: %s Mc: %s }" % (
        self.__vertexs, self.__edgesOut, self.__edgesIn, self.v_size(), self.__countEdge, self.__mc)

if __name__ == '__main__':
    graph: DiGraph = DiGraph()
    graph.add_node(1, (2, 3))
    graph.add_node(2, (2, 3))
    graph.add_node(3, (2, 3))
    graph.add_node(4, (2, 3))
    graph.add_node(5, (2, 3))
    graph.add_edge(1, 2, 50)
    graph.add_edge(1, 3, 50)
    graph.add_edge(4, 1, 50)
    print("******************************************")
    print(graph)
    graph.remove_node(1)
    print("******************************************")
    print(graph)
    # graph:DiGraph = DiGraph()
    # graph.add_node(1,(2,3))
    # graph.add_node(1,(2,3))
    # print("******************************************")
    # print(graph)
    # graph.add_edge(1, 2,50)
    # graph.add_edge(2, 1,50)
    # print("******************************************")
    # print(graph)
    # graph.add_node(2,(5,7))
    # graph.add_edge(2, 1,50)
    # graph.add_edge(1, 2,50)
    # print("******************************************")
    # print(graph)


    # graph.remove_edge(2,8)
    # graph.remove_edge(8,2)
    # graph.remove_edge(8,3)
    # print("******************************************")
    # print(graph)
    # graph.remove_edge(1,2)
    # print("******************************************")
    # print(graph)