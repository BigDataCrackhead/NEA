import pygame
import Variables as v

OFFBLUE=pygame.Color("#88CCCC")

def highlightGroupLink(w, choice, x, y):
    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(w, OFFBLUE, (0, 10, 160, 20))

    if not choice:
        if x>0 and x< 200:
            if y>600 and y<800:
                pygame.draw.rect(w, OFFBLUE, (0, 600, 200, 200))
    else:
        if x>0 and x<100:
            if y>600 and y<700:
                pygame.draw.rect(w, OFFBLUE, (0, 600, 100, 100))
            if y>700 and y<800:
                pygame.draw.rect(w, OFFBLUE, (0, 700, 100, 100))
        if x>100 and x<200:
            if y>600 and y<700:
                pygame.draw.rect(w, OFFBLUE, (100, 600, 100, 100))
            if y>700 and y<800:
                pygame.draw.rect(w, OFFBLUE, (100, 700, 100, 100))

def highlightGroupEdit(win, group, x, y):
    groupHost=group.getGroupHost()
    groupMembers=group.getGroupMembers()
    
    try:
        temp=groupHost.getXY()
        pygame.draw.rect(win, v.REALORANGE, (temp[0]-4, temp[1]-4, temp[2]+8, temp[3]+8))

        for member in groupMembers:
            temp=member.getXY()
            pygame.draw.rect(win, v.GREEN, (temp[0]-4, temp[1]-4, temp[2]+8, temp[3]+8))
    except:
        pass

    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 160, 20))

    if x>0 and x<100:
        if y>600 and y<700:
            pygame.draw.rect(win, OFFBLUE, (0, 600, 100, 100))
        if y>700 and y<800:
            pygame.draw.rect(win, OFFBLUE, (0, 700, 100, 100))
    if x>100 and x<200:
        if y>600 and y<700:
            pygame.draw.rect(win, OFFBLUE, (100, 600, 100, 100))
        if y>700 and y<800:
            pygame.draw.rect(win, OFFBLUE, (100, 700, 100, 100))

def highlighterGroupHost(win, x, y, groupHost=None):
    if groupHost:
        temp=groupHost.getXY()
        pygame.draw.rect(win, OFFBLUE, (temp[0]-4, temp[1]-4, temp[2]+8, temp[3]+8))
    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 160, 20))
            return True
    if x>0 and x< 200:
        if y>600 and y<800:
            pygame.draw.rect(win, OFFBLUE, (0, 600, 200, 200))
    return False

def highlighterGroupName(win, x, y):
    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 160, 20))
            return True
    return False
    
def highlighterTime(win, x, y):
    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 160, 20))

    if x>560 and x<640:
        if y>580 and y<620:
            pygame.draw.rect(win, OFFBLUE, (560, 580, 80, 40))

def highlighterEdit(win, x, y, obj):

    if obj.group:
        if x>40 and x<160:
            if y>490 and y<510:
                pygame.draw.rect(win, OFFBLUE, (40, 490, 120, 20))

    if x>0 and x<160:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 160, 20))
    if x>550 and x<650:
        if y>625 and y<675:
            pygame.draw.rect(win, OFFBLUE, (550, 625, 100, 50))
            
def highlighter(win, x, y):
    if x>0 and x<120:
        if y>10 and y<30:
            pygame.draw.rect(win, OFFBLUE, (0, 10, 120, 20))
    if x>1050 and x<1190:
        if y>680 and y<715:
            pygame.draw.rect(win, OFFBLUE, (1050, 680, 140, 35))
        elif y>740 and y<775:
            pygame.draw.rect(win, OFFBLUE, (1050, 740, 140, 35))
    if y>0 and y<30:
        if x>1000 and x<1100:
            pygame.draw.rect(win, OFFBLUE, (1000, 0, 100, 30))
        if x>1100 and x<1200:
            pygame.draw.rect(win, OFFBLUE, (1100, 0, 100, 30))
    if x>0 and x<100:
        if y>600 and y<700:
            pygame.draw.rect(win, OFFBLUE, (0, 600, 100, 100))
        if y>700 and y<800:
            pygame.draw.rect(win, OFFBLUE, (0, 700, 100, 100))
    if x>100 and x<200:
        if y>600 and y<700:
            pygame.draw.rect(win, OFFBLUE, (100, 600, 100, 100))
        if y>700 and y<800:
            pygame.draw.rect(win, OFFBLUE, (100, 700, 100, 100))