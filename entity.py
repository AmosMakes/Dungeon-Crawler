import random as rng

class Entity:
    def __init__(self, health : float, max_health : float, defense :float , energy : float, max_energy : float, min_damage : float, max_damage : float) -> None:
        self.health = health
        self.max_health = max_health
        self.defense = defense
        self.energy = energy
        self.max_energy = max_energy
        self.min_damage = min_damage
        self.max_damage = max_damage
    
    # We get a random damage base on the stats and use take damage function
    def attack(self, entity ) -> None:
        self.energy = clamp(self.energy -20,0,self.max_energy)
        damage = rng.randint(self.min_damage,self.max_damage)
        entity.take_damage(damage,self)
        print(" ")
        print(f"{self.name} attacked {entity.name}")
        print(f"{self.name} dealt {damage}")
        print(f"{entity.name} has {entity.health}hp / {entity.defense}def / {entity.energy}energy")
        print(" ")
    
    # this function will be called in fight not in attack function
    def can_attack(self) -> bool   :
        if self.energy > 20:
            return True
        return False
        
    
    # the energy recharges and give 10hp back
    def rest(self) -> None:
        self.energy = self.max_energy 
        self.health = clamp(self.health + 10, 0, self.max_health)
        print(f"{self.name} replenished their energy")
        print(f"hp: {self.health}") 
    
    # simple take damage function  defense must be destroyed before damaging health
    def take_damage(self, damage : float,entity) -> None:
        if self.defense > 0:
            self.defense = clamp(self.defense - damage,0,5000)
        else:
            self.health = clamp(self.health - damage,0,5000) 
            if self.health <= 0:
                self.die(entity)
    
    # this function get rewriten in child class its here just so that take_damage can call it so i dont have to make new take_damage in child
    def die(self,entity) -> None:
        pass
        

class Enemy(Entity):
    def __init__(self, health : float, max_health : float, defense :float , energy : float, max_energy : float, min_damage : float, max_damage : float, min_gold : float, max_gold: float, name : str,tressure) -> None:
        self.min_gold = min_gold
        self.max_gold = max_gold
        self.name = name
        self.tressure = tressure
        super().__init__(health,max_health,defense,energy,max_energy,min_damage,max_damage)
    
    #enmy AI
    def enemy_turn(self,player) :
        if self.energy > 20:
            self.attack(player)
        else:
            self.rest()
    
    
    #we give player the gold and random chance at item
    def die(self,player):
        gold_earned = rng.randint(self.min_gold,self.max_gold)
        player.purse += gold_earned
        print(" ")
        print(f"The player has killed {self.name}")
        print(f"Player earned {gold_earned}g")
        if rng.randint(1,15) == 1:  
            match self.tressure.type:
                case 0: # armor
                    player.add_armor(self.tressure)
                case 1: # weapon
                    player.add_weapon(self.tressure)
            #self.player/
        
        print("--------------------")
        print(" ")
    

class Player(Entity):
    def __init__(self, health : float, max_health : float, defense :float , energy : float, max_energy : float, min_damage : float, max_damage : float, purse : int, armor, weapon) -> None:
        self.purse = purse
        self.heal_amount = 1
        self.armor = armor
        self.weapon = weapon
        self.name = "Player"
        self.armor_inventory = []
        self.weapon_inventory =[]
        self.add_armor(armor)
        self.add_weapon(weapon)
        super().__init__(health,max_health,defense,energy,max_energy,min_damage,max_damage)
        self.equip_armor(armor)
        self.equip_weapon(weapon)
    
    # We check if the armor is null or if we allready have if its uniqe we add it into our inventory 
    def add_armor(self,armor) -> None:
        if armor != None or armor in self.armor_inventory == True:
            self.armor_inventory.append(armor)
            print(" ")
            print("The player obtained " + armor.name)
            print(" ")
    
    # We do this so we can check before adding armor and so that the code cannot acidently change our inventory safety
    def get_armor(self) -> None:
        armor_arr = []
        for i in self.armor_inventory:
            armor_arr.append(i.name)
        return armor_arr
    
    # we equip our armor and add apropriate stats to out player
    def equip_armor(self,armor) -> None:
        if armor != None or armor in self.armor_inventory == False:
            self.armor = armor
            self.defense = armor.defense
            
            print(" ")
            print(f"you equiped {armor.name}")
            print(f"your defense {self.defense}")
            print(" ")
        
    
    
    # We check if the weapon is null or if we allready have if its uniqe we add it into our inventory 
    def add_weapon(self,weapon) -> None:
        if weapon != None or weapon in self.weapon_inventory == True:
            self.weapon_inventory.append(weapon)
            print(" ")
            print("The player obtained " + weapon.name)
            print(" ")
    
    # We do this so we can check before adding weapon and so that the code cannot acidently change our inventory safety
    def get_weapon(self) -> None:
        weapon_arr = []
        for i in self.weapon_inventory:
            weapon_arr.append(i.name)
        return weapon_arr
    
    # we equip our weapon and add apropriate stats to out player
    def equip_weapon(self,weapon) -> None:
        if weapon != None or weapon in self.weapon_inventory == False:
            self.weapon = weapon
            self.min_damage = self.min_damage + weapon.damage
            self.max_damage = self.max_damage + weapon.damage
            print(" ")
            print(f"you equiped {weapon.name}")
            print(f"your damage {self.min_damage}-{self.max_damage }")
            print(" ")
    
    # a simple switch statment for upgrading
    def upgrade(self,stat : str) -> None:
        match stat.lower():
            case "health":  
                self.health += 50
                self.max_health += 50
                print(" ")
                print("The player has upgraded their max health by 50")
                print(f"Player hp {self.max_health}")
                print(" ")
            case "energy": 
                self.energy += 60 
                self.max_energy += 60
                print(" ")
                print("The player has upgraded their max energy by 50")
                print(f"Player energy {self.max_energy}")
                print(" ")
            case "damage":  
                self.min_damage += 15
                self.max_damage += 15
                print(" ")
                print("The player has upgraded their damage by 15")
                print(f"Player damage {self.min_damage}-{self.max_damage}")
                print(" ")
    
    # check if we have enought to buy
    def buy(self,price) -> bool:
        if price <= self.purse:
            self.purse -= price
            return True
        return False
        
    
    # we check if player has heals and if yes we add him random health from 25-30 and clamp it at max_health and 
    def heal(self) -> bool:
        if self.heal_amount > 0:
            health_healed = rng.randint(300,500)
            self.health = clamp(self.health + health_healed,0,self.max_health)
            self.heal_amount -= 1
            print(" ")
            print(f"player healed {self.health}/{self.max_health}")
            print(" ")
            return True
        print(" ")
        print(f"player doesnt have enough heals")
        print(" ")
        return False

    #player input
    def player_turn(self,enemy) -> bool:
        player_input = input("Whats your move  : ").lower()
        match player_input:
            case "attack":
                if self.can_attack():
                    self.attack(enemy)
                    return True
                print(" ")
                print("Player doesnt have enough energy")
                print(" ")
                return False
            case "rest":
                self.rest()
                return True
            case "heal":
                if self.heal():
                    return True
        return False

    #player died
    def die(self,player) -> None:
        print(" ")
        print("you died returning to lobby")
        print("--------------------")
        print(" ")
        #self.print_stats()
        # set running false
    
    #prints player stats called when new thing equiped or dead
    def print_stats(self) -> None:
        print(" ")
        print("Player Stats")
        print("--------------------")
        print("Health - " + str(self.health))
        print("Energy - " + str(self.max_energy))
        print("Purse - " + str(self.purse))
        print("Base Damage - " + str(self.min_damage))
        print("Armor Inventory - " + str(self.get_armor()))
        print("Weapon Inventory - " + str(self.get_weapon()))
        print("--------------------")
        print(" ")
        
    



# a simple clamp function for conviniece
def clamp(n : float, min : float, max : float): 
    return sorted((min,n,max))[1]
    