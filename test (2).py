class Character:
    def __init__(self, charClass, health, strength, defence, agility):
        self.heroType = charClass
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def showStats(self):
        print "Character type:", self.heroType
        print "==========================================================="
        print "Health:", self.health
        print "Strength:", self.strength
        print "Defence:", self.defence
        print "Agility:", self.agility
        print "==========================================================="

    def agility2(self):
        return self.agility
        

def intro():
    print "This story to typing here."
    raw_input("Preess <ENTER> to continue.")
    menu()

def confirmHero():
    print "Hahaha!!!"
    activeChar.showStats()
    print "To confirm the character you are chosing press <1> to reselect press <2>"
    choiceChar = input("Enter your choice: ")
    if choiceChar ==1:
        print "Begin the game"
        menu()
    if choiceChar ==2:
        startGame()
    else:
        print "You have entered an worng value."

def startGame():
    global activeChar

    print "Please select your character:"
    print "1) Swordman"
    print "2) Magician"
    print " "
    print "==========================================================="
    chooseHero = input("Enter your choice: ")
    if chooseHero ==1:
        activeChar = Character('Swordman', 150, 150, 100, 50)
        confirmHero()
    if chooseHero ==2:
        activeChar = Character('Magician', 75, 80, 50, 150)
        confirmHero()
    
def conExit():
    print "Do you would like to exit the game?"
    print "1) Yes"
    print "2) No"
    userExitInput = input("Enter your choice: ")
    if userExitInput ==1:
        print "==========================================================="
        print "Good Bye, I hope to see you again."
        raw_input("Press <ENTER> to exit")
        quit()
    elif userExitInput ==2:
        menu()

def menu():
    print "==========================================================="
    print "||                                                       ||"
    print "||                    Welcome to Python                  ||"
    print "||                                                       ||"
    print "==========================================================="
    print "1) Introduction"
    print "2) Start Game"
    print "3) Credits"
    print " "
    print "9) Quit"
    print "==========================================================="
    userMenuInput = input("Enter your choice: ")
    if userMenuInput ==1:
        print "==========================================================="
        intro()
    elif userMenuInput ==2:
        print "==========================================================="
        startGame()
    elif userMenuInput ==3:
        print "==========================================================="
        credit()
    elif userMenuInput ==9:
        print "==========================================================="
        conExit()
    else:
        print "You have entered an wrong choice"

menu()
