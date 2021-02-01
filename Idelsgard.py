import random
import time
import sys
import os


def prnt_hold_0(messages):
    print(messages)
    time.sleep(0.2)


def prnt_hold_1(messages):
    print(messages)
    time.sleep(1)


def prnt_hold_2(messages):
    print(messages)
    time.sleep(2)


def title_screen():
    os.system('clear')
    prnt_hold_1('                 ')
    prnt_hold_1('#################')
    prnt_hold_1('     Welcome     ')
    prnt_hold_1('       to        ')
    prnt_hold_1('                 ')
    prnt_hold_0('I d e l s g a r d')
    prnt_hold_0('  . . . . . . .  ')
    prnt_hold_0('    . . . . .    ')
    prnt_hold_0('      . . .      ')
    prnt_hold_0('        .        ')
    prnt_hold_2('                 ')
    prnt_hold_1('An Adventure Game')
    prnt_hold_1('       by        ')
    prnt_hold_1('   Felix Harder  ')
    prnt_hold_2('#################')
    prnt_hold_2('                 ')
    os.system('clear')
    for x in range(5):
        prnt_hold_0('Loading.         ')
        os.system('clear')
        prnt_hold_0('Loading. .       ')
        os.system('clear')
        prnt_hold_0('Loading. . .     ')
        os.system('clear')


def ask_name(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_2("Welcome, adventurer!\n")
    hero_name = input("Before we dive into our little story, "
                      "please enter your name:\n")
    prnt_hold_1("\nHey, " + hero_name + "! Welcome!")
    prnt_hold_2("Let's begin the adventure!\n")
    prnt_hold_2("")
    os.system('clear')
    beginning(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def beginning(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    print('#################')
    print("\nGame is starting...\n")
    print('#################')
    prnt_hold_2("")
    os.system('clear')
    prnt_hold_2("Meet " + hero_name + ", the fearless adventurer.")
    prnt_hold_2("Our hero is on his way to Idelsgard, a small village"
                " that has their lovely church taken "
                "over by a " + enemy_option + ".")
    prnt_hold_2("'Just the right challenge for me', " + hero_name + " says,")
    prnt_hold_2("'though I'm afraid, my rusty spoon "
                "won't be enough for this challenge.'")
    prnt_hold_2("You look down at your ineffective "
                "spoon in your hand, then put it away.")
    prnt_hold_2("You've been walking for hours, when you reach a crossroad.")
    prnt_hold_2(hero_name + " notices that the signs have been destroyed.")
    crossroad(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def crossroad(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_2("Take your chance!")
    print("Enter 1 to turn left.")
    print("Enter 2 to turn right.")
    while True:
        crossroad_decision = input("Which will it be, " + hero_name + ":\n")
        if crossroad_decision == "1":
            idelsgard(weapon, enemy_option,
                      weapon_list, hero_name, dwarf_name)
            break
        elif crossroad_decision == "2":
            deadly_valley(weapon, enemy_option,
                          weapon_list, hero_name, dwarf_name)
            break


def idelsgard(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_1("Good decision, " + hero_name + "!\n")
    prnt_hold_2("After a long walk, you can see the village.")
    prnt_hold_2("You arrive safely at Idelsgard.")
    prnt_hold_2("The villagers are euphoric you've finally arrived.")
    prnt_hold_2("The " + enemy_option +
                " has been upon them for quite some time.")
    prnt_hold_2("A dwarf greets you:")
    prnt_hold_2("'Greetings, " + hero_name + "!'")
    prnt_hold_2("It's your old friend " + dwarf_name + ".")
    prnt_hold_2("You've been on many adventures with him.")
    prnt_hold_2("'Let me join you!'")
    prnt_hold_2("Together you walk to the city center.")
    idelsgard_city(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def idelsgard_city(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    if "axe" in weapon:
        prnt_hold_1("You have two options to visit:")
        prnt_hold_0("Enter 1 to go to the tavern.")
        prnt_hold_0("Enter 3 to go to the church.")
        while True:
            locations = input("Where do you want to go next:\n")
            if locations == "1":
                tavern(weapon, enemy_option,
                       weapon_list, hero_name, dwarf_name)
                break
            elif locations == "3":
                church(weapon, enemy_option,
                       weapon_list, hero_name, dwarf_name)
                break
            else:
                idelsgard_city(weapon, enemy_option,
                               weapon_list, hero_name, dwarf_name)
                break
    else:
        prnt_hold_1("You have three options to visit:")
        prnt_hold_0("Enter 1 to visit the tavern.")
        prnt_hold_0("Enter 2 see what the shady merchant waving "
                    "at you from the corner of the street has to offer.")
        prnt_hold_0("Enter 3 try your luck at the church.")
        while True:
            locations = input("Where do you want to go:\n")
            if locations == "1":
                tavern(weapon, enemy_option, weapon_list,
                       hero_name, dwarf_name)
                break
            elif locations == "2":
                shady_merchant(weapon, enemy_option, weapon_list,
                               hero_name, dwarf_name)
                break
            elif locations == "3":
                church(weapon, enemy_option, weapon_list,
                       hero_name, dwarf_name)
                break
            else:
                idelsgard_city(weapon, enemy_option,
                               weapon_list, hero_name, dwarf_name)
                break


def tavern(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    if "dwarf" in weapon:
        prnt_hold_1("'No time for drinking again, " + hero_name +
                    ".' says " + dwarf_name + ".")
        prnt_hold_1("He is right, there's a " + enemy_option +
                    " waiting to be defeated.\n")
    else:
        prnt_hold_2("'Aye, the tavern of course old friend!' "
                    "says " + dwarf_name + ".")
        prnt_hold_2("The two of you spend the whole night drinking "
                    "and laughing about old times.")
        prnt_hold_2("When the sun rises, " + hero_name + " asks the dwarf:")
        prnt_hold_2("'Join me on my mission, " + dwarf_name +
                    ", one last time?'")
        prnt_hold_2("The dwarf doesn't hesitate a second. 'Of course I will'.")
        prnt_hold_2("With the dwarf as your ally, "
                    "you return to the city center.\n")
        weapon.append("dwarf")
    idelsgard_city(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def shady_merchant(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_2("'Beware of that merchant' says " + dwarf_name + ".")
    prnt_hold_1("You walk up to the merchant, "
                "since he won't stop waving at you.")
    prnt_hold_1("'If you must, I'll watch your back', "
                "the dwarf reassure's you.")
    prnt_hold_1("The merchant says: 'Don't be afraid, "
                "I'm your friend.'")
    prnt_hold_1("'A mysterious man gave me this for you, "
                "to defeat the " + enemy_option + ".'")
    prnt_hold_2("\nHe shows you the " + weapon_list + "!!!\n")
    prnt_hold_2("'It's yours,' the merchant says.")
    prnt_hold_2("You can't believe your eyes, the " + weapon_list +
                " was lost for hundreds of years.")
    prnt_hold_2("You show the axe to the dwarf.")
    prnt_hold_2("When " + hero_name + " turns around to thank him, "
                "he has disappeared.")
    prnt_hold_2("You swap your rusty spoon for the " + weapon_list + ".")
    prnt_hold_2("You feel prepared to fight!\n")
    prnt_hold_2("The two of you return to the city center.\n")
    weapon.append("axe")
    idelsgard_city(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def church(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_2("")
    os.system('clear')
    prnt_hold_2("")
    prnt_hold_2("It's time. You approach the church...")
    prnt_hold_2("")
    prnt_hold_2("You open the huge door, when the " + enemy_option +
                " lashes out at you!!!\n")
    if "axe" in weapon:
        prnt_hold_2("You feel confident, knowing you found the Axe.\n")
        if "dwarf" in weapon:
            prnt_hold_2(dwarf_name + " will fight by your side!")
            prnt_hold_2(hero_name + " readies his " + weapon_list + "!")
            prnt_hold_2("The " + enemy_option + " should stand no chance.\n")
            fight(weapon, enemy_option, weapon_list, hero_name, dwarf_name)
        else:
            fight(weapon, enemy_option, weapon_list, hero_name, dwarf_name)
    elif "dwarf" in weapon:
        prnt_hold_2("You only have your old rusty spoon,")
        prnt_hold_2("but " + dwarf_name + "'s a real warrior!")
        prnt_hold_2("Do you take the chance?\n")
        fight(weapon, enemy_option, weapon_list, hero_name, dwarf_name)
    else:
        prnt_hold_2("'I'm not ready', whispers " + hero_name + ".\n")
        fight(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def fight(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    print("Enter 1 to Fight!")
    print("Enter 2 to run away!")
    while True:
        fightorrun = input("Choose now, " + hero_name + ":\n")
        if fightorrun == "1":
            if "axe" in weapon:
                if "dwarf" in weapon:
                    prnt_hold_2("The " + enemy_option +
                                " knows he doesn't stand a chance.")
                    prnt_hold_2("Both of you attack!")
                    prnt_hold_2("The beast goes down!")
                    prnt_hold_2("You give him the final blow "
                                "with the " + weapon_list + "!")
                    prnt_hold_2("You have freed Idelsgard of the "
                                + enemy_option + ". You Win!!!\n")
                else:
                    prnt_hold_1("The " + enemy_option + " attacks relentless!")
                    prnt_hold_1("You fight back hard.")
                    prnt_hold_1("Swinging the " + weapon_list +
                                " again and again.")
                    prnt_hold_1("The " + enemy_option + " wounds you!")
                    prnt_hold_1("But you fight back bravely, until...")
                    prnt_hold_1("...you give the final blow!")
                    prnt_hold_2("The " + enemy_option + " is slain!")
                    prnt_hold_2("The wounds will heal in time.\n")
                    prnt_hold_2("You have freed Idelsgard of the "
                                + enemy_option + ". You Win!!!\n")
            elif "dwarf" in weapon:
                prnt_hold_1("You take the chance!")
                prnt_hold_2("Your spoon breaks as soon as "
                            "you make your first attack!")
                prnt_hold_1(dwarf_name + " goes in for the attack!")
                prnt_hold_1("He tries to save you, but the "
                            + enemy_option + " has already wounded you.")
                prnt_hold_2("It's bad...")
                prnt_hold_1("The dwarf keeps fighting!")
                prnt_hold_1("Until he slays the " + enemy_option + "!")
                prnt_hold_2("You both have freed Idelsgard!")
                prnt_hold_2("")
                prnt_hold_2("But only " + dwarf_name +
                            " will live to tell the tale...\n")
            else:
                prnt_hold_1("You do your best...")
                prnt_hold_1("But your rusty spoon breaks with "
                            "the first swing at the "
                            + enemy_option + ".")
                prnt_hold_2("The last thing you see is the "
                            + enemy_option + "'s mouth.")
                prnt_hold_2("")
                prnt_hold_2("YOU DIED!\n")
            replay()
            break
        if fightorrun == "2":
            prnt_hold_2("You run back to the city center!\n")
            idelsgard_city(weapon, enemy_option,
                           weapon_list, hero_name, dwarf_name)
            break


def deadly_valley(weapon, enemy_option, weapon_list, hero_name, dwarf_name):
    prnt_hold_1("You keep wandering for hours.")
    prnt_hold_1("'This can't be right', " + hero_name + " says to himself.")
    prnt_hold_1("You've landed in the deadly valley.")
    prnt_hold_1("Noone that enters it, ever returns.")
    prnt_hold_1("Our Hero, " + hero_name + " is lost forever...")
    prnt_hold_2("")
    prnt_hold_2("")
    prnt_hold_2(hero_name + " get's lost in the Deadly Valley.\n")
    prnt_hold_2("Noone has heard of him since...\n")
    replay()


def replay():
    restart = input("Play again? (Type Y/N)\n").lower()
    if restart == "y":
        prnt_hold_2("")
        os.system('clear')
        prnt_hold_2("\nRestarting the game ...\n\n")
        os.system('clear')
        start_adventure()
    elif restart == "n":
        prnt_hold_1("\n\nSee you next time.\n\n")
    else:
        replay()


def start_adventure():
    weapon = []
    hero_name = []
    weapon_list = random.choice(["Axe of Nhosneruh",
                                 "Axe of Ettun", "Axe of Eruh"])
    enemy_option = random.choice(["Ogre", "Wicked Witch", "Water Witch",
                                  "Witcher", "Nogron"])
    dwarf_name = random.choice(["Heldemir", "Gimli", "Gloin", "Domli"])
    ask_name(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


def start_adventure_title():
    weapon = []
    hero_name = []
    weapon_list = random.choice(["Axe of Nhosneruh",
                                 "Axe of Ettun", "Axe of Eruh"])
    enemy_option = random.choice(["Ogre", "Wicked Witch", "Water Witch",
                                  "Witcher", "Nogron"])
    dwarf_name = random.choice(["Heldemir", "Gimli", "Gloin", "Domli"])
    title_screen()
    ask_name(weapon, enemy_option, weapon_list, hero_name, dwarf_name)


start_adventure_title()
