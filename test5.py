class Character:
    def __init__(self, charclass, health, strength, defence, agility):
        self.heroType = charclass
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def showStats(self):
        print "Character type:", self.heroType
        print " "
        print "--------------------"
        print "Health:", self.health
        print "Strength:", self.strength
        print "Defence:", self.defence
        print "Agility:", self.agility

    def agility2(self):
        return self.agility

class Enemy:
    def __init__(monster, charclass, health, strength, defence, agility):
        monster.eType = charclass
        monster.health = health
        monster.strength = strength
        monster.defence = defence
        monster.agility = agility

    def showStats(monster):
        print "Monster type:", monster.eType
        print "---------------------"
        print "Health:", monster.health
        print "Strength:", monster.strength
        print "Defence:", monster.defence
        print "Agility:", monster.agility

    def agility2(monster):
        return monster.agility

def WormBeast():
    global monster
    monster = Enemy('WormBeast', 500, 1, 1, 1)
    return monster

def into():
    print "You story for your name goes here: ........"
    raw_input ("Press <Enter> to continue")
    menu()

def fight():
    import random
    print "FIGHT"
    global heroRun
    print "This Guy"
    activeChar.showStats()
    print "vs"
    monster.showstats()

    print "Do you want to fight or run?"
    print "Run (1)"
    print "Fight (2)"
    battleInput = input("Enter your choice: ")
    if battleInput ==1:
        print "You attempt to run"
        raw_input("Toko Tok Tok")

        if activeChar.agility2() > monster.agility2():
            print "You have Run"
            raw_input("Toko Tok Tok")
            moon()
        if activeChar.agility2() < monster.agility2():
            print "Ha ha ha ...a...a... !!! You can not run away"
            raw_input("Ha ha ha !!!")
            fight()

    while battleInput ==2:
        if monster.health >= 0 and activeChar.health >=0:
            HeroNormalDamage = [0,10,20,30,40]
            HeroCriticalDamage = [0,0,0,0,100]
            HeroNormalDamageRandom = random.choice(HeroNormalDamage)
            HeroCriticalDamageRandom = random.choice(HeroCriticalDamage)

            HitCalculator = [1,1,1,1,2]
            randomHitCalculator = random.choice(HitCalcultor)

            eNormalDamage = [0,10,20,30,40]
            eCriticalDamage = [0,0,0,0,100]
            eNormalDamageRandom = random.choice(eNormalDamage)
            eCriticalDamageRandom = random.choice(eCriticalDamage)
            
            if randomHitcalculator ==1:
                monster.health = monster.health - HeroNormalDamageRandom
                activeChar.health = activeChar.health - eNormalDamageRandom
                print "You have hit monster for", HeroNormalDamageRandom, "Damage. You have", \
                activeChar.health, "remaining"
                print "Monster has hit you for", eNormalDamageRandom, "Damage. Enemy has", \
                monster.health, "remaining"
                raw_input("Wait wait!!!!!")
            if randomHitcalculator ==2:
                monster.health = monster.health - HeroCriticalDamageRandom
                activeChar.health = activeChar.health - eCriticalDamageRandom
                print "You have critically hit monster for", HeroCriticalDamageRandom, \
                "Damage. You have", activeChar.helath, "remaining"
                print "Monster has critcally Hit you for", eCriticalDamageRandom, \
                "Damage. Enemy has", monster.health, "remaining"
                raw_input("Wait wait!!!!!")

        else:
            battleInput = 0
            if monster.health <=0:
                raw_input ("You win the battle")
            if activeChar.health <=0:
                raw_input ("You lost the battle")
                

def moon():
    import random
    print "Your", activeChar.heroType, "character has reached the moon"
    print "Do you want to hunt for Monsters (Press<1>)?"
    print "Do you want to go back to the earth to select a new plant to go to (Press <2>)"
    choiceLevel_Moon = input("Enter your choice" )
    if choiceLevel_Moon ==1:
        rand = random.randint(1,10)
        if rand <=0:
            print "You met a POWERFUL MONSTER"
            raw_input("To fight Press <ENTER> now!!!")
            moon()
            
        if rand >=2:
            rand2 = random.randint(1,10)
            if rand2 <5:
                #print "You met a FLAME BEAST"
                #raw_input("To fight Press <ENTER> now!!!")
                #moon()
                WormBeast()
                raw_input("Press <ENTER> to see his status")
                monster.showstats()
                raw_input("Lets Begin the fight")
            fight()
            if rand2 >=5:
                print "You met a ICE BEAST"
                raw_input("To fight Press <ENTER> now!!!")
                moon()
            

    if choiceLevel_Moon ==2:
        print "You are now in the rocket back to the earth"
        raw_input("You have landed on the earth press <Eneter> to select another planet")
        beginGame()
        

def beginGame():
    print "Game Begins Here"
    print "Do you want to go to the Moon (Press <1>)"
    print "Do you want to go to Saturn (Press <2>)"
    print "Do you want to go to Mars (Press <3>)"
    choiceLevel = input("Enter your Choice: ")
    if choiceLevel ==1:
        print "Go to the Moon"
        moon()

def confirmHero():
    #print "You have chosen", heroType, ". His stength is", strength
    activeChar.showStats()
    print "To confirm the character you're chosing press <1> to reselect Press <2>"
    choiceChar = input("Enter your Choice: ")
    if choiceChar ==1:
        print "Begin Game"
        beginGame()
    if choiceChar ==2:
        startGame()

def startGame():
    global activeChar
    #global heroType
    #global health
    #global strength
    #global defence

    print "Please choose your character: "
    print "1) Ogre"
    print "2) Human"
    chooseHero = input("Enter your choice: ")
    if chooseHero ==1:
        #heroType= 'Ogre'
        #health = 150
        #strength = 150
        #defence = 50
        activeChar = Character('Ogre', 150, 150, 50, 50)
        confirmHero()
    if chooseHero ==2:
        #heroType= 'Human'
        #health = 200
        #strength = 150
        #defence = 50
        activeChar = Character('Human', 200, 150, 50, 50)
        confirmHero()

def menu():
    print "1) Introduction"
    print "2) Start Game"
    print "3) Credits"
    print " "
    print " "
    print " "
    print "9) Quit the game"
    print "======================================="
    userinput = input("Enter your choice: ")
    if userinput ==1:
        print "Introduction"
        into()
    elif userinput ==2:
        print "Start Game"
        startGame()
    #elif userinput ==3...
    elif userprint ==9:
        quit()
    else:
        print "You have entered an invalid choice"
        
menu()
