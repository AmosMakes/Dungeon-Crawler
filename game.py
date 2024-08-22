import os
import entity
from resources import *
import dungeon
import shop

running = True
room = "lobby"

class Game():
    def __init__(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        global running
        print(" ")
        print("Welcome to Verdeit")
        print("--------------------")
        print("Story")
        print("----------")
        print("The city of Verdeit has the biggest dungeon in this island.")
        print("Venture into this dungeon and find its secrets and treasures as you reach the lowest floor")
        print("----------")
        print_how_to_play()
        running = command_you_ready()
        
        
    # changing scenes
    def run(self) -> None:
        global room
        while running:
            match room:
                case "lobby":
                    lobby_commands()
                case "dungeon":
                    dungeon.Dungeon()
                    room = "lobby"
                case "shop":
                    shop.Shop()
                    room = "lobby"
                    

# self explenatory
def lobby_commands() -> None:
    global running
    global room
    player_input = input("whats your next move : ").lower()
    match player_input.split()[0]:
        case "dungeon":
            room = "dungeon"
        case "shop":
            room = "shop"
        case "equip":
            weapon = player_input.strip("equip ")
            for i in player.armor_inventory:
                if i.name == weapon:
                    player.equip_armor(i)
            for i in player.weapon_inventory:
                if i.name == weapon:
                    player.equip_weapon(i)
        case "upgrade":
            stat = player_input.split()[1]
            if stat in ["health","energy","damage"] and player.buy(50):
                player.upgrade(stat)
                return
            print(f"not enough gold - {player.purse}/50")
        case "inventory":
            print(" ")
            print("Armor - " + str(player.get_armor()))
            print("Weapon - " + str(player.get_weapon()))
            print(" ")
        case "purse":
            print(" ")
            print(f"you have {player.purse}g")
            print(" ")
        case "instructions":
            print_how_to_play()
        case "quit":
            exit()

# self explenatory
def command_you_ready() -> bool:
    player_input = input("Are you ready : ").lower()
    if player_input == "yes" : 
        return True
    else:
        exit()

# self explenatory
def print_how_to_play() -> None:
    print(" ")
    print("How-to-play")
    print("--------------------")
    print("Dungeon      - you will have to pass 30 rooms if you die you start again with treasures found in the dungeon")
    print("Shop         - you will enter shop where you can buy ")
    print("Equip        - if you enter this and the name of equipment you will quip it stats boost")
    print("Inventory    - see your items")
    print("Purse        - see your coins")
    print("Upgrade      - if you enter this and the name of the stats it will upgrade for 100g (health/damage)")
    print("")
    print("Attack       - you will deal damage to enemy and use up your energy")
    print("Rest         - you will reset your energy")
    print("Heal         - you will heal and use your potion")
    print("")
    print("instructions - this message will reapet")
    print("Quit         - you will quit this game")
    print("--------------------")
    print(" ")
