MOUSE=The mouse
BUTTON=A button
NODELIST=A list of nodes with their values
GAME=True as long as the game is running
CURRENTBONUS=How many units bonus you have left to spend
ALLYLIST=How many allied nodes you have
INPUT=An inputted number from the user (Probably use a slider or smth)
YOURTURN=True when it is your turn

NODE=A class that has variables:
    ally: Either True or False depending on whether it is allied. Default False.
    storedValue: The value in units of that node currently. Default int(0).
    costValue: The value in units required to take that node. If it is zero then it must be allied. Default int(1).
    depth: How far into the board the node is. Default int(0).

SELECTEDNODES=An empty list
FOREIGNNODE=None

while GAME:
    #Your Turn:
    if YOURTURN:

        #Distrobuting Bonus:
        CURRENTBONUS=length(ALLYLIST) #The CURRENTBONUS Will Be The Number Of Allied Nodes You Have
        while CURRENTBONUS: #While CURRENTBONUS>0 Runs
            if MOUSE clicked: #If The Mouse Is Pressed
                for NODE in ALLYLIST: #Loops Through The Nodes In The ALLYLIST
                    if MOUSE over NODE: #If The Mouse Is Hovering Over A Node In ALLYLIST
                        INPUT=How many units from your CURRENTBONUS you want to send to this NODE (From 1->CURRENTBONUS)
                        CURRENTBONUS-=INPUT #Sends Those Units To The Node
                        NODE.storedValue+=INPUT
            
            if MOUSE over BUTTON:
                CURRENTBONUS=0 #If You Don't Want To Use Your Bonus Goes To The Next Part


        #Checking For New Nodes Or Moving Values
        if MOUSE clicked: #If The Mouse Is Pressed
            for NODE in NODELIST: #Loops Through The Available Nodes
                if MOUSE over NODE: #If The Mouse Is Hovering Over A Node In NODELIST
                    if NODE = FOREIGNNODE: #If The Node Has Already Been Selected Then You Deselect It
                        FOREIGNNODE=None
                    else: #If It Hasn't Then You Need To Know Whether A Node Has Been Selected
                        if FOREIGNNODE: #Checks If A Node Has Been Selected
                            if not NODE.ally: #If A Node Has Been Selected And The Node Being Hovered Over
                                            #Is Not An Ally Then Checks If It Can Be Afforded
                                if FOREIGNNODE.storedValue>=NODE.costValue:
                                    FOREIGNNODE.storedValue-=NODE.costValue #If It Can Be Afforded Then The 
                                                                            #Selected Node Becomes An Ally
                                    NODE.ally=True
                                    ALLYLIST.append(NODE)
                                else:
                                    break #If It Cannot Be Afforded Then Throw A "You Cannot Afford This" Message
                            else: #If The Node Is An Ally Then You Want To Send Units To It
                                INPUT=How many units you want to send (From 1->FOREIGNNODE.storedValue)
                                if NODE.depth>FOREIGNNODE.depth: #Checks Whether You Need To Pay To Send Units
                                    FOREIGNNODE.storedValue-=INPUT
                                    NODE.storedValue+=INPUT
                                else:
                                    FOREIGNNODE.storedValue-=INPUT
                                    NODE.storedValue+=INPUT-1        
                        else: #If A Node Hasn't Been Selected Then Makes This Node Selected
                            FOREIGNNODE=NODE
            if MOUSE over BUTTON:
                YOURTURN=False #Ends Your Turn When You Press "End Turn"
