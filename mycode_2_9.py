# link: https://github.com/Taarzogfd/aima-python/blob/master/mycode_2_9.py

from mycode_2_8 import *


class myVacCleaner:
    def decide(self, location, perception):
        # each entry in perception is a list consists of a tuple and a string.
        # the tuple is a coordinate
        # valid values for the string: 'Clean', 'Dirty'
        dirtyEntries=[]
        cleanEntries=[]
        for entry in perception:
            if (entry[0]==location and entry[1]=='Dirty'):
                return 'Suck'
            if entry[1]=='Dirty':
                dirtyEntries.append(entry[0])
            elif entry[1]=='Clean':
                cleanEntries.append(entry[0])
            else:
                print('** Cleanness value invalid! **')
                print('** Location:'+str(entry[0])+' Value:'+str(entry[1]))
                raise RuntimeError('See Console for details')


        cleanEntries.remove(location)
        if dirtyEntries!=[]:
            target=random.choice(dirtyEntries)
        else:
            target=random.choice(cleanEntries)

        xMove=target[0]-location[0]
        yMove=target[1]-location[1]

        if (xMove==1 and yMove==0):
            return 'Right'

        if (xMove==-1 and yMove==0):
            return 'Left'

        if (xMove==0 and yMove==1):
            return 'Up'

        if (xMove==0 and yMove==-1):
            return 'Down'

        print('** WARNING: invalid xMove or yMove:'+str(xMove)+','+str(yMove)+' **')
        raise RuntimeError('See Console for details')


def genDirtyCleanList(decimal, max):
    returnVal=[]
    for i in range(max):
        if (decimal%2):
            returnVal.append('Dirty')
        else:
            returnVal.append('Clean')
        decimal //= 2
    return returnVal


if __name__=='__main__':
    widthMain=int(input('Input width:'))
    heightMain=int(input('Input height:'))
    steps_taken=30 # Total steps
    totalTests=0
    if (widthMain<=0 or heightMain<=0):
        print('** WARNING: WIDTH AND HEIGHT MUST BE POSITIVE INTEGERS **')
        raise RuntimeError('See Console for details')

    inst_Env=myVacEnv(width=widthMain,height=heightMain)
    inst_Cleaner=myVacCleaner()

    totalEntries=widthMain*heightMain

    for i in range(2**totalEntries):
        DCList=genDirtyCleanList(i,totalEntries)
        
        for agentStartPointNum in range(totalEntries):
            agentInitLocationMain=[agentStartPointNum%widthMain,agentStartPointNum//widthMain]
            
            #initialize
            inst_Env.agentLocation=agentInitLocationMain
            inst_Env.score=0

            DCpointer=0
            for i in range(heightMain):
                for j in range(widthMain):
                    inst_Env.cleanness[i][j]=DCList[DCpointer]
                    DCpointer+=1
            
            ### test output
            print('------------ TEST ROUND BEGINS -----------')
            totalTests+=1
            print('Will take %d steps' % steps_taken)
            print('INITIAL: ')
            print('Agent: '+str(agentInitLocationMain))
            print('Cleanness:')
            print(inst_Env.cleanness)

            for i in range(steps_taken):
                inst_Env.execute_action(inst_Cleaner)
                

            print('\n\n\nFINAL SCORE: '+str(inst_Env.score))
            print('------------- TEST ROUND ENDS ------------\n\n')

print('++++++++ ALL TEST ROUNDS FINISHED SUCCESSFULLY ++++++++')
print('Width: %d, Height: %d, Steps: %d' % (widthMain,heightMain,steps_taken))
print('Total test rounds: %d' % (totalTests))