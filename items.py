# the item class doesnt realy have to complicated but can be usefull if i want to more features
class Item :
    def __init__(self, type : int, damage : float , defense : float , name : str ):
        self.type = type # 0 - armor / 1 - weapon
        self.damage = damage
        self.defense = defense
        self.name = name