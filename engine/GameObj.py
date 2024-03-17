class ChrObj(object):
    def __init__(self,x,y,c):
        self.display_c = c
        self.rx,self.ry = x,y
    
class Entity(object):
    def __init__(self, mass_x, mass_y) -> None:
        self.mass_x = mass_x
        self.mass_y = mass_y
        self.objs = []
        pass
    def Display(self) -> None:
        for i in self.objs :
            print(f"\033{self.mass_x+i.rx};{self.mass_y+i.ry}H]{i.display_c}",end="")
    