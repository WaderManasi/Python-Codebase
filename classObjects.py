#This is a function problem. 
#You don't need to take any input. 
#Complete the class functions getName and getHp; and also complete the function fusion.
#The fusion function takes two objects and returns a third object that has following properties:
#name = first-half of obj1 name+ last-half of obj2 name.
#hp = hp of obj1+hp of obj2

class Character:
    def __init__(self,name,hp):
        self.name=name ##Assigning name to the current object's name variable
        self.hp=hp ##Assigning hp to the current object's hp variable
    def boost(self,amount):
        self.hp=self.hp*amount ## boosting current object's hp
    def getName(self):
        return self.name
    def getHp(self):
        return self.hp


def fusion(a,b):
    l1 = int(len(a.name)/2)
    l2 = int(len(b.name)/2)
    h = a.hp + b.hp
    s = a.name[:l1] + b.name[l2:]
    o = Character(s,h)
    return o

def show(a): ##Already completed
    print(a.getName(),a.getHp()) ##printing the newobject's name and hp


def main():
    t=int(input())
    while(t>0):
        name1=input()
        hp1=int(input())
        boost1=int(input())

        name2=input()
        hp2=int(input())
        boost2=int(input())

        chara1=Character(name1,hp1)
        chara1.boost(boost1)

        chara2=Character(name2,hp2)
        chara2.boost(boost2)

        show(fusion(chara1,chara2))

        t-=1
if  __name__=='main':
    main()