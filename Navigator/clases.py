class Building:
    graph=None
    floors=None

class Graph:
    connections = []
    points=[]
    points_dict={}

class Path:
    points = []
    connections = []
    floors = []
    floors_obj={}
    weight=-1
    def __init__(self):
        self.points = []
        self.connections = []
        self.floors = []
        self.weight = -1


