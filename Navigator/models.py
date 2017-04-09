from django.db import models
from Navigator.clases import *



"""поинт - место на карте (кабинет, лвход на лестницу итд)"""
class Point(models.Model):

    name = models.CharField(verbose_name='name', max_length=255, default="")                 #имя
    #floor_index = models.ForeignKey(Area,null=True)        #индекс инстанса в котором находится точка
    path_for_point_pic = models.CharField(verbose_name='path_for_point_pic', max_length=255, default="")     #путь к картинке
    x = models.IntegerField(verbose_name='x', default=0)                   #координата х на карте инстанса
    y = models.IntegerField(verbose_name='y', default=0)                  #координата у на карте инстанса



""" этаж
    в близжайшем буду щем станет
    инстансом
    ИНСТАНС - фрагмент местности внутри здания (кусок циркуля, часть этажа)
    """
class Area(models.Model):
    picture_path = models.CharField(verbose_name='picture_path', max_length=255, default="")    #
    #floor_index = IntegerField() # ошибка



class GraphConnection(models.Model):
    point1 = models.ForeignKey(Point,null=True,related_name='point1')            # указатель на поинт 1
    point2 = models.ForeignKey(Point,null=True,related_name='point2')                 #указатель на поит 2
    connection_weight = models.IntegerField(verbose_name='connection_weight', default=0)      # вес соедиения
    connection_comment = models.CharField(verbose_name='connection_comment', max_length=255, default="")         # коментарий соединения
    picture_path = models.CharField(verbose_name='picture_path', max_length=255, default="")               # путь к картинке соединения
    floor_index = models.ForeignKey(Area, null=True)           # указатель на инстанс если соединение внутри одного инстанса
    trans_floor_marker = models.BooleanField(verbose_name='trans_floor_marker', default=False)     # маркер того что поинты входящие в соединение находятся в разных инстансах

""" таблица диалогов с тремя стилями
1й стиль - официальный
2й стиль - средний
3й стиль - не официал

например реплика с ключом 0
1й стиль - здравствуйте
2й стиль - привет
3й стиль - здарова братуха
"""
class Dialogs(models.Model):      #
    style1=models.CharField(verbose_name='style1', max_length=255, default="")       #
    style2=models.CharField(verbose_name='style2', max_length=255, default="")       #
    style3=models.CharField(verbose_name='style3', max_length=255, default="")       #



