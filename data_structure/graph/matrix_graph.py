"""图 基于邻接矩阵存储"""


class Graph(object):
    def __init__(self, Matrix):
        vnum = len(Matrix)
        for x in Matrix:
            if len(x) != vnum:
                raise ValueError('False')
        self.Mat = [Matrix[i][:] for i in range(vnum)]
        self.Vnum = vnum
        self.edgenum = 0
        for i in range(self.Vnum):
            for j in range(self.Vnum):
                if self.Mat[i][j] != 0:
                    self.edgenum += 1

    def get_edgenum(self):
        return self.edgenum

    def get_Vnum(self):
        return self.Vnum

    def IsExist(self, v):
        return v < 0 or v >= self.Vnum

    def add_edge(self, vi, vj, val=1):
        if self.IsExist(vi) or self.IsExist(vj):
            raise ValueError('False')
        self.Mat[vi][vj] = val

    def out_edges(self, v):
        if self.IsExist(v):
            return False
        m = len(self.Mat[v])
        res = []
        for i in range(m):
            if self.Mat[v][i] != 0:
                res.append((v, i, self.Mat[v][i]))
        return res


if __name__ == '__main__':
    a = [[0, 1, 0, 1, 0],
         [1, 0, 1, 0, 0],
         [1, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 0, 0]]
    graph = Graph(a)
    print(graph.get_Vnum())
    graph.add_edge(0, 2)
    print(graph.out_edges(0))
    print(graph.get_edgenum())
