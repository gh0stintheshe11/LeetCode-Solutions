class Robot:

    def __init__(self, width: int, height: int):
        self.dir="East"
        self.cor=[0,0]
        self.arr=[width-1,height-1]
        self.width=width
        self.height=height

    def step(self, num: int) -> None:
        total=((self.height+self.width-2)*2)
        num=num%total
        if num!=0:
           i=0
           while i<num:
                if self.dir=="East":
                    if self.cor[0]==self.width-1:
                        num+=1
                        self.dir="North"
                    else:self.cor[0]+=1

                elif self.dir=="West":
                    if self.cor[0]==0:
                        num+=1
                        self.dir="South"
                    else:self.cor[0]-=1
                elif self.dir=="North":
                    if self.cor[1]==self.height-1:
                        num+=1
                        self.dir="West"
                    else:self.cor[1]+=1
                elif self.dir=="South":
                    if self.cor[1]==0:
                        num+=1
                        self.dir="East"
                    else:self.cor[1]-=1
                i+=1      
        elif self.cor==[0,0]  and self.dir=="East":self.dir="South"
      
    def getPos(self) -> List[int]:
        return self.cor

    def getDir(self) -> str:
        return self.dir