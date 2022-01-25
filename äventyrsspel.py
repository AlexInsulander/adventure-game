import random as rand
import keyboard
import time
import os


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()


class item():
    def __init__(self, name, quantity=0):
        self.name = name
        self.quantity = quantity

    def add_quantity(self):

        self.quantity += 1

    def sub_quantity(self):

        self.quantity -= 1

    def set_quantity(self, new_quantity):

        self.quantity = new_quantity


'''
Potion class types
'''

smallHealingPotion = item("Small healing potion")
bigHealingPotion = item("Big healing potion")
ragePotion = item("Rage potion")


class hero():
    def __init__(self, name, str, hp, gold):
        self.name = name
        self.str = str
        self.hp = hp
        self.gold = gold
        self.showinv = [smallHealingPotion, bigHealingPotion, ragePotion]
        self.killcount = 0
        self.lvl = 1

    def add_strength(self, strength, add):
        strength += add

    def __str__(self):
        print(f"You are the hero {player.name} with strength {player.str} och hp {player.hp}. You have killed {player.killcount} enemiess, you are lvl {player.lvl} and have {player.gold} gold. In your inventory there is")
        for i in range(0, len(player.showinv)):
            if player.showinv[i].quantity == 0:
                pass
            elif player.showinv[i].quantity > 0:
                print(f"{player.showinv[i].quantity} " +
                      f"{player.showinv[i].name}")


player = hero("Larry", 10, 10, 0)


class monster():
    def __init__(self, monsterDmg, monsterHp, monsterType):

        self.monsterDmg = monsterDmg
        self.monsterHp = monsterHp
        self.monsterType = monsterType

    def get_monsterDmg(self):
        print(self.monsterDmg)

    def set_monsterDmg(self, new_monsterDmg):
        self.monsterDmg = new_monsterDmg

    def get_monsterHp(self):
        print(self.monsterHp)

    def set_monsterHp(self, new_monsterHp):
        self.monsterHp = new_monsterHp

    def get_monsterType(self):
        return self.monsterType

    def set_monsterType(self, new_monsterType):
        self.monsterType = new_monsterType


'''
Monster class types
'''
skeleton = monster(2, 2, "skeleton")
bats = monster(1, 2, "bats")
goblins = monster(3, 3, "goblins")
barbarians = monster(4, 5, "barbarians")
motherwitch = monster(10, 20, "motherwitch")


def silverchest(gold, sword):
    """
    Chest opening.
    (gold) --> (gold),
    """
    odds = rand.randint(1, 10)
    if odds <= 4:
        gained_gold = rand.randint(5, 10)
        gold += gained_gold
        print(
            f"You gained {gained_gold} from the chest, your new gold count is {gold}")
    elif odds <= 8:
        potion_type = rand.randint(1, 3)
        if potion_type == 1:
            ragePotion.add_quantity()
            print("You gained one rage potion")
            checkpotions()
        elif potion_type == 2:
            bigHealingPotion.add_quantity()
            print("You gained one big healing potion")
            checkpotions()
        elif potion_type == 3:
            smallHealingPotion.add_quantity()
            print("You gained one small healing potion")
            checkpotions()
    else:
        odds = rand.randint(1, 4)
        print(odds)
        if odds == 1 and odds > sword:
            print("You found an Wooden Sword!")
            sword = 1
        elif odds == 2 and odds > sword:
            print("You found an Iron Sword!")
            sword = 2
        elif odds == 3 and odds > sword:
            print("You found an Diamond Sword!")
            sword = 3
        elif odds == 4 and odds > sword:
            print("You found an The Dragonslayers Sword!")
            sword = 4
        else:
            print(
                f"You found a sword which is weaker than your current one, you throw it away")

    return gold, sword


def dungeon(alive, hp, str, gold, killcount, sword):
    i = 0
    print("You find yourself in a new cave system and see three doors infront of you, but the question remains, ")
    while alive == True and i < 8:
        while True:
            answer = input(
                "which door will you go through? Left[a] Middle[s] Right[d] --> ")
            if answer == "a":
                print("You went through the left door")
                break
            elif answer == "s":
                print("You went through the middle door")
                break
            elif answer == "d":
                print("You went through the right door")
                break
            else:
                print("please select a valid option")

        door = rand.randint(1, 3)
        if door == 1:

            monsterbattle = rand.randint(1, 4)
            if monsterbattle == 1:
                alive, hp, gold, killcount = fighting(
                    alive, hp, str, skeleton.monsterHp, skeleton.monsterDmg, skeleton.monsterType, gold, killcount)
            elif monsterbattle == 2:
                alive, hp, gold, killcount = fighting(
                    alive, hp, str, bats.monsterHp, bats.monsterDmg, bats.monsterType, gold, killcount)
            elif monsterbattle == 3:
                alive, hp, gold, killcount = fighting(
                    alive, hp, str, goblins.monsterHp, goblins.monsterDmg, goblins.monsterType, gold, killcount)
            elif monsterbattle == 4:
                alive, hp, gold, killcount = fighting(
                    alive, hp, str, barbarians.monsterHp, barbarians.monsterDmg, barbarians.monsterType, gold, killcount)
        elif door == 2:
            gold, sword = silverchest(gold, sword)
        elif door == 3:
            alive, hp = trap(alive, hp)
        time.sleep(5)
        clearConsole()

        i += 1

    return alive, hp, gold, killcount, sword


def fighting(alive, hp, dmg, monsterhp, monsterdmg, monstertype, gold, killcount):
    print(
        f"You have entered a fight with {monstertype}. The {monstertype} has {monsterhp} hp and {monsterdmg} dmg")
    if monsterdmg + monsterhp < hp + dmg:
        gained_gold = rand.randint(1, 5)
        gold += gained_gold
        killcount += 1
        print(f"You have won the battle against the {monstertype}")
        print(
            f"You have gained {gained_gold} and your current gold count is {gold}")
        if killcount % 3 == 0:
            player.lvl += 1
            player.str += 1
            player.hp += 1
            print(
                f"congratulations you just leveled up to level {player.lvl}. Your new strength is {player.str} and you new hp is {player.hp}")

        time.sleep(3)
    else:
        print(f"The {monstertype} has defeated you")
        print(monsterdmg, monsterhp)
        print(hp, dmg)
        alive = False

    return alive, hp, gold, killcount


def trap(alive, hp):
    print("You found a trap!")
    random_letter = rand.randint(1, 6)
    if random_letter == 1:
        random_letter = "q"
    elif random_letter == 2:
        random_letter = "w"
    elif random_letter == 3:
        random_letter = "e"
    elif random_letter == 4:
        random_letter = "a"
    elif random_letter == 5:
        random_letter = "s"
    elif random_letter == 6:
        random_letter = "d"

    print(f"You need to press {random_letter}, in 3 seconds or less")

    i = 0
    while True:  # making a loop
        i = i + 1

        if i > 30:
            print("You took too long so you lost 2 hp")
            hp -= 2
            break

        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(f'{random_letter}'):  # if key 'q' is pressed
                print('You Pressed A Key!')
                print("You live")

                break   # finishing the loop

        except:
            break  # if user pressed a key other than the given key the loop will break

        time.sleep(0.1)
    return alive, hp


def heart_beat_test():
    print(f"Your heart is beating fast. You need to calm down! (Press space when the numbers 1 appear on your screen)")

    time.sleep(2)
    score = 0
    i = 0
    mellanrum = 30
    runda = 0

    while True:
        i += 1

        if runda == 5:
            print("Congratulations!")
            break

        if i < mellanrum:
            print("0")

        if i < mellanrum and keyboard.is_pressed(" "):
            print("Faail!")
            break

        if i >= mellanrum:
            print(1)

        try:
            if keyboard.is_pressed(" ") and i >= mellanrum and score == 0:
                print('Nice!')
                score += 1
                mellanrum = rand.randint(15, 50)
                i = 0
                runda += 1
                time.sleep(1)
                score = score - 1
            if i > mellanrum + 12 and score == 0:
                print("0")
                print("Faail!")
                break

        except:
            break

        time.sleep(0.04)


def checkpotions():
    potion_count = 0
    for i in range(0, len(player.showinv)):
        potion_count += player.showinv[i].quantity
    print(potion_count)
    if potion_count == 5:
        for i in range(0, len(player.showinv)):
            if player.showinv[i].quantity > 0:
                print(f"{player.showinv[i].quantity} " +
                      f"{player.showinv[i].name}")
        while True:
            answer = input(
                "Which potion do you want to use? rage potion [a] small healing potion [s] big healing potion [d] --> ")
            if answer == "a":
                if ragePotion.quantity > 0:
                    ragePotion.sub_quantity
                    break
                else:
                    print("You dont have enough of this potion")
            elif answer == "s":
                if smallHealingPotion.quantity > 0:
                    smallHealingPotion.sub_quantity
                    break
                else:
                    print("You dont have enough of this potion")
            elif answer == "d":
                if bigHealingPotion.quantity > 0:
                    bigHealingPotion.sub_quantity
                    break
                else:
                    print("You dont have enough of this potion")
            else:
                print("please select a valid option")
    else:
        pass


def use_potion(hp, str):
    while True:
        answer = input(
            "Which potion do you want to use? rage potion [a] small healing potion [s] big healing potion [d] --> ")
        if answer == "a":
            if ragePotion.quantity > 0:
                ragePotion.sub_quantity()
                str += 2
                print("you gained 2 str")
                break
            else:
                print("You dont have enough of this potion")
                break
        elif answer == "s":
            if smallHealingPotion.quantity > 0:
                smallHealingPotion.sub_quantity()
                hp += 1
                print("you gained 1 hp")
                break
            else:
                print("You dont have enough of this potion")
                break
        elif answer == "d":
            if bigHealingPotion.quantity > 0:
                bigHealingPotion.sub_quantity()
                hp += 2
                print("you gained 2 hp")
                break
            else:
                print("You dont have enough of this potion")
                break
        else:
            print("please select a valid option")
            break
    return hp, str


def main():
    sword = 0
    alive = True

    while alive == True and player.hp > 0:
        print("In a land far far away was, a man, perhaps a skeleton called Larry.")
        print("He was out patrolling with his comrades when he saw a beautiful butterfly and decided to follow it.")
        print("The butterfly flies into a magical forest of wild creatures")
        print("Larry doesnt realise this until it is too late and cant manage to find his way back")
        print("Larry is confused and scared so he seeks safety by going into a cave")
        print("There he finds a night witch who gives him the option to pick between three chests\n")
        answer = ""
        while True:
            answer = input(
                "\nWhich chest do you want to choose? Left[a] Middle[s] Right[d] check inventory[i] use potion [p] --> ")
            if answer == "a":
                print("hp + 1")
                player.hp += 1
                break
            elif answer == "s":
                print("hp + 1")
                player.str += 1
                break
            elif answer == "d":
                print("hp + 1")
                player.hp += 1
                break
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)
            else:
                print("Please select a valid option")
        while True:
            answer = input(
                "Do you want to exit the cave or look around? Exit[a] Look around[s] check inventory[i] use potion [p] --> ")
            if answer == "s":

                print("You looked around and found 1 big heal potion")
                bigHealingPotion.add_quantity()
                print("You gained one big healing potion")
                checkpotions()
                break
            elif answer == "a":
                time.sleep(0.1)
                clearConsole()
                print(
                    "You turn back to exit the cave but find that there is an exit no longer")
                while True:
                    answer = input(
                        "You look back. Your now only two options are to either talk to the witch take a look around. What shall it be? look around[a] talk to the witch[s] check inventory[i] use potion [p] --> ")
                    if answer == "a":
                        print(
                            "You look around you and spot a potion. You add 1 big heal potion to your inventory")
                        break
                    elif answer == "s":
                        while True:
                            answer = input(
                                "You talk to the witch and she asks you to choose between an apple[a] and wine[s] check inventory[i] use potion [p] --> ")
                            if answer == "a":
                                print("It was poison so you lost one hp")
                                player.hp -= 1
                                break
                            elif answer == "s":
                                time.sleep(0.1)
                                print("You gained one str")
                                player.str += 1
                                break
                            elif answer == "i":
                                player.__str__()
                            elif answer == "p":
                                player.hp, player.str = use_potion(
                                    player.hp, player.str)

                            else:
                                print("please select a valid option")
                        break
                    elif answer == "i":
                        player.__str__()
                    elif answer == "p":
                        player.hp, player.str = use_potion(
                            player.hp, player.str)
                    else:
                        print("please select a valid option")
                break
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)
            else:
                print("please select a valid option")
        time.sleep(3)
        clearConsole()
        alive, player.hp, player.gold, player.killcount, sword = dungeon(
            alive, player.hp, player.str, player.gold, player.killcount, sword)
        print("You find your way out of the cave and discover a path leading down to a cabin. By the cabin you see a well and something shiny in the grass")
        while True:
            answer = input(
                "Where do you go? Shiny object[a] cabin[s] well[d] back into the cave system[f] check inventory[i] use potion [p] --> ")
            if answer == "a":
                print(
                    "You approach the shiny object and find a helmet with some bloodstains on it")
                while True:
                    answer = input(
                        "Do you want to equip the helmet or not? yes[a] no[s] check inventory[i] use potion [p] --> ")
                    if answer == "a":
                        print("You have equipped the helmet")
                        break
                    elif answer == "s":
                        print("You chose to not equip the helmet")
                        break
                    elif answer == "i":
                        player.__str__()
                    elif answer == "p":
                        player.hp, player.str = use_potion(
                            player.hp, player.str)
                    else:
                        print("please select a valid option")
                break
            elif answer == "s":
                break
            elif answer == "d":
                print(
                    "You approach the well but as you look down bats flies up in your face and you lose one HP")
                player.hp -= 1
                break
            elif answer == "f":
                alive, player.hp, player.gold, player.killcount, sword = dungeon(
                    alive, player.hp, player.str, player.gold, player.killcount, sword)
                print("You find your way out of the cave and discover a path leading down to a cabin. By the cabin you see a well and something shiny in the grass")
#            elif answer == "b":
#                player.gold = shop(player.gold)
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)
            else:
                print("please select a valid option")

        print("You enter the cabin ")
        while True:
            answer = input(
                "Where to you look first? left[a] basement[s] right[d] check inventory[i] use potion [p] --> ")
            if answer == "a":
                alive, player.hp = trap(alive, player.hp)

                while True:
                    answer = input(
                        "Where to you look now? basement[a] right[s] check inventory[i] use potion [p] --> ")
                    if answer == "a":
                        print(
                            "you go down the basement and find a labratory, down in the labratory you find three different potions.")
                        while True:
                            answer = input(
                                " Which one do you pick up first? small healing potion[a] big healing potion[s] rage potion[d] check inventory[i] use potion [p] --> ")
                            if answer == "a":
                                print(
                                    "You pick up the small healing potion but accedentally knock over the remaining bottles")
                                smallHealingPotion.add_quantity()
                                print("You gained one small healing potion")
                                checkpotions()
                                break
                            elif answer == "s":
                                print(
                                    "You pick up the big healing potion but accedentally knock over the remaining bottles")
                                bigHealingPotion.add_quantity()
                                print("You gained one big healing potion")
                                checkpotions()
                                break
                            elif answer == "d":
                                print(
                                    "You pick up the rage potion but accedentally knock over the remaining bottles")
                                ragePotion.add_quantity()
                                print("You gained one rage potion")
                                checkpotions()
                                break
                            elif answer == "i":
                                player.__str__()
                            elif answer == "p":
                                player.hp, player.str = use_potion(
                                    player.hp, player.str)
                            else:
                                print("please select a valid option")
                        break
                    elif answer == "s":
                        break

                    elif answer == "i":
                        player.__str__()

                    elif answer == "p":
                        player.hp, player.str = use_potion(
                            player.hp, player.str)

                    else:
                        print("please select a valid option")
                break
            elif answer == "s":
                print(
                    "you go down the basement and find a labratory, down in the labratory you find three different potions.")
                time.sleep(0.1)

                while True:
                    answer = input(
                        " Which one do you pick up first? red potion[a] purple potion[s] rage potion[d] check inventory[i] use potion [p] --> ")
                    if answer == "a":
                        print(
                            "You pick up the small healing potion but accedentally knock over the remaining bottles")
                        smallHealingPotion.add_quantity()
                        print("You gained one small healing potion")
                        checkpotions()
                        break
                    elif answer == "s":
                        print(
                            "You pick up the big healing potion but accedentally knock over the remaining bottles")
                        bigHealingPotion.add_quantity()
                        print("You gained one big healing potion")
                        checkpotions()
                        break
                    elif answer == "d":
                        print(
                            "You pick up the rage potion but accedentally knock over the remaining bottles")
                        ragePotion.add_quantity()
                        print("You gained one rage potion")
                        checkpotions()
                        break
                    elif answer == "i":
                        player.__str__()

                    elif answer == "p":
                        player.hp, player.str = use_potion(
                            player.hp, player.str)

                    else:
                        print("please select a valid option")

                while True:
                    answer = input(
                        "Where to you look now? left[a] right[s] check inventory[i] use potion [p] --> ")
                    if answer == "a":
                        alive, hp = trap(alive, player.hp)
                        break
                    elif answer == "s":
                        print("You turn right and continue walking")
                        break
                    elif answer == "i":
                        player.__str__()
                    elif answer == "p":
                        player.hp, player.str = use_potion(
                            player.hp, player.str)
                    else:
                        print("please select a valid option")
                break
            elif answer == "d":
                break
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)

            else:
                print("please select a valid option")

        while True:
            answer = input(
                "After 3 seconds an unknown sound appears and you chose to hide, \n where do you wanna hide? under a table[a] in the a cabinet[d] or behind the door [s] check inventory[i] use potion [p] --> ")
            if answer == "a":
                print("You decided to hide under the table. Just as you get under the table you hear the door open and footsteps inside the room.  The sound slowly dissapear after a short while..\nYou walk out of the room and you open the door but suddenly sense a presence behind you..\nITS THE MOTHERWITCH!! ")
                break
            elif answer == "s":
                print("You snuck inside the cabinet, and after a short while the sound dissapear\nYou walk out of the room and you open the door but suddenly sense a presence behind you..\nITS THE MOTHERWITCH!!")
                break
            elif answer == "d":
                print("You chose to hide yourself behind the door. but she finds you...")
                break
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)
            else:
                print("please select a valid option")

        heart_beat_test()

        while True:
            answer = input(
                "You have encountered the final boss! Mother Witch. What will you do.\nSwing your sword at her[a] or wait to see what she does[d] check inventory[i] use potion [p] --> ")
            if answer == "a":
                print(
                    "You took the initiative to start the fight with a effective swing! You made 10 damage on her!")
                motherwitch.monsterHp -= player.str
                break
            elif answer == "d":
                print(
                    "The MotherWitch took the initiative to start the fight and therefor you took 2 damage!")
                player.hp -= motherwitch.monsterDmg
                break
            elif answer == "i":
                player.__str__()
            elif answer == "p":
                player.hp, player.str = use_potion(player.hp, player.str)
            else:
                print("plese select a valid option")
        alive, player.hp, player.gold, player.killcount = fighting(
            alive, player.hp, player.str, motherwitch.monsterHp, motherwitch.monsterDmg, motherwitch.monsterType, player.gold, player.killcount)

        break
    if alive == True:
        print("congratulation you beat the mother witch")
        print("Here are your stats")
        player.__str__()

    else:
        print("You died")
        #       bossfight


main()
