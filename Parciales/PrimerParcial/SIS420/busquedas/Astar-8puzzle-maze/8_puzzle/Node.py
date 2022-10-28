import copy

class Node:
    def __init__(self,data,goal=0):
        self.parent = 0
        self.data = data
        self.stat = ""
        self.cost = 0
        self.level = 0
        self.goal = goal
    

    def up(self,index_xr,index_xc,parent):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr+1][index_xc]
        c_data[index_xr+1][index_xc] = "x"
        a = Node(c_data,self.goal)
        a.stat = "UP"
        a.level = self.level + 1
        a.cost = a.h(self.goal)+ a.level
        a.parent = parent
        a.goal = self.goal
        return a

    def right(self,index_xr,index_xc,parent):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr][index_xc-1]
        c_data[index_xr][index_xc-1] = "x"
        a = Node(c_data,self.goal)
        a.stat = "right"
        a.level = self.level + 1
        a.cost = a.h(self.goal)+ a.level
        a.parent = parent
        a.goal = self.goal
        return a

    def down(self,index_xr,index_xc,parent):
        c_data = copy.deepcopy(self.data)
        c_data[index_xr][index_xc] = c_data[index_xr-1][index_xc]
        c_data[index_xr-1][index_xc] = "x"
        a = Node(c_data,self.goal)
        a.stat = "down"
        a.level = self.level + 1
        a.cost = a.h(self.goal) + a.level
        a.parent = parent
        a.goal = self.goal
        return a

    def left(self,index_xr,index_xc,parent):
        w_data = copy.deepcopy(self.data)
        w_data[index_xr][index_xc] = w_data[index_xr][index_xc+1]
        w_data[index_xr][index_xc+1] = "x"
        e = Node(w_data,self.goal)
        e.stat = "left"
        e.level = self.level + 1
        e.cost = e.h(self.goal)+ e.level
        e.parent = parent
        e.goal = self.goal
        return e

    def get_parent(self):
        return str(str(self.parent) + self.stat)


    def Gen_node(self,parent):   
        if self.data[0][0] == 'x':
            return [self.up(0,0,parent),self.left(0,0,parent)]
        elif self.data[0][1] == 'x':
            return [self.up(0,1,parent),self.left(0,1,parent),self.right(0,1,parent)]
        elif self.data[0][2] == 'x':
            return [self.up(0,2,parent),self.right(0,2,parent)]
        elif self.data[1][0] == 'x':
            return [self.up(1,0,parent),self.left(1,0,parent),self.down(1,0,parent)]
        elif self.data[1][1] == 'x':
            return [self.up(1,1,parent),self.right(1,1,parent),self.down(1,1,parent),self.left(1,1,parent)]
        elif self.data[1][2] == 'x':
            return [self.up(1,2,parent),self.right(1,2,parent),self.down(1,2,parent)]
        elif self.data[2][0] == 'x':
            return [self.down(2,0,parent),self.left(2,0,parent)]
        elif self.data[2][1] == 'x':
            return [self.down(2,1,parent),self.left(2,1,parent),self.right(2,1,parent)]
        elif self.data[2][2] == 'x':
            return [self.down(2,2,parent),self.right(2,2,parent)]
        return None

    def h(self,goal):
        h = 0
        for i in range(len(self.data)) :
            for j in range(len(self.data)) :
                if self.data[i][j] != goal[i][j] and self.data[i][j] != 'x':
                    h+=1
        return h

    def __lt__(self, nxt):
        return self.cost < nxt.cost
