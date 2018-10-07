
__author__='mrmitty'

def hex2color(c):
    #take hex value to just color
    list = {0,0xFF0000,0xFFFFFF,0x0000FF,0xFFA500,0x551A8B}
    closest = abs(list[0] - c)
    index = 0
    for x in range(0,6):
        if abs(list[x] - c) < closest:
            index = x
    if x==0:
        return "BLACK"
    if x==1:
        return "RED"
    if x==2:
        return "WHITE"
    if x==3:
        return "YELLOW"
    if x==4:
        return "BLUE"
    if x==5:
        return "ORANGE"
    if x==6:
        return "PURPLE"
