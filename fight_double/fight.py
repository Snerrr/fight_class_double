from shot import Hit
from warrior import Fighter
from random import randint
import text
class Boy():
    def __init__(self):
        self.fighter_1 = Fighter("Conor Mcgregor", 90, 800)
        self.fighter_2 = Fighter("Habib Nurmagomedov", 70, 1000)
        self.hit_1 = Hit("golovoy", 7, 0.2)
        self.hit_2 = Hit("rukoy", 1, 1)
        self.hit_3 = Hit("nogoy", 2, 0.6)

    def random_popadanie_golovoy(self):
        popadanie = randint(1, 10)
        if popadanie > 2:
            return False
        else:
            return True
        
    def random_popadanie_nogoi(self):
        popadanie = randint(1, 10)
        if popadanie > 6:
            return False
        else: 
            return True
        
    def info_boec_1(self):
        return self.fighter_1.get_info()
    
    def info_boec_2(self):
        return self.fighter_2.get_info()
    
    def proverka_boec_1(self):
        if self.fighter_1.get_hp() <= 0:
            return False
        else:
            return True

    def proverka_boec_2(self):
        if self.fighter_2.get_hp() <= 0:
            return False
        else:
            return True

    #-------------------удары моего бойца ->
    
    def zdorovie_1(self):
        hp = self.fighter_2.get_hp()
        if hp > 0:
            return f"{text.hp_opponent} {hp}"
        else :
            return text.no_opponent
    
    def udar_golovoy(self):
        uron = self.fighter_1.get_attack() * self.hit_1.get_krit() * self.random_popadanie_golovoy()
        self.fighter_2.set_hp(self.fighter_2.get_hp() - uron)
        if uron == 0:
            return text.konor_miss
        else:
            return text.konor_strike

    def udar_rukoy(self):
        uron = self.fighter_1.get_attack() * self.hit_2.get_krit()
        self.fighter_2.set_hp(self.fighter_2.get_hp() - uron)
        if uron == 0:
            return text.konor_miss
        else:
            return text.konor_strike
        
    def udar_nogoy(self):
        uron = self.fighter_1.get_attack() * self.hit_3.get_krit() * self.random_popadanie_nogoi()
        self.fighter_2.set_hp(self.fighter_2.get_hp() - uron)
        if uron == 0:
            return text.konor_miss
        else:
            return text.konor_strike

    #----------------------- удары по моему бойцу ->

    def random_vibor(self):
        vibor = randint(1 ,3)
        return vibor
    
    def zdorovie(self):
        hp = self.fighter_1.get_hp()
        if hp > 0:
            return f"{text.hp_my} {hp}"
        else :
            return text.no_my
    
    def udar_golovoy_1(self):
        uron = self.fighter_2.get_attack() * self.hit_1.get_krit() * self.random_popadanie_golovoy()
        self.fighter_1.set_hp(self.fighter_1.get_hp() - uron)
        if uron == 0:
            return text.habib_miss
        else:
            return text.habib_strike

    def udar_rukoy_1(self):
        uron = self.fighter_2.get_attack() * self.hit_2.get_krit()
        self.fighter_1.set_hp(self.fighter_1.get_hp() - uron)
        if uron == 0:
            return text.habib_miss
        else:
            return text.habib_strike
    
    def udar_nogoy_1(self):
        uron = self.fighter_1.get_attack() * self.hit_3.get_krit() * self.random_popadanie_nogoi()
        self.fighter_1.set_hp(self.fighter_1.get_hp() - uron)
        if uron == 0:
            return text.habib_miss
        else:
            return text.habib_strike
