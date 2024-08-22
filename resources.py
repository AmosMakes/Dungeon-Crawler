from entity import *
from items import *

#------------------Item--------------------------

# starting items
iron_sword = Item(1,10,0,"iron sword")
iron_armor = Item(0,0,10,"iron armor")


#Shop items
sharp_sword = Item(1,30,0,"sharp sword")
hardend_armor = Item(0,0,35,"hardend armor")

diamond_sword = Item(1,70,0,"diamond sword")
diamond_armor = Item(0,0,100,"diamond armor")

dragon_sword = Item(1,120,0,"dragon sword")
dragon_armor = Item(0,0,200,"dragon armor")


#Enemy Drops
skeleton_sword = Item(1,40,0,"skeleton sword")
skeleton_armor = Item(0,0,60,"skeleton armor")


vampire_sword = Item(1,100,0,"vampire sword") 
undead_armor =  Item(0,0,150,"undead armor")

moonlight_sword = Item(1,200,0,"moonlight sword")
godskin_armor = Item(0,0,150,"godskin armor")
#------------------------------------------------

#-----------------Entity--------------------------

#------ Player
player = Player(100,100,0,100,100,15,40,50,iron_armor,iron_sword)

# |==============================================================================================================================|
# |  [ health , max_health , defense , energy , max_energy , min_damage , max_damage , min_gold , max_gold , name , treaseure ]  |
# |==============================================================================================================================|


#------ Floor 1 
enemy_1_01 = Enemy(50,50,0,100,100,10,40,25,40,"Simple Skeleton",skeleton_sword)
enemy_1_02 = Enemy(20,20,40,75,75,15,25,30,31,"Skeleton archer",skeleton_sword)
enemy_1_03 = Enemy(25,25,10,100,100,40,50,30,60,"Skeleton Minion",skeleton_sword)
enemy_1_04 = Enemy(150,150,0,40,40,10,15,25,40,"Skeleton Guard",skeleton_armor)
enemy_1_05 = Enemy(50,50,60,500,500,20,40,40,60,"Skeleton Ancestor",skeleton_armor)
#------


#------ Floor 2 
enemy_2_01 = Enemy(100,100,0,100,150,30,60,70,75,"Goblin",vampire_sword)
enemy_2_02 = Enemy(40,40,80,125,125,30,55,65,70,"Undead",vampire_sword)
enemy_2_03 = Enemy(55,55,20,100,100,50,70,90,110,"Phantom",vampire_sword)
enemy_2_04 = Enemy(200,200,0,60,60,20,25,100,110,"Zombie",undead_armor)
enemy_2_05 = Enemy(70,70,80,500,500,40,60,150,200,"Mimic",undead_armor)
#------


#------ Floor 3
enemy_3_01 = Enemy(150,150,20,200,200,50,80,110,115,"Cyclops",moonlight_sword)
enemy_3_02 = Enemy(80,80,100,150,150,60,70,100,120,"Trol",moonlight_sword)
enemy_3_03 = Enemy(100,100,40,180,180,60,80,70,150,"Sea Serpent",moonlight_sword)
enemy_3_04 = Enemy(350,350,0,100,100,50,75,150,200,"Lich",godskin_armor)
enemy_3_05 = Enemy(100,100,120,500,500,40,80,60,100,"Basilisk",godskin_armor)
#------


#------ bosses
enemy_0_01 = Enemy(150,150,60,100,100,50,70,200,250,"Skeleton Boss",skeleton_armor)
enemy_0_02 = Enemy(350,350,60,100,100,50,70,200,250,"Giant",undead_armor)
enemy_0_03 = Enemy(666,666,66,160,160,100,120,0,0,"Oldest one",godskin_armor)
#------

#------------------------------------------------


