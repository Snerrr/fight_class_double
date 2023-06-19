class Hit:
    
    def __init__(self, nazvanie:str, krit: int, chance: float):
        self.nazvanie = nazvanie
        self.krit = krit
        self.chance = chance
    
    def get_krit(self):
        return self.krit
    
    def get_chance(self):
        return self.chance
    
    def get_chance(self):
        return self.name