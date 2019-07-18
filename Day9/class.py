from abc import ABCMeta,abstractmethod

class Creep(object):

    __slots__=('_hp','_attack')

    def __init__(self,hp):
        self._hp=hp

    @abstractmethod
    def attack(self):
        pass

    #@property
    def get_hp(self):
        return self._hp
    

class Hero(Creep):

    __slots__=('_hp','_mp')

    def __init__(self,hp,mp):
        super().__init__(hp)
        self._mp=mp

    #@property
    def get_mp(self):
        return self._mp

    @abstractmethod
    def get_skill_mp(self):
        pass

    @abstractmethod
    def get_skill_damage(self):
        pass
    
    def skill(self):
        if self.get_mp()>=self.get_skill_mp():
            self._mp-=self.get_skill_mp()
            return self.get_skill_damage()
        else :
            return self.attack()

class HouYi(Hero):
    
    def __init__(self,hp,mp):
        super().__init__(hp,mp)
    
    def attack(self):
        return 80
    
    def get_skill_damage(self):
        return 140

    def get_skill_mp(self):
        return 20
    
    def __str__(self):
        return "---HouYi---\nHp:%d\nMp:%d"%(self._hp,self._mp)

def main():
    hy=HouYi(300,100)
    print(hy.attack())
    print(hy.skill())
    print(hy.skill())
    print(hy.skill())
    print(hy.skill())
    print(hy)
    print(hy.skill())
    print(hy.skill())    

if __name__ == "__main__":
    main()