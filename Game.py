class character:
    def __init__(self, charClass, health, defence, strength, agility, dexterity, luck, exp):
        self.heroType = charClass
        self.heal = health
        self.defe = defence
        self.str = strength
        self.agi = agility
        self.dex = dexterity
        self.luk = luck
        self.exp = exp

    def showStats(self):
        print "============================================================"
        print "Character Type:", self.heroType
        print "============================================================"
        print "EXP:", self.exp
        print "Health:", self.heal
        print "Defence:", self.defe
        print "Strength:", self.str
        print "Agility:", self.agi
        print "Dexterity:", self.dex
        print "Luck:", self.luk
        print "============================================================"
        
    def showStats2(self):
        print "=========================================================================="
        print "  #####                           #####                                   "
        print " #     # #    #   ##   #####     #     # #####   ##   ##### #    #  ####  "
        print " #       #    #  #  #  #    #    #         #    #  #    #   #    # #      "
        print " #       ###### #    # #    #     #####    #   #    #   #   #    #  ####  "
        print " #       #    # ###### #####           #   #   ######   #   #    #      # "
        print " #     # #    # #    # #   #     #     #   #   #    #   #   #    # #    # "
        print "  #####  #    # #    # #    #     #####    #   #    #   #    ####   ####  "
        print "=========================================================================="
        print "This is your", hero.heroType, "status."
        print "=========================================================================="
        print "EXP:", self.exp
        print "Health:", self.heal
        print "Defence:", self.defe
        print "Strength:", self.str
        print "Agility:", self.agi
        print "Dexterity:", self.dex
        print "Luck:", self.luk
    print "==========================================================================="
        
    def agility2(self):
        return self.agi

    def exp2(self):
        return self.exp

class Enemy:
    def __init__(self, charClass, health, defence, strength, agility, dexterity, luck, exp):
        self.eType = charClass
        self.heal = health
        self.defe = defence
        self.str = strength
        self.agi = agility
        self.dex = dexterity
        self.luk = luck
        self.exp = exp

    def showStats(self):
        print "============================================================"
        print "Monster type:", self.eType
        print "============================================================"
        print "EXP:", self.exp
        print "Health:", self.heal
        print "Defence:", self.defe
        print "Strength:", self.str
        print "Agility:", self.agi
        print "Dexterity:", self.dex
        print "Luck:", self.luk
        print "============================================================"

    def agility2(self):
        return self.agi

def Pick_Pick():
    global monster
    monster = Enemy('Pick Pick', 20, 1, 2, 1, 1, 1, 20)
    return monster

def Rock_coco():
    print " "
def ButterQueen():
    print " "
def UDan():
    print " "
def intro():
    print "This is where the place you can place the story here."
    raw_input ("Press <ENTER> return to menu.")
    print "lkdshflsfjs;lkf;ja"
    raw_input ("Press <ENTER> return to menu.")
    inputIntro()

def inputIntro():
    print "============================================================"
    print "Do you want to play the game?"
    print "1) Yes, I would like to play the game."
    print "2) No, I would like to go to Main Menu."
    print "============================================================"
    introInput = input("Enter your choice: ")
    if introInput ==1:
        print "============================================================"
        gameStart()
    elif introInput ==2:
        print "============================================================"
        menu()
    else:
        print "============================================================"
        print "You entered the wrong value. Please enter the value again."
        inputIntro()
        
def field_Fight():
    import random
    global heroRun
    
    print "  _______  __         __     __   "
    print " |   _   ||__|.-----.|  |--.|  |_ "
    print " |.  1___||  ||  _  ||     ||   _|"
    print " |.  __)  |__||___  ||__|__||____|"
    print " |:  |        |_____|             "
    print " |::.|                            "
    print " `---'                            "
    print " "

    hero.showStats()
    print " ____   ____   ______   "
    print "|_  _| |_  _|.' ____ \  "
    print "  \ \   / /  | (___ \_| "
    print "   \ \ / /    _.____`.  "
    print "    \ ' /    | \____) | "
    print "     \_/      \______.' "
    monster.showStats()

    print "Your", hero.heroType, "have two way to choose."
    print "1) Run"
    print "2) Fight"
    print "=========================================================="
    fieldbattleInput = input("Enter your choice: ")
    if fieldbattleInput ==1:
        print "You attempt to run"
        raw_input("Tik Tok Tik Tok Tik Tok")

        if hero.agility2() > monster.agility2():
            print "You have Run"
            raw_input("Run of your life!!!")
            field()
        if hero.agility2() < monster.agility2():
            print "Oh!!! You can't run away."
            raw_input("Ha ha ha !!!")
            fight()

    while fieldbattleInput ==2:
        if monster.heal >= 0 and hero.heal >=0:
            HeroNormalDamage = [10,20,30,40,50]
            HeroCriticalDamage = [0,0,100,100]
            HeroNormalDamageRandom = random.choice(HeroNormalDamage)
            HeroCriticalDamageRandom = random.choice(HeroCriticalDamage)
            HeroTotalNormalDamage = HeroNormalDamageRandom * (hero.str + hero.dex)
            HeroTotalCriticalDamage = HeroCriticalDamageRandom * (2 * (hero.str + hero.dex))

            eNormalDamage = [0,10,20,30,40,50]
            eCriticalDamage = [0,0,0,100,100]
            eNormalDamageRandom = random.choice(eNormalDamage)
            eCriticalDamageRandom = random.choice(eCriticalDamage)
            eTotalNormalDamage = eNormalDamageRandom * (hero.str + hero.dex)
            eTotalCriticalDamage = eCriticalDamageRandom * (2 * (hero.str + hero.dex))

            HitCalculator = [1,1,1,1,2]
            randomHitCalculator = random.choice(HitCalculator)

            HeroDefence = [0,10,20,30,40,50,60,70,80,90,100]
            HeroDefenceRandom = random.choice(HeroDefence)
            HeroTotalDefence = HeroDefenceRandom * hero.defe

            eDefence = [0,10,20,30,40,50,60,70,80,90,100]
            eDefenceRandom = random.choice(eDefence)
            eTotalDefence = eDefenceRandom * monster.defe
            
            if randomHitCalculator ==1:
                
                if HeroTotalNormalDamage < eTotalDefence:
                    HTND = 0
                if HeroTotalNormalDamage > eTotalDefence:
                    HTND = HeroTotalNormalDamage - eTotalDefence
                                
                if eTotalNormalDamage < HeroTotalDefence:
                    ETND = 0
                if eTotalNormalDamage > HeroTotalDefence:
                    ETND = eTotalNormalDamage - HeroTotalDefence
                monster.heal = monster.heal - HTND
                hero.heal = hero.heal - ETND
                print "You have hit monster for", HeroTotalNormalDamage, \
                "Damage. But the", monster.eType, "have", eTotalDefence,"You have", hero.heal, "remaining"
                print "Monster has Hit you for", eTotalNormalDamage, \
                "Damage. But your", hero.heroType, "have", HeroTotalDefence, "so Enemy has", monster.heal, "remaining"
                raw_input("Wait wait!!!!!")
            if randomHitCalculator ==2:

                if HeroTotalCriticalDamage < eTotalDefence:
                    HTCD = 0
                if HeroTotalCriticalDamage > eTotalDefence:
                    HTCD = HeroTotalCriticalDamage - eTotalDefence

                if eTotalCriticalDamage < HeroTotalDefence:
                    ETCD = 0
                if eTotalCriticalDamage > HeroTotalDefence:
                    ETCD = eTotalCriticalDamage - HeroTotalDefence
                        
                monster.heal = monster.heal - HTCD
                hero.heal = hero.heal - ETCD
                print "You have critically hit monster for", HeroTotalCriticalDamage, \
                "Damage. But the", monster.eType, "have", eTotalDefence,"You have", hero.heal, "remaining"
                print "Monster has critcally Hit you for", eTotalCriticalDamage, \
                "Damage. But your", hero.heroType, "have", HeroTotalDefence, "so Enemy has", monster.heal, "remaining"
                raw_input("Wait wait!!!!!")

        else:
            if monster.heal <=0:
                hero.exp = hero.exp + monster.exp
                
                raw_input ("You win the battle")
                field()
            if hero.heal <=0:
                hero.exp = hero.exp - monster.exp

                raw_input ("You Lose the battle")
                town()

def field():
    print "Now, your", hero.heroType, "is in the field."
    print "============================================================"
    print "What would you like to do next?"
    print "1) Find a monster to hunt"
    print "2) Go back to the town"
    print "============================================================"
    field_Menu = input("Enter your choice: ")
    if field_Menu ==1:
        Pick_Pick()
        print "Your", hero.heroType, "meet a Pick Pick."
        raw_input ("Press <ENTER> to show his status.")
        field_Fight()
    if field_Menu ==2:
        print "                                           "
        print " __        __ U  / \  u  | |     | |/ /    "
        print " \ \      / /  \/ _ \/ U | | u   | ' /     "
        print " /\ \ /\ / /\  / ___ \  \| |/__U/| . \u    "
        print "U  \ V  V /  U/_/   \_\  |_____| |_|\_\    "
        print ".-,_\ /\ /_,-. \    >>  //  \,-,>> \,-.    "
        print " \_)-'  '-(_/ (__)  (__)(__)(__)\.)   (_/  "
        print " "
        raw_input ("Your character is walking to town.")
        town()

    else:
        print "============================================================"
        raw_input ("Sorry, You entered the wrong value. Please enter the value again.")
        print "============================================================"
        field() 

def forest():
    print " "

def desert():
    print " "

def town():
    print "                                                  "
    print "            ####       ####       ###             "
    print "            ####       ####       ###             "
    print "            ####       ####       ###             "
    print "            #########################             "
    print "            #########################             "
    print "            #########################             "
    print "                ##################                "
    print "                ##################                "
    print "                ##################                "
    print "                                                  "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                 ################                 "
    print "                                                  "
    print "              ######################              "
    print "                                                  "
    print "            #########################             "
    print "            #########################             "
    print "            #########################             "
    print "                                                  "
    print "         ################################         "
    print "         ################################         "
    print " "
    print "Now, your", hero.heroType, "is inside the town."
    print "============================================================"
    print "What would you like to do next?"
    print "1) Go to field"
    print "2) Go to forest"
    print "3) Go to desert"
    print "4) To see the character status"
    print " "
    print "9) To end the game and go back to main menu"
    print "============================================================"
    townInput = input("Enter your choice: ")
    if townInput ==1:
        print "                                           "
        print " __        __ U  / \  u  | |     | |/ /    "
        print " \ \      / /  \/ _ \/ U | | u   | ' /     "
        print " /\ \ /\ / /\  / ___ \  \| |/__U/| . \u    "
        print "U  \ V  V /  U/_/   \_\  |_____| |_|\_\    "
        print ".-,_\ /\ /_,-. \    >>  //  \,-,>> \,-.    "
        print " \_)-'  '-(_/ (__)  (__)(__)(__)\.)   (_/  "
        print " "
        raw_input ("Your character is walking to field.........")
        field()
    elif townInput ==2:
        print "                  _       _       _  __    "
        print " __        __ U  / \  u  | |     | |/ /    "
        print " \ \      / /  \/ _ \/ U | | u   | ' /     "
        print " /\ \ /\ / /\  / ___ \  \| |/__U/| . \u    "
        print "U  \ V  V /  U/_/   \_\  |_____| |_|\_\    "
        print ".-,_\ /\ /_,-. \    >>  //  \,-,>> \,-.    "
        print " \_)-'  '-(_/ (__)  (__)(__)(__)\.)   (_/  "
        print " "
        raw_input ("Your character is walking to forest........")
        forest()
    elif townInput ==3:
        print "                  _       _       _  __    "
        print " __        __ U  / \  u  | |     | |/ /    "
        print " \ \      / /  \/ _ \/ U | | u   | ' /     "
        print " /\ \ /\ / /\  / ___ \  \| |/__U/| . \u    "
        print "U  \ V  V /  U/_/   \_\  |_____| |_|\_\    "
        print ".-,_\ /\ /_,-. \    >>  //  \,-,>> \,-.    "
        print " \_)-'  '-(_/ (__)  (__)(__)(__)\.)   (_/  "
        print " "
        raw_input ("Your character is walking to desert........")
        desert()
    elif townInput ==4:
        print "This is your", hero.heroType, "status."
        print "============================================================"
        hero.showStats2()
        raw_input ("Press <ENTER> to continue the game.")
        print "============================================================"
        town()
    elif townInput ==9:
        print "============================================================"
        print "Are you sure that you would like to end the game?"
        print "WARNING: The game is not saveable!"
        print "1) Yes"
        print "2) No"
        endInput = input("Enter your choice: ")
        if endInput ==1:
            print "============================================================"
            print "Good Bye."
            raw_input("Press <ENTER> to exit")
            menu()
        elif endInput ==2:
            town()
        else:
            print "============================================================"
            raw_input ("Sorry, You entered the wrong value. Please enter the value again.")
            print "============================================================"
            town()
    else:
        print "============================================================"
        raw_input ("Sorry, You entered the wrong value. Please enter the value again.")
        print "============================================================"
        town()      

def confirmHero():
    hero.showStats()
    print "To confirm the character you're chosing press <1> to reselect press <2>"
    choiceChar = input("Please enter your choice: ")
    if choiceChar ==1:
        print " ______  _______  ______ _____ __   _      _______ _     _ _______       ______ _______ _______ _______"
        print " |_____] |______ |  ____   |   | \  |         |    |_____| |______      |  ____ |_____| |  |  | |______"
        print " |_____] |______ |_____| __|__ |  \_|         |    |     | |______      |_____| |     | |  |  | |______"
        print "======================================================================================================="
        town()
    elif choiceChar ==2:
        gameStart()
    else:
        print "============================================================"
        print "You entered the wrong value. Please enter the value again."
        print "============================================================"
        confirmHero()

def gameStart():
    global hero
    
    print "Please select your character."
    print "============================================================"
    print "##.............##...........##...........#######..........##"
    print "##...........####...........##..........##.....##.........##"
    print "##.............##...........##.................##.........##"
    print "##.............##...........##...........#######..........##"
    print "##.............##...........##..........##................##"
    print "##.............##...........##..........##................##"
    print "##...........######.........##..........#########.........##"
    print "============================================================"
    print "|| Hero Type: Swordman      || Hero Type: Archer          ||"
    print "|| Health: 200              || Health: 75                 ||"
    print "|| Defence: 6               || Defence: 4                 ||"
    print "|| Strength: 6              || Strength: 4                ||"
    print "|| Agility: 2               || Agility: 5                 ||"
    print "|| Dexterity: 3             || Dexterity: 5               ||"
    print "|| Luck: 2                  || Luck: 5                    ||"
    print "============================================================"
    chooseHero = input("Enter your character no.: ")
    if chooseHero ==1:
        hero = character('Swordman', 200, 6, 6, 2, 3, 2, 0)
        print "=============================================================="
        print "|                    Dj                                      |"
        print "|                   EEDEG                                    |"
        print "|       L          #WWKEE                                    |"
        print "|       G          ,WWKKKW                                   |"
        print "|      Gf           fWKEEE                                   |"
        print "|      DL            WWDDK,                                  |"
        print "|      DG            fGDDDK                                  |"
        print "|     jDG             DEjfL                                  |"
        print "|     LLD            DKiijLG                                 |"
        print "|     GGD            DffttGLE                                |"
        print "|     GDD            LLttjLGE                                |"
        print "|     DED            DLjjtGGG                                |"
        print "|     EE             DGfEWEGW:                               |"
        print "|     DE              KfWfGG#K                               |"
        print "|     ED              fLjLGGj#                               |"
        print "|    .ED              LEKELGi#DDDGDGG                        |"
        print "|     EL              E#LKGGjEGDDLGGDKD                      |"
        print "|     D:              EEDEfLKGDDEGGDGDED                     |"
        print "|     D             ttDGKEGKDDDDGGGDDDDKE                    |"
        print "|     D            jfjEWKWW#LLfLGLfWEEGDWE                   |"
        print "|     D           tifKitfLLDDEGGGDDGfL#EDWi                  |"
        print "|   LGEE         ;;tEGijDDGLGLLfGGGGDGj#DDK                  |"
        print "|   Etfj:       i;tLEKLLGLffffffLfLLDEDf#KK,                 |"
        print "|    jDEGDLDGD  itLGGGDffjiitjjtfLLGGDDDf#EE                 |"
        print "|   ttEKDGDGfffjtGGL,Gfjjtj;tttjtfGLLDGDGf#E                 |"
        print "|   WDEEDWEEfEtjGGLfGLLjft;,iLjtffffLGGDDGDKK                |"
        print "|   .;D  .#GKLffLK GGjj;f;f;,ttG;fjfGLKDGDGKK                |"
        print "|           K;fi  ;Lfi,.: .::ijtfjjjGDGLDDDjE                |"
        print "|                 fGji.:;.D;;,LfDt;LfLGDGEELE,               |"
        print "|                 GDj,,.:,;:,DE,iiLjLfGGGDDGGE               |"
        print "|                ;jGi,:.;tjiGt,L;jLGGGLLGGDDLE               |"
        print "|                jfGG,t;i,j:,fL:,tfffGLELGDDLE               |"
        print "|                iEDGtiDi;j:,jEi;tjjjffLLGDEEKi              |"
        print "|                fGGfitt;i,DL,LD,DDGLLEDGEKEEGE              |"
        print "|                jLLf,jjitjGfiD;,tjftLLLGDEKEGE              |"
        print "|                jGfftjjjLtiGLjDiiLjtGLEDGDDELE.             |"
        print "|                LDfftt,jjtiGj,GLEGtffLGGGDDEDEK             |"
        print "|                fDLGLfffjtjjfttDDjfLGGGGDGDLEEE             |"
        print "|                fGfGGDDDGfjjLLjGjfDLLLGDDDEDEEE             |"
        print "=============================================================="
        confirmHero()
    elif chooseHero ==2:
        hero = character('Archer', 75, 4, 4, 5, 5, 5, 0)
        print "=============================================================="
        print "|                               .,DjDD                       |"
        print "|                               ;LtiiD                       |"
        print "|                              .:D  tG                       |"
        print "|                              :iDG ,G                       |"
        print "|                               tGD .G                       |"
        print "|                               ,tLLEDt                      |"
        print "|                                :iDEDG                      |"
        print "|                                 DDGEEG                     |"
        print "|                               :DDj,iGG                     |"
        print "|                             :Dft   tG:G                    |"
        print "|                          ;Gt;       iD:G,                  |"
        print "|                         ,Dti        ,iiEL                  |"
        print "|                        ;Dt;          if:G                  |"
        print "|                     ..ttj:           i;;G:                 |"
        print "|                    .G;D.              ,G;L                 |"
        print "|                   tEfD;                ,;L                 |"
        print "| LfjLfjGG:GL    ,EDj.                   ifiGG,              |"
        print "| ,DGDEDDDDGDi. fGGt.                    ,:tGGitt            |"
        print "|  LGLGDtDDiGE;DtGfi                     .;iGG;;,;;it        |"
        print "|  .GDfDDGGEGDDGEfjf.                    .;iGGtDDDG D ,;     |"
        print "|    ii:Di.:j;GijffLLfffLDDDDDEDDDDDDGGGGLjtGGtGLGGDGEDDKEEf |"
        print "|   jtLDGtGGjjLfjLff                      ijGEjEELffjti      |"
        print "|   DfEGfDfLifii LtL                      ttDEjffjji         |"
        print "|  G,iLjDLEGt;   ;Dit                    :ftGKii             |"
        print "|  DLL  L G.L     Lftj                   iGfDKi              |"
        print "|                    f:Ei               tEEK                 |"
        print "|                     LjL;              ijLE                 |"
        print "|                         jEt         ifEE                   |"
        print "|                           DEt      ;fEK                    |"
        print "|                            EEG    tGtG                     |"
        print "|                              DEjttGED                      |"
        print "|                               ,EjLfK                       |"
        print "|                                jGfEG                       |"
        print "|                               tffED                        |"
        print "|                               i;t Ei                       |"
        print "|                              ;DG  fG                       |"
        print "|                              ;GE  ,D                       |"
        print "|                              tDDj,ED                       |"
        print "|                               ;DEDKD                       |"
        print "=============================================================="
        confirmHero()
    else:
        print "============================================================"
        raw_input ("Sorry, You entered the wrong value. Please enter the value again.")
        print "============================================================"
        gameStart()

def credits():
    print "This is the place that you can write the credits here."
    raw_input ("Press <Enter> return to menu")
    menu()

def conExit():
    print "============================================================"
    print "Do you would like to exit the game?"
    print "1) Yes"
    print "2) No"
    userExitInput = input("Enter your choice: ")
    if userExitInput ==1:
        print "============================================================"
        print "Good Bye, I hope to see you soon."
        raw_input("Press <ENTER> to exit")
        quit()
    elif userExitInput ==2:
        menu()
    else:
        print "============================================================"
        raw_input ("Sorry, You entered the wrong value. Please enter the value again.")
        conExit()
    
def menu():
    print "============================================================================================================================================"
    print ">======>               >=>                                       >=>       >=>               >=>                                        >=> "
    print ">=>    >=>             >=>   >=>                                 >> >=>   >>=>               >=>  >>                                    >=> "
    print ">=>    >=> >=>   >=> >=>>==> >=>         >=>     >==>>==>        >=> >=> > >=>   >==>        >=>       >==>    >=>     >=>    >=> >=>   >=> "
    print ">======>    >=> >=>    >=>   >=>>=>    >=>  >=>   >=>  >=>       >=>  >=>  >=> >>   >=>   >=>>=> >=> >>   >=>   >=>   >=>   >=>   >=>   >=> "
    print ">=>           >==>     >=>   >=>  >=> >=>    >=>  >=>  >=>       >=>   >>  >=> >>===>>=> >>  >=> >=> >>===>>=>   >=> >=>   >=>    >=>   >=> "
    print ">=>            >=>     >=>   >>   >=>  >=>  >=>   >=>  >=>       >=>       >=> >>        >>  >=> >=> >>           >=>=>     >=>   >=>   >=> "
    print ">=>           >=>       >=>  >=>  >=>    >=>     >==>  >=>       >=>       >=>  >====>    >=>>=> >=>  >====>       >=>       >==>>>==> >==> "
    print ">=>                                                                                                                                         "
    print "============================================================================================================================================"
    print "1) Introduction"
    print "2) Start Game"
    print "3) Credits"
    print " "
    print "9) Quit the game"
    print "============================================================"
    homeInput = input("Enter your Choice: ")
    if homeInput ==1:
        print "============================================================"
        intro()
    elif homeInput ==2:
        print "============================================================"
        gameStart()
    elif homeInput ==3:
        print "============================================================"
        credits()
    elif homeInput ==9:
        conExit()
    else:
        print "============================================================"
        raw_input ("Sorry, you entered a wrong choice. Please enter the value again.")
        menu()

menu()
