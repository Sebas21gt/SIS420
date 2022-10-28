import copy
from scipy.spatial import distance
class Node:

    def __init__(self, x=0, y=0,cost=0,d=0,parent=0,start=0,end=0,world=0):
        self.pos = (x,y)
        self.world = world
        self.pos_x = x
        self.pos_y = y
        self.cost = cost
        self.d = d
        self.parent = parent
        self.start = start
        self.end = end

    def neighbor(self):

        neighbors = []
        if self.pos == (0,0):
            neighbors.append(self.gen_new_node(self.pos_x + 1,self.pos_y,(self.pos_x,self.pos_y)))
            neighbors.append(self.gen_new_node(self.pos_x ,self.pos_y+1,(self.pos_x,self.pos_y)))
            return neighbors

        if self.pos_x - 1 != -1:
            print("1",self.pos_x-1,self.pos_y)   
            neighbors.append(self.gen_new_node(self.pos_x - 1,self.pos_y,(self.pos_x,self.pos_y)))           


        if self.pos_x != self.world.width:
            print("2",self.pos_x+1,self.pos_y)   
            neighbors.append(self.gen_new_node(self.pos_x + 1,self.pos_y,(self.pos_x,self.pos_y)))  


        if self.pos_y - 1 != -1:
            print("3",self.pos_x,self.pos_y-1)         
            neighbors.append(self.gen_new_node(self.pos_x,self.pos_y - 1,(self.pos_x,self.pos_y)))  


        if self.pos_y != self.world.width:
            print("4",self.pos_x,self.pos_y+1)
            neighbors.append(self.gen_new_node(self.pos_x,self.pos_y + 1,(self.pos_x,self.pos_y)))  

            
        return neighbors

    def manhadtan_dis(self,a,b):
        return sum(abs(val1-val2) for val1, val2 in zip(a,b))

    def euclidean(self,a,b):
        return distance.euclidean(a,b)

    def gen_new_node(self,x,y,parent):
        d = self.d + 1
        cost = self.euclidean((x,y),self.end)
        # cost = self.euclidean((x,y),self.end)
        a = copy.deepcopy(self.parent)
        a.append(parent)
        newNode = Node(x,y,cost,d,a,self.start,self.end,self.world)
        return newNode
