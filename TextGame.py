#matthew walker
#10/18
#text game
import sys

#creating a function to ask questions so that I dont have to sloog through nested if statements
def askquestion(question,op1 = "",op2 = "",op3 = ""):
    response = input(question).lower()
    option = op1 + op2 + op3
    option = option.lower()
    while response not in option:
        response = input(question).lower()
    return response

def start():
    print("slowly the wolf stocks toward you. you see salyva dripping from its fangs, you see the fire in its eyes, the killer instinct the ruthlesness.")
    print("you awake in a cold sweat and only a vague recelection of the dream. you slide out of bed and activate the morning program of your house.")
    print("the year is 9034 and humans have advanced in technology significantly. You have come to xanther4 hunting a werewolf.")
    print("you glance at the wall where your gun case is. inside you know is a pistol that shoots silver bullets and a silver sword that is masterfully crafted.")
    print("the society you live in has almost completly forgotten the old legends and myths like that of the werewolf.")
    print("quickly you eat your breakfast and go to head outside to find clues.")

    choice = askquestion("do you take your weapons with you yes/no","yes","no","leave")
    if choice == "yes":
        choice1()
    elif choice == "no":
        choice2()
    elif choice == "leave":
        end5()
    else:
        start()


def choice1():
    print("""
                                                  &&
                                                    &&
 ______________________________________,___________&&&&              &
/__________________________________________________&@@@@@@@@@@@@@@@@&&}
\______________________________________ ___________&@@@@@@@@@@@@@@@@&&}
                                       `           &&&&              &
                                                    &&
                                                    &&
                                                  &&


    
                    n-._
                   M//  \
                  ///L_/_)
                 /////y|||
                / 78)/| ||
               / /""  \_/
              / /
             n /
            (O)
    """)
    print("you realize that the possble pay off of defeating your quarry outways the risk of discovery. walking over to the cabinet you take out the gun and")
    print("sword strapping them on and filling the gun belt with spair bullets. As you walk outside into the darkness of the planet you go over in your mind what you know")
    print("you landed on this planet a week ago. upon your arrivel you heard that several people had been murderd and that a huge monster had killed them.")
    print("when you had created a false full moon you had been able to detect howling on your houses adio range scanner. according to the scanner the howling had been detected")
    print("to the south west. But you knew that no one lived over ther and you would rather find the werewolf in human form. the only other clue you had")
    print("was the fact that to the east there lived what the colonists called 'a crazy old man who eats raw meat' this sounded promising since werewolves tended to eat raw meat in human or wolf form")

    choice = askquestion("do you go southwest/east","east","southwest")
    if choice == "east":
        choice4()
    elif choice == "southwest":
        choice5()
    else:
        choice1()

    


def choice2():
    print("you decide that its best not to scare anyone by carrying weapons. As you walk outside into the darkness of the planet you go over in your mind what you know")
    print("you landed on this planet a week ago. upon your arrivel you heard that several people had been murderd and that a huge monster had killed them.")
    print("when you had created a false full moon you had been able to detect howling on your houses adio range scanner. according to the scanner the howling had been detected")
    print("to the south west. But you knew that no one lived over ther and you would rather find the werewolf in human form. the only other clue you had")
    print("was the fact that to the east there lived what the colonists called 'a crazy old man who eats raw meat' this sounded promising since werewolves tended to eat raw meat in human or wolf form")
    print("so two clues however without a weapon it would be foolish to try and chase a werewolf so there is no point in going southwest. instead you may try and ask around")
    print("for more clues or check out the old guys house.")

    choice = askquestion("do you ask/east","ask","east")
    if choice == "ask":
        choice3()
    elif choice == "east":
        choice4()
    else:
        choice2()


def choice3():
    print("you decide that you need more information. you press a button on your suit and your speeder immadiatly comes to you from beside the house. Mounting")
    print("it you speed of towards the village and make it in a matter of minutes. dismounting you take in the scene. A small group of metalic sepheres some with")
    print("garden extensions others with garages. But all with the same basic spherical shape. you approach the closest house but on your way to it your eye catches")
    print("something strange on the side of the house that is almost facing away from you.")

    choice = askquestion("do you investigate/ignore","investigate","ignore")
    if choice == "investigate":
       end3()
    elif: choice == "ignore":
        end4()
    else:
        choice3()
        

def choice4():
    print("you press a button on your suit and immediatly your speeder comes from around the side of the house. Mounting it you speed off toward the east.")
    print("after 5 minutes of racing along the rough red and green terrain of xanther4 you see in the distance a small shack made out of what appears to be wood.")
    print("this puzzles you slightly as this planet didnt seem to have any forests and no one used actuall wood anymore. everyones house also doubled as their")
    print("space craft. As you pull up in front of the house you make quick note of the fact that this house seems to have no power source. After checking your")
    print("scanner you head up to the door, the scanner showed no sign of biological life this however you knew could be decieving as werewolves dont give off redable")
    print("biosignitures. slowly you approch the door and push it gently open. it is stiff but swings in after a little effort. the squeak that emmites from the door breaks")
    print("the deffining silence that surounds this place. As you step inside you here a noise above you in the attic. upon investigating the house you find a trap door leading")
    print("to the attic, but in the living room you find a strange looking statue.")

    choice = askquestion("do you look statue/look attic","look statue","look attic")
    if choice == "look statue":
        choice6()
    elif choice == "look attic":
        choice7()
    else:
        choice4()
    

def choice5():
    print("you press a button on your suit and immediatly your speeder comes from around the side of the house. mounting it you speed off toward the southwest.")
    print("as you go you glance at your speeders radar and notice something strange about the landscape but you arent sure if you should stop and check it out,")
    print("keep going and ignore it or keep going and try and figure out what it is by just looking at your radar.")

    choice = askquestion("do you stop/ignore/watch radar","stop","ignore","watch radar")
    if choice == "stop":
        choice10()
    elif choice == "ignore":
        choice11()
    elif choice == "watch radar":
        end1()
    else:
        choice5()

def choice6():
    print("""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||###|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||###########|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||###############|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||#################||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||###################|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||#################||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||###############|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||###########|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||###|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||#|||||||||||#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||(##||#||||(#||##)||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||(*#####)|||||(#####*)||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||(######)|||||||(######)|||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||(#######)|||||||(#######)||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||(########)|||||||(########)|||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||(#########)|||||||||(#########)|||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||(#########)|(##)|||||||(##)|(#########)|||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||(########)|||(##)|||||||(##)|||(########)||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||(#########)|||(##)|||||||(##)|||(#########)|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||****#####(#########)|||(##)|||||||(##)|||(#########)#####****||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    """)
    print("the statue looks like two wolves howling at the moon. the moon part of the statue seems to be giving off a weird kind of light.")
    print("as you stare at it you start feeling nuasiated and strange images start flashing through your mind. Images start flashing through your mind")
    print("images of fire blood and death and in these images comes the realization that you are killing people...and eating them. though gruesome")
    print("the images start feeling attractive.")

    choice = askquestion("do you try to leave/stare","leave","stare")
    if choice == "leave":
        choice8()
    elif choice == "stare":
        end2()
    else:
        choice6()

def choice7():
    print("you decide that the statue can wait and instead move to the trap door slowly you pull the trap door down and head up the stairs.")
    print("as you enter the attic you can see an old man facing away from you shuddering violently. Behind and to your left you sense a light.")
    print("you glance back at the light to see where its coming from. you see the same statue as you noticed in the living room. It looks like")
    print("two wolves howling at the moon. The light comes from the moon section of the statue. hearing a growl you jerk back around to see that")
    print("the old man is no longer there and that in his place a great werewolf stands growling. As soon as your eyes lock it springs toward you")

    choice = askquestion ("do you go for your gun/sword","gun","sword")
    if choice == "gun":
        end6()
    elif choice == "sword":
        end7()
    else:
        choice7()
        
    

def choice8():
    print("As you pull away you feel as though a massive part of yourself is pulled yout of you and the rage from the statue is stuffed in")
    print("suddenly you fall to the ground shaking violently. You feel hair start sprouting all over your body, your teeth get longer and sharper")
    print("your sense of smell increases. You feel yourself losing your mind. Next to the statue you saw a silver dagger.")

    choice = askquestion("do you use the dagger/don't","dagger","don't")
    if choice == "dagger":
        end8()
    elif choice == "don't":
        end9()
    else:
        choice8()

def choice9():
    print("""
as you speed down the canyon you suddenly see a giant figure land in front of you. fearing its a human you stop rapidly with your bike turned sideways
the canyon floor is thin and you bike takes up nearly the entire width. You see that the figure you stopped for is actually exactly what you hunting for.
it seems it found you first.
""")
    choice = askquestion("do you fight/run","fight","run")
    if choice == "fight":
        end14()
    elif choice == "run":
        end 15()
    else:
        choice9()

def choice10():
    print("""
you decide to stop and get a closer look. the first thing you notice is that the radar shows the land from the top down looking like two wolves howling at the moon
You stop your speeder and get off. slowly you look around. Above you tower giant rock pillars
as you look around you here a sound above you. Looking up you see a dark figure far above you.
""")

    choice = askquestion("do you attack the figure with your gun/sword/leave","gun","sword","leave")
    if choice == "gun":
        end10()
    elif choice == "sword":
        end11()
    elif choice == "leave":
        end12()
    else:
        choice10()

def choice11():
    print("""
you figure its probably nothing and speed on. for nearly an hour you speed through the canyons and over the hills. Eventually, while you
are in a deep canyon you are presented with going left or right.
""")
    choice = askquestion("do you go left/right","left","right")
    if choice == "left":
        choice9()
    elif choice == "right":
        end13()
    else:
        choice11()






def end1():
    print("""
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||#####||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||###########|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||###############|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||#################||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||###################|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||#################||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||###############|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||###########|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||#####||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||#|||||||||||#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||(##||#||||(#||##)||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||(*#####)|||||(#####*)||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||(######)|||||||(######)|||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||(#######)|||||||(#######)||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||(########)|||||||(########)|||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||(#########)|||||||||(#########)|||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||(#########)|(##)|||||||(##)|(#########)|||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||(########)|||(##)|||||||(##)|||(########)||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||(#########)|||(##)|||||||(##)|||(#########)|||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||****#####(#########)|||(##)|||||||(##)|||(#########)#####****||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    """)
    print("""as you watch your raddar you realize that the landscape looks like two wolves howling at the moon. This seems incredibly puzzling,
and frightning. there is no way that is a natrual formation this planet must have been home to cultists at some point suddenly
your collision warner bleeps. You look up just in time to see a giant piller right in front of you. You attempt to dodge but its
to late as the world blacks out your last thought is of how those stupid dont text and drive posters from the 2000s were true(: ....YOU DIED.""")
    input("press enter to end")
    sys.exit()

def end2():
    print("ascii art")
    print("""
as you continue to gaze at the moon you here a sound behind you. you try to turn around to see what it is but realize you cant move a muscle!
the sound gets closer and closer then an old man says "hey what are you doing in here?" you try to respond but cant say anything.
"what are you looking at?"he says. you attempt to wave your arm to tell him to get away but he walks over beside you. as soon as his face
is within line of site of the fake moon you here him snarl and snort. out of the corner of your eye you see him fall to the ground thrashing.
to your horror he starts sprouting hair all over his body. slowly his teeth and nose get longer and his arms and legs transform into the much more
slender legs of a wolf. his body swells getting large enough to rip his shirt of. slowly the thrashing dies down and as it does you find you are starting
to get your movement back. you turn your head and look at the wolf that now lies next to you. slowly you start to back away angling for the door.
you are within a few paces of the door you turn to find the handle... but it is a fatel mistake. as soon as you turn away from the wolf it lunges of
the ground and with a single bound is on top of you. you try for a weapon but its too late. the last thing you here is the wolf snarling and the last you see is its fangs.....YOU DIED.
""")
    input("press enter to end")
    sys.exit()

def end3():
    print("""
As you walk around the side of the house you see a dark figure. At first you think its just a nother human but to late you realizeits a werewolf.
As it leaps toward you you think back to what you had seen now you realize what it realy was....claw marks... your screams are unheard as the
werewolf eliminates you.......YOU DIED
""")
    input("press enter to end")
    sys.exit()

def end4():
    print("""
you ignore it whatever it was. as you enter the house you see a man comming in from outside. upon seeng you his face darkens. "what do you want
werewolf hunter?" "im look for clues you say". "we dont want you around mr you need to leave now!". as the man talks you see him get more and
more angry. As he looks at you now you see a killer look in his eye. you realize all to well that you are unarmed. Slowly you back away to the door
and leave. after getting back on your speeder you realize that this is probably a waste of your time you speed back to you house and leave the planet
in search of better hunting grounds......YOU SURVIVED
""")
    input("press enter to end")
    sys.exit()

def end5():
    print("ascii art")
    print("""
suddenly you decide you dont really wanna be here............................... BYE!
""")
    input("press enter to end")
    sys.exit()

def end6():
    print("ascii art")
    print("""
you go for your gun. pulling it out and trying to aim it. but you are to slow as you try to pull the trigger the werewolf knocks it from you hand
then shoves you down the stairs. as you land on the floor beneath you hear it try an pounce on you. as quickly as you can you make for the door. but
the wolf is faster and catches you a short ways before you make it.........YOU DIED.
""")
    input("press enter to end")
    sys.exit()

def end7():
    print("ascii art")
    print("""
realizing you are in close courters you draw your sword. the wolf lunges at you but just before impact you get your blade pointed at it. it
slides onto the sword with the sound of flesh and meteal colidding. there is a loud thump as you and the wolf fall to the floor below. quickly you push
it off of you and stand up backing away. The wolf makes a feeble attempt to rise then falls to the ground dead.........YOU KILLED THE WEREWOLF!!
""")

def end8():
    print("ascii art")
    print("""
in an attempt to save the villegers from having two werewolves to deal with you claw your way toward the statue. Rising unsteadely as your legs transform
you reach out with a half human half wolf hand and grab the knife. Closing your eyes you stab yourself in the heart. searing pain shoots through your whole
body and you howl in pain falling back onto the floor you lay their your body goning numb. slowly everything fades to black and you know no more.....YOU DIED
""")
    input("press enter to end")
    sys.exit()

def end9():
    print("ascii art")
    print("""
you decide that the villegers will just have to deal with their own problems. You feel hair start sprouting all over your body, your teeth get longer
and sharper your sense of smell increases. As the transformation continues you feel savage power rising inside you. As you complete your transfromation
you here someone coming down from the attic as you look up another werewolf enters the room ans snarels at you. Rapidly you gauge your opponents strength.
he is old and weak, this should be an easy fight.....due to not being sure on where the school draws the line on combat ima skip the fight scene and go straight
to you being outside. As you leave the wooden shack you feel the thrill of the hunt begin and stalk off in search of other prey..... YOU BACAME A WEREWOLF.
""")
    input("press enter to end")
    sys.exit()

def end10():
    print("""
You pull you gun out and start shooting. you can see you shoots hitting close. then you here a howl. the figure tumbles off of the rock
to late you realize its headed

""")
    input("press enter to end")
    sys.exit()
def end11():
    print("""


""")
    input("press enter to end")
    sys.exit()
def end12():
    print("""


""")
    input("press enter to end")
    sys.exit()
def end13():
    print("""


""")
    input("press enter to end")
    sys.exit()
def end14():
    print("""


""")
    input("press enter to end")
    sys.exit()
def end15():
    print("""


""")
    input("press enter to end")
    sys.exit()



start()

