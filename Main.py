import random
from operator import add
import time
class Display:
    def __init__(self,Width,Height):
        pass



class MazeGen:
    def __init__(self,Width,Height):
        self.Board={}
        self.Width=Width
        self.Height=Height
        for X in range(Height):
            for Y in range(Width):
                self.Board[(Y,X)]={"Parent":(-1,-1),"Created":False}
        
           
    def GetCandidates(self):
        Directions=[(0,1),(0,-1),(1,0),(-1,0)]
        Candidates=[]
        for X in Directions:
            Pos=tuple(map(add,self.AgentPosition,X))
            if Pos[0] >= 0 and Pos[0] < self.Width and Pos[1] >= 0 and Pos[1] < self.Height:
                if self.Board[Pos]["Created"] == False:
                    Candidates.append(Pos)
        return Candidates
    
    def RunMazeGenerator(self,Visiulize=False,ShowEnd=False):
        StartingPos=(random.randint(0,self.Width - 1),random.randint(0,self.Height - 1))
        self.Board[StartingPos]["Created"]=True
        self.AgentPosition=StartingPos
        #print(self.AgentPosition)
        while True:
            
            Candidates=self.GetCandidates()
            #print(Candidates)
            if len(Candidates) == 0:
                if self.AgentPosition == StartingPos:
                    #print(self.Board)
                    if ShowEnd:
                        self.PrintBoard()
                    return self.Board
                self.AgentPosition=self.Board[self.AgentPosition]["Parent"]
            else:
                
                Direction=random.choice(Candidates)
                self.Board[Direction]["Parent"]=self.AgentPosition
                self.Board[Direction]["Created"]=True
                self.AgentPosition=Direction
                if self.AgentPosition != StartingPos and random.randint(0,100) < 7:
                    self.AgentPosition=self.Board[self.AgentPosition]["Parent"]
            if Visiulize:
                self.PrintBoard(ShowAgent=True)
                time.sleep(0.2)
    def Debug(self):
        Out=[["⬜" for X in range(self.Width)] for X in range(self.Height)]
        for X,A in self.Board.items():
            Item=""
            if A["Created"]:
                Item="🟩"
            else:
                Item="🟥"
            Out[X[1]][X[0]]=Item

        for X in range(len(Out)):
            Out[X]="".join(Out[X]) + "\n"

        Out="".join(Out)
        print(Out)

    def GetDirection(self,Pos1,Pos2):
        return (Pos2[0] - Pos1[0], Pos2[1] - Pos1[1])
    def PrintBoard(self,ShowAgent=False):
        Out=[["⬛" for X in range((self.Width * 2) + 1)] for X in range((self.Height * 2) + 1)]
        for X,A in self.Board.items():
            if A["Created"]:
                ModPos=((X[0] * 2) + 1,(X[1] * 2) + 1)
                Out[ModPos[1]][ModPos[0]]="⬜"
                if A["Parent"] == (-1,-1):
                    continue
                ModParentConnection=self.GetDirection(X,A["Parent"])
                Out[ModPos[1] + ModParentConnection[1]][ModPos[0] + ModParentConnection[0]]="⬜"

        if ShowAgent:
            Out[(self.AgentPosition[1] * 2) + 1][(self.AgentPosition[0] * 2) + 1]="🟩"
        for X in range(len(Out)):
            Out[X]="".join(Out[X]) + "\n"

        Out="".join(Out)
        print(Out)



            
                
                
           # exit()  
                

#



if __name__ == "__main__":
    while True:
        MG=MazeGen(17,17)
        MG.RunMazeGenerator(Visiulize=True,ShowEnd=True)
        time.sleep(5)