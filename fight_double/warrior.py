class Fighter:
    
    def __init__(self, name: str, attack: int, hp: int):
        self.name = name
        self.attack = attack
        self.hp = hp
    
    def get_attack(self):
        return self.attack
    
    def get_hp(self):
        return self.hp
    
    def set_hp(self, hp):
        self.hp = hp
    
    def get_info(self):
        return f"name: {self.name},  attack: {self.attack},  hp: {self.hp}"