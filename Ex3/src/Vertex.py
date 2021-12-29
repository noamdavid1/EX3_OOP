

class Vertex:


    def __init__(self,key:int,pos:tuple = None):
        self.__id = key
        self.w = 0
        self.tag = 0
        self.info = ""
        self.pos = pos

    def get_id(self) -> int:
        return self.__id

    def get_pos(self) -> tuple:
        return self.pos


    def __gt__(self, other):
        other: Vertex =other
        return other.w<self.w

    def __repr__(self) -> str:
        return "id: %s w: %s"%(self.__id,self.w)


if __name__ == '__main__':
    n: Vertex=Vertex(1,(1,1))
    print(n.get_id())