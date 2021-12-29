

class Edge:

    def __init__(self,src:int,dest:int,w:float):
        self.__src=src
        self.__dest=dest
        self.__w=w
        self.info=""
        self.tag=0


    def get_src(self) -> int:
        return self.__src

    def get_dest(self) -> int:
        return self.__dest

    def get_w(self) -> float:
        return self.__w


    def __repr__(self) -> str:
        return "src: %s dest: %s weight: %s"%(self.__src,self.__dest,self.__w)


if __name__ == '__main__':
    e:Edge=Edge(1,2,500)
    print(e.get_w())
    print(e.get_src())
    print(e.get_dest())
    e.tag=50000
    print(e.tag)
    e.info="petah tikva"
    print(e.info)