import pygame

def clickHandle(w, x, y, l):
    pass

def checkMove(w, x, y, l):
    for i in l:
        if i.checkWithin(x, y):
            i.move(x, y, w)
            return i
    return False

def checkWithin(x, y, x1, y1, width, height):
    if x>x1 and x<x1+width:
        if y>y1 and y<y1+height:
            return True
    return False

def rotate(obj, itemList):
    for temp in obj.conns:
        obj.delConnection(temp, itemList)
    obj.pygameImgID=pygame.transform.rotate(obj.pygameImgID, 90)
    obj.width, obj.height=obj.height, obj.width

    print(len(obj.conns))
    
    obj.rotation+=90
    if obj.rotation==450:
        obj.rotation=90