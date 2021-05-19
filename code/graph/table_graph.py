"""图 基于邻接表存储 顺序分配和链式分配相结合"""


class HeadNode(object):
    def __init__(self, adj_vex, data=None):
        self.adj_vex = adj_vex
        self.data = data
        self.next_arc = None


class EdgeNode(object):
    def __init__(self, adj_vex, info=1):
        self.adj_vex = adj_vex
        self.next_arc = None
        self.info = info

    pass


class Graph(object):
    """无向图"""

    def __init__(self, v_num: int):
        self.v_num = v_num
        self.head_node_lis = []
        for i in range(v_num):
            self.head_node_lis.append(HeadNode(i))

        self.visited_1 = list(0 for _ in range(v_num))
        self.visited_2 = list(0 for _ in range(v_num))

    def _add_edge_node(self, i: int, j: int):
        node = self.head_node_lis[i]
        while node.next_arc:
            node = node.next_arc
        node.next_arc = EdgeNode(j)

    def add_edge(self, vi: int, vj: int) -> True or False:
        if vi < 0 or vi >= self.v_num or vj < 0 or vj >= self.v_num:
            return False

        self._add_edge_node(vi, vj)
        self._add_edge_node(vj, vi)
        return True

    def get_info(self, vi: int):
        if vi < 0 or vi >= self.v_num:
            return False
        p = self.head_node_lis[vi]
        res = []
        while p.next_arc:
            p = p.next_arc
            res.append(p.adj_vex)
        return res

    def dfs(self, v: int):
        """图的DFS遍历"""
        self.visited_1[v] = 1
        print(v)
        p = self.head_node_lis[v].next_arc
        while p:
            w = p.adj_vex
            if self.visited_1[w] == 0:
                self.dfs(w)
            p = p.next_arc

    def bfs(self, v: int):
        """图的BFS遍历"""
        # 参考二叉树的层次遍历
        if self.visited_2[v] == 1:
            return

        queue = []  # 存放顶点节点
        p = self.head_node_lis[v]
        queue.append(p)
        self.visited_2[p.adj_vex] = 1

        while queue:
            p = queue.pop(0)
            print(p.adj_vex)  # 出队可以做其他操作

            for adj_vex in self.get_info(p.adj_vex):
                if self.visited_2[adj_vex] == 0:
                    queue.append(self.head_node_lis[adj_vex])
                    self.visited_2[adj_vex] = 1  # 入队即算访问了


if __name__ == '__main__':
    gr = Graph(5)
    gr.add_edge(1, 2)
    gr.add_edge(1, 3)
    gr.add_edge(3, 4)
    gr.add_edge(2, 3)
    gr.add_edge(3, 0)
    gr.add_edge(4, 0)
    print(gr.get_info(3))
    print('****************************')
    gr.dfs(3)
    print('bfs')
    gr.bfs(3)
    print('bfs')
    gr.bfs(2)
    pass
