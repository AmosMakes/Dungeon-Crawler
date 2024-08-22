from resources import *

class Shop:
    def __init__(self) -> None:
        self.weapon_price = {sharp_sword : 100, diamond_sword : 200, dragon_sword : 300}
        self.armor_price = {hardend_armor : 150, diamond_armor : 250,dragon_armor : 350}
        self.in_shop = True
        self.print_instructions()
        self.print_offers()
        self.shop()
    
    #while loop for this scene
    def shop(self):
        while self.in_shop:
            self.player_commands()
        
    #could be more optimized and rewrtien
    def player_commands(self):
        player_input = input("Shop : ").lower()
        match player_input.split()[0]:
            case "buy":
                item = player_input.lstrip("buy ")
                for i in self.weapon_price:
                    if i.name == item and player.buy(self.weapon_price[i]):
                        player.add_weapon(i)
                        self.weapon_price.pop(i)
                        break
                for i in self.armor_price:
                    if i.name == item and player.buy(self.armor_price[i]):
                        player.add_armor(i)
                        self.armor_price.pop(i)
                        break
                if item == "heal":
                    if player.buy(10):
                        print(" ")
                        print("You purchased heal")
                        print(" ")
                        player.heal_amount += 1
            case "offers":
                self.print_offers()
            case "leave":
                print(" ")
                print("You left the shop")
                print(" ")
                self.in_shop = False
    
    def print_instructions(self):
        print(" ")
        print("--------------------")
        print("buy (item name) - to buy item")
        print("offers          - shows current offers")
        print("leave           - to leave shop")
        print("--------------------")
        print(" ")
    
    #prints current offers
    def print_offers(self):
        print("--------------------")
        print("     Weapons")
        for i in self.weapon_price:
            print(f"{i.name} - {self.weapon_price[i]} ({i.damage}dmg)")
        print(" ")
        print("     Armor")
        for i in self.armor_price:
            print(f"{i.name} - {self.armor_price[i]} ({i.defense}def)")
        print(" ")
        print("Heal   - 10g")
        print("--------------------")
        print(" ")