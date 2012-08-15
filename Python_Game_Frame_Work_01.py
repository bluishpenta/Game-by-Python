class Character: #This is the Hero Class and it creates the container for enemy characteristics.
    def __init__(self, charclass, health, strength, defence, agility): # This function creates the hero's characteristics framework
        self.charclass = charclass
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def showstats(self):  # this function is used when we want to display the hero's stats
        print "Character type:", self.charclass
        print " "
        print "---------------------------------------------------"
        print "Health:", self.health
        print "Strength:", self.strength
        print "Defence:", self.defence
        print "Agility:", self.agility

    def agility2(self): # this function is used when we want to extract and test the hero's agility
        return self.agility


class Enemy: #This is the enemy Class and it creates the container for enemy characteristics.
    def __init__(self, charclass, health, strength, defence, agility): # This function creates the enemy's characteristics framework
        self.charclass = charclass
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def agility2(self): # this function is used when we want to extract and test the enemy's agility
        return self.agility

    def showstats(self): # this function is used when we want to display the enemy's stats
        print "Character type:", self.charclass
        print " "
        print "---------------------------------------------------"
        print "Health:", self.health
        print "Strength:", self.strength
        print "Defence:", self.defence
        print "Agility:", self.agility

def WormBeast(): #This Function Defines the Monster WormBeast and populates the Enemy Class with the WormBeast Stats
        global monster
        monster = Enemy('WormBeast', 500, 1, 1, 1)
        return monster

def menu(): # Main Function to display the menu/ accept the users input and redirect to other functions
    print "1) Introduction"
    print "2) Start Game"
    print "3) Credits"
    userinput = input("Enter your Choice: ")
    if userinput == 1:
        #print "Introduction"
        intro()
    elif userinput == 2:
        #print "Start Game"
        startGame()
    #elif userinput == 3: ... more codes here
    else:
        print "You have chosen an invalid choice"

def intro(): #displays the introduction text
    print "You have chosen Introduction"
    raw_input("Press Enter to continue: ")
    menu()

def startGame(): #this function askes the user what kind of hero he want to be and sends the appropriate stats the hero creation class
    #print "Start Game"
    global activeChar
    #global heroType
    #global health
    #global strength
    #global defence
    print "Please choose your character"
    print "1) Ogre"
    print "2) Human"
    choosehero = input("Enter your Choice: ")
    if choosehero == 1:
        #heroType= 'Ogre'
        #health = 150
        #strength = 150
        #defence = 50
        activeChar=Character('Orge', 150, 150, 50, 0) 
        confirmHero()
    if choosehero == 2:
        #heroType= 'Human'
        #health = 200
        #strength = 150
        #defence = 50
        activeChar=Character('Human', 200, 150, 50, 2)
        confirmHero()

def confirmHero(): # this menu confirms the hero type he has chosen and sends the heor to the begining of the journey / beginGame()
    print "You have chosen", activeChar.charclass, ". His strength is", activeChar.strength
    print "To confim character Press <1> to reselect Press <2>"
    choiceChar = input("Enter your Choice: ")
    if choiceChar == 1:
        #print "Begin Game"
        beginGame()
    if choiceChar == 2:
        startGame()

def beginGame(): # gives the user the choice of the areahe want to go to / moon()
    print "Game Begins Here"
    print "Do you want to go to the Moon (Press <1>)"
    print "Do you want to go to Saturn (Press <2>)"
    print "Do you want to go to Mars (Press <3>)"
    choiceLevel = input("Enter your Choice: ")
    if choiceLevel == 1:
        #print "Go to the Moon"
        moon()


def fight(): # initiates Fight Sequence

    import random
    
    global heroRun
    print "This Guy"
    activeChar.showstats()
    print "vs"
    monster.showstats()

    print "Do you want to fight or run?"
    print "Run (1)"
    print "Fight (2)"
    battleInput = input("Enter your Choice: ")
    #if battleInput == 1:
    while battleInput == 1:
        print "You attempt to run"
        raw_input("Toko Tok Tok")
                          
        if activeChar.agility2() > monster.agility2():
            print "You have Run"
            raw_input("Toko Tok Tok")
            moon()
        if activeChar.agility2() < monster.agility2():
            print "Haa Haa you cannot run"
            raw_input("Ha Ha ha")
            fight()



    while battleInput == 2:
        if monster.health >= 0 and activeChar.health >= 0:
            if activeChar.strength > monster.defence:
                HeroNormalDamage = [0,10,20,30,40]
                HeroCriticalDamage = [0,0,0,0,100]
                HeroNormalDamageRandom = random.choice(HeroNormalDamage)
                HeroCriticalDamageRandom = random.choice(HeroCriticalDamage)
                HitCalculator = [1,1,1,1,2]
                randomHitcalculator = random.choice(HitCalculator)

                eNormalDamage = [0,10,20,30,40]
                eCriticalDamage = [0,0,0,0,100]
                eNormalDamageRandom = random.choice(eNormalDamage)
                eCriticalDamageRandom = random.choice(eCriticalDamage)
                    
                if randomHitcalculator == 1:
                    monster.health = monster.health - HeroNormalDamageRandom
                    activeChar.health = activeChar.health - eNormalDamageRandom
                    print "You have hit monster for", HeroNormalDamageRandom, "Damage. You have", activeChar.health, "remaining"
                    print "Monster has hit you for", eNormalDamageRandom, "Damage.Enemy has", monster.health, "remaining"
                    raw_input("WAITWAIT")
                if randomHitcalculator == 2:
                    monster.health = monster.health - HeroCriticalDamageRandom
                    activeChar.health = activeChar.health - eCriticalDamageRandom
                    print "You have critically hit monster for", HeroCriticalDamageRandom, "Damage. You have", activeChar.health, "remaining"
                    print "Monster has critcally Hit you for", eCriticalDamageRandom, "Damage.Enemy has", monster.health, "remaining"
                    raw_input("WAITWAIT")
                
        else:
            battleInput = 0
            if monster.health <= 0:
                print "You have won the battle"
                moon()
            if activeChar.health <=0:
                print "You have lost the battle"
                raw_input("Click to Restart Game")
                menu()

def moon(): # gives the hero the choice of seeking to fight or to go back.
    import random
    print "Your", activeChar.charclass, "character has reached the moon"
    print "Do you want to hunt for Monsters (Press <1>)?"
    print "Do you want to go back to earth to select a new planet to go to (Press <2>)"
    choiceLevel_Moon = input("Enter your Choice: ")
    if choiceLevel_Moon == 1:
        rand = random.randint(1, 10)
        if rand <= 5:
            print "You met a WormBeast"
            WormBeast()
            raw_input("Press <Enter> to show his stats: ")
            monster.showstats()
            raw_input("Lets Begin Battle")
            fight() #Commence Fight Sequence
        if rand > 5:
            raw_input("You find nothing Press <Enter> to proceed")
            moon()
                       
    if choiceLevel_Moon == 2:
        print "You are now in a rocketjet back to earth"
        raw_input("You have landed on earth press <Enter> to select another planet")
        beginGame() # sends the user back

menu()
