import pickle, pygame
import listenToHarry as classy
import Draw as d
import Click as c

def packUpGroup(groupList):
    bigListy=[]

    for group in groupList:
        listy=[[], [], [], []]
        listy[0]=group.groupName
        listy[1]=group.groupHost.id
        listy[2]=[]
        listy[3]=[[], [], [], []]

        for i in group.groupMembers:
            listy[2].append(i.id)
        
        tempIndex=0
        for i in group.direction:
            listy[3][tempIndex]=[]
            for x in i:
                listy[3][tempIndex].append(x.id)
            tempIndex+=1

        bigListy.append(listy)

    return bigListy

def unpackGroup(data, l):
    listy=[]
    print()
    print("List to Pull From", l)
    for group in data:
        print("Looping Through Data:", group)
        temp=classy.Group(group[0])

        for obj in l:
            if obj.id == group[1]:
                temp.setGroupHost(obj)
            if obj.id in group[2]:
                temp.addMember(obj)
            for index in range(4):
                if obj.id in group[3][index]:
                    temp.addDirection(obj, index)
        print("Attributes of Group:", temp, temp.groupHost, temp.groupMembers)
        print()
        listy.append(temp)
    return listy

def pack(l, num, time, toPackGroupList):
    print("================")
    print("Packing")
    print("================")

    listy=[[],[],[]]#defines empty list which will contain the board

    length=len(l)
    for x in range (length, 0, -1):#Loops through the objects
        menu=l[x-1]
        if menu.checkInside(0, 600, 200, 800):#Removes objects that are generated for the menu
            l.remove(menu)
            classy.Object.counterStorage.append(menu.id)

    listy[0].append(time)
    for i in l:
        temp=i.packUpObj()
        listy[1].append(temp)
    listy[2]=packUpGroup(toPackGroupList)

    if num==0:
        with open('./Saves/spareSave.pickle', 'wb') as handle:
            pickle.dump(listy, handle, protocol=pickle.HIGHEST_PROTOCOL)
    elif num==1:
        with open('./Saves/saveOne.pickle', 'wb') as handle:
            pickle.dump(listy, handle, protocol=pickle.HIGHEST_PROTOCOL)
    elif num==2:
        with open('./Saves/saveTwo.pickle', 'wb') as handle:
            pickle.dump(listy, handle, protocol=pickle.HIGHEST_PROTOCOL)

def unpack(num):
    print("================")
    print("Unpacking")
    print("================")

    if num==0:
        with open('./Saves/spareSave.pickle', 'rb') as handle:
            temp = pickle.load(handle)
    elif num==1:
        with open('./Saves/saveOne.pickle', 'rb') as handle:
            temp = pickle.load(handle)
    elif num==2:
        with open('./Saves/saveTwo.pickle', 'rb') as handle:
            temp = pickle.load(handle)

    listy=[]
    time=temp[0][0]
    for i in temp[1]:
        if i[4]=="RD":
            newObject=classy.Road(i[0], i[1])
        elif i[4]=="TL":
            newObject=classy.TrafficLight(i[0], i[1])
        elif i[4]=="4J":
            newObject=classy.FourJunction(i[0], i[1]) 
        elif i[4]=="TJ":
            newObject=classy.TJunction(i[0], i[1])
        elif i[4]=="TN":
            newObject=classy.Turn(i[0], i[1])
        
        newObject.setSpecial(i[5])
        newObject.setId(i[6])

        while i[3]!=newObject.rotation:
            c.rotate(newObject, [])
            newObject.defineGeometry()

        newObject.conns=i[2]
        
        updateInstance=newObject
        listy.append(newObject)
    
    
    newGroupList=unpackGroup(temp[2], listy)
    if not newGroupList:
        newGroupList=[]
    else:
        for group in newGroupList:
            group.infectGroup()

    try:
        updateInstance.updateGlobal(listy)
    except:
        pass
    
    print()
    print("Printing Unpacked Values")
    print("Printing Group List:", newGroupList)
    print("Printing Item List:", listy)
    print("Printing Time:", time)
    print()
    
    return listy, time, newGroupList