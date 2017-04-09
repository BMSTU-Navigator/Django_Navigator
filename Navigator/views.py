from django.shortcuts import render
from Navigator.clases import *
from Navigator.models import *
# Create your views here.
"""получить код поинта по его нзвнию
    нужно обвесить эксепшеном

"""
#remake
def get_id(string):
    return (Point.get(Point.name==string)).id
#remake
def get_instance_path_by_id(id):
    tmp= (Area.get(Area.id == id)).picture_path
    return tmp
#remake
def get_floor_by_id(id):
    return Area.get(Area.id == id)
#remake
def get_dialog_item(id,style):
    if style==1: return Dialogs.get(Dialogs.id == id).style1
    if style==2: return Dialogs.get(Dialogs.id == id).style2
    if style==3: return Dialogs.get(Dialogs.id == id).style3

#remake
def get_building()->Building:
    building = Building()
    building.graph=get_graph()
    building.floors=Area.select()
    return building


#remake
def get_graph()->Graph:
    graph=Graph()
    graph.connections=GraphConnection.select()
    graph.points=Point.select()
    graph.points_dict={}
    for point in graph.points:
        graph.points_dict[point.id]=point
    return graph