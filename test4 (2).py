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
    def __init__(self, charclass, health, strength, defence, agility):
        self.charclass = charclass
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

def WormBeast():
    global monster
    monster = Enemy('WormBeast', 500, 1, 1, 1)
    return monster

def into():
    print "You story for your name goes here: ........"
    raw_input ("Press <Enter> to continue")
    menu()

def fight():
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

    elif battleInput ==2:
        print "   "

    else:
        battleInput = 0
        if monster.health <=0:
            print "You win the battle"
            moon()
        if activeChar.health <=0:
            print "You lost the battle"
            raw_input

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
