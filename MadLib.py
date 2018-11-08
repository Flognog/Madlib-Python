import random



#Lists
adj_list = []
nat_list = []
name_list = []
noun_list = []
pnoun_list = []
num_list = []
shape_list = []
food_list = []
game_list = []
verbing_list = []
plant_list = []
place_list = []
partofbody_list = []
adverb_list = []

def whichstory():
    checker = True
    while checker == True:
        story = input("Which Story? 1, 2, 3 or 4 for random: ")
        if story == 1:
            checker = False
            story_one()
            printer_one()
            break
        elif story == 2:
            checker = False
            story_two()
            printer_two()
            break
        elif story == 3:
            checker = False
            story_three()
            printer_three()
            break
        elif story == 4:
            checker = False
            randomstory = random.randint(1,3)
            if randomstory == 1:
                story_one()
                printer_one()
                break
            elif randomstory == 2:
                story_two()
                printer_two()
                break
            elif story == 3:
                story_three()
                printer_three()
                break
            else:
                print "Critical Randomizer Error"
            
            
        else:
            print "Invalid entry"

def playagain():
    playagain = raw_input("Would you like to play again? Y/N")
    playagain = str.upper(playagain)
    if playagain == "Y":
        whichstory()
    elif playagain == "N":
        quit()
    else:
        print "Invalid Entry"
        playagain()
def adjective():
    adj = raw_input("Pick an adjective: ")
    adj = str.upper(adj)
    adj_list.append(adj)
    
def adverb():
    adverb = raw_input("Pick an Adverb:")
    adverb = str.upper(adverb)
    adverb_list.append(adverb)
 
def nationality():
    nat = raw_input("Pick a nationality: ")
    nat = str.upper(nat)
    nat_list.append(nat)
    
def name():
    name = raw_input("Pick a name: ")
    name = str.upper(name)
    name_list.append(name)

def noun():
    noun = raw_input("Pick a noun: ")
    noun = str.upper(noun)
    noun_list.append(noun)

def pnoun():
    pnoun = raw_input("Pick a plural noun: ")
    pnoun = str.upper(pnoun)
    pnoun_list.append(pnoun)

def number():
    number = raw_input("Pick a number: ")
    number = str.upper(number)
    num_list.append(number)
    
def shape():
    shape = raw_input("Pick a shape: ")
    shape = str.upper(shape)
    shape_list.append(shape)
    
def food():
    food = raw_input("Pick a food item: ")
    food = str.upper(food)
    food_list.append(food)

def game():
    game= raw_input("Pick a Game: ")
    game = str.upper(game)
    game_list.append(game)
    
def verbing():
    verbing = raw_input("Pick a verb ending in ING: ")
    verbing = str.upper(verbing)
    verbing_list.append(verbing)
    
def plant():
    plant = raw_input("Pick a plant: ")
    plant = str.upper(plant)
    plant_list.append(plant)

def partofbody():
    pob = raw_input("Pick a body part: ")
    pob = str.upper(pob)
    partofbody_list.append(pob)
    
def place():
    place = raw_input("Pick a place: ")
    place = str.upper(place)
    place_list.append(place)

def story_one():
    print " "
    adjective()
    adjective()
    adjective()
    adjective()

    nationality()
    
    name()
    
    noun()
    noun()
    noun()
    
    pnoun()
    
    number()
    number()
    
    shape()
    
    food()
    food()

def story_two():
    print " "
    adjective()
    adjective()
    adjective()
    
    noun()
    noun()
    noun()
    
    pnoun()
    pnoun()
    pnoun()
    pnoun()
    
    game()
    
    number()
    
    verbing()
    verbing()
    verbing()
    verbing()
    
    plant()
    
    place()
    
    partofbody()
 
def story_three():
    print " "
    pnoun()
    pnoun()
    
    verbing()
    verbing()
    verbing()
    
    noun()
    noun()
    noun()
    noun()
    noun()
    
    partofbody()
    partofbody()
    partofbody()
    partofbody()
    
    adverb()
               
def printer_one():
    print " "
    print "Pizza was invented by a %s %s" % (str.upper(adj_list[0]), str.upper(nat_list[0]))
    print "chef named %s. To make a pizza, you need" % (str.upper(name_list[0]))
    print "to take a lump of %s, and make a thin, round" % (str.upper(noun_list[0]))
    print "%s %s. Then you cover it with" % (str.upper(adj_list[1]), str.upper(noun_list[1]))
    print "%s sause, %s cheese, and fresh" % (str.upper(adj_list[2]), str.upper(adj_list[3]))
    print "chopped %s. Next you have to bake it in a very" % (str.upper(pnoun_list [0]))
    print "hot %s. When its done, cut it into %s" % (str.upper(noun_list[2]), str.upper(num_list[0]))
    print "%s. Some kids like %s pizza the" % (str.upper(shape_list[0]), str.upper(food_list[0]))
    print "best, but my favorite is the %s pizza. If i could," % (str.upper(food_list[1]))
    print "would eat pizza %s times a day!" % (str.upper(num_list[1]))
    
def printer_two():
    print " "
    print "A vacation is when you take a trip to some %s place" % (str.upper(adj_list[0]))
    print "with your %s family. Usually you go to some place" % (str.upper(adj_list[1]))
    print "that is near a.an %s or up on aan %s." % (str.upper(noun_list[0]), str.upper(noun_list[1]))
    print "A good vacation place is one where you can ride %s" % (str.upper(pnoun_list[0]))
    print "or play %s or go hunting for %s. I like" % (str.upper(game_list[0]), str.upper(pnoun_list[1]))
    print "to spend my time %s or %s." % (str.upper(verbing_list[0]), str.upper(verbing_list[1]))
    print "When my parents go on a vacation, they spend there time eating" 
    print "three %s a day, and fathers play golf, and mothers" % (str.upper(pnoun_list[2]))
    print "sit around %s. Last summer, my little brother" % (str.upper(verbing_list[2]))
    print "fell in a/an %s and got poison %s all" % (str.upper(noun_list[2]), str.upper(plant_list[0]))
    print "over his %s. My family is going to go to (the)" % (str.upper(partofbody_list[0]))
    print "%s, and i will practice %s. Parents" % (str.upper(place_list[0]), str.upper(verbing_list[3]))
    print "need vacations more than kids do because parents are always very"
    print "%s and because they have to work %s" % (str.upper(adj_list[2]), str.upper(num_list[0]))
    print "hours every day all year making enough %s to pay" % (str.upper(pnoun_list[3]))
    print "for the vacation."

def printer_three():
    print " "
    print "I was home alone and scared out of my %s. I could hear" % (pnoun_list[0])
    print "the wind %s, and off in the distance a/an %s" % (verbing_list[0], noun_list[0])
    print "was howling. I crossed the room, locked the %s, and" % (noun_list[1])
    print "climbed into bed, pulling the %s over my %s." % (pnoun_list[1], partofbody_list[0])
    print "Then it happened. I could hear a/an %s %s" % (noun_list[2], verbing_list[1])
    print "up the stairs. My %s started to chatter and my knees" % (partofbody_list[1])
    print "began %s. The %s was the thrust" % (verbing_list[2], noun_list[3])
    print "open and there was a huge %s with hair all over his" % (noun_list[4])
    print "%s. It was my father. 'Hi, were home' he said %s" % (partofbody_list[2], adverb_list[0])
    print "'Hope you werent afraid of staying hmome alone.'" 
    print "'No,' I said, lying through my %s." % (partofbody_list[3])
    
    
whichstory()
