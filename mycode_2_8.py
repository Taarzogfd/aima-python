# link: https://github.com/Taarzogfd/aima-python/blob/master/mycode_2_8.py

from agents import *


# The environment has one agent in it.
# The agent's decision process is triggered by function decide(),
# and the agent returns its result in:
# 'Suck', 'Up', 'Down', 'Left', 'Right'.

class myVacEnv(XYEnvironment):
    def __init__(self, width=2, height=1, agentInitialLocation=[0, 0]):
        super().__init__(width, height)
        self.cleanness=[]  # Dirty places need to be initialized manually
        self.score=1000  # Default: 1000
        self.agentLocation=agentInitialLocation  # Location: [x,y] width is x, and height is y
        self.agent=None  # must be initialized

        # Initialize: every place is clean
        for i in range(self.height):
            self.cleanness.append([])
            for j in range(self.width):
                self.cleanness[i].append('Clean')

    def things_near(self, location, radius=1):
        # location must be a tuple with exactly 2 elements.
        radiusSq=radius*radius
        returnVal=[]
        for i in range(self.height):
            for j in range(self.width):
                if distance_squared(location, (j, i))<=radiusSq:
                    returnVal.append([[j, i], self.cleanness[i][j]])
        return returnVal

    def percept(self, location):
        return self.things_near(location)

    def agentSucks(self):
        x, y=self.agentLocation
        if self.cleanness[y][x]=='Dirty':
            print('The agent has cleaned a dirty place:'+str(x)+","+str(y))
            self.cleanness[y][x]='Clean'
            self.score+=100
        elif self.cleanness[y][x]=='Clean':
            print('This place is already clean:'+str(x)+","+str(y))
            self.score-=100
        else:
            print('** WARNING: cleaness invalid at '+str(self.agentLocation)+' **')
            raise RuntimeError('See Console for details')

    def agentMoves(self, action):
        if action=="Suck":
            print('Agent starts cleaning!')
            self.agentSucks()
            return

        # self.score-=5 #reserved for penalty on move

        if action=='Left':
            if self.agentLocation[0]==0:
                print("The agent is at leftmost.")
            else:
                self.agentLocation[0]-=1
                print("The agent moved one step leftward. "+str(self.agentLocation))
            return

        if action=='Right':
            if self.agentLocation[0]==self.width-1:
                print("The agent is at rightmost.")
            else:
                self.agentLocation[0]+=1
                print("The agent moved one step rightward. "+str(self.agentLocation))
            return

        if action=='Up':
            if self.agentLocation[1]==self.height-1:
                print("The agent is at uppermost.")
            else:
                self.agentLocation[1]+=1
                print("The agent moved one step upward. "+str(self.agentLocation))
            return

        if action=='Down':
            if self.agentLocation[1]==0:
                print("The agent is at bottom.")
            else:
                self.agentLocation[1]-=1
                print("The agent moved one step downward. "+str(self.agentLocation))
            return

        # default
        print("** WARNING: The agent returned an incorrect message ** "+str(self.agentLocation))
        raise RuntimeError('See Console for details')

    def execute_action(self, agent):
        if agent==None:
            print('** WARNING: AGENT NOT DEFINED **')
            raise RuntimeError('See Console for details')

        agentPerception=self.percept(self.agentLocation)
        agentDecision=agent.decide(self.agentLocation,agentPerception)
        self.agentMoves(agentDecision)
