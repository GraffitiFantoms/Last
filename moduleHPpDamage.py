import random
#from moduleHPm import IfMonster
      #  kickPRNG = IfMonster(rngM) / 5
      #  kickPRNG2 = (kickPRNG / 5) + 3
i = 1
def kickPlayerRNG(rngM):
    if rngM == 1:
        kickPRNG = random.randint(10, 14)

    elif rngM == 2:
        kickPRNG = random.randint(10, 13)
    		
    elif rngM == 3:
        kickPRNG = random.randint(2, 70)

    elif rngM == 4:
        kickPRNG = random.randint(30, 45)

    elif rngM == 5:
        kickPRNG = random.randint(15, 30)

    elif rngM == 6:
        kickPRNG = random.randint(10, 11)

    elif rngM == 7:
        kickPRNG = random.randint(10, 17)

    elif rngM == 8:
        kickPRNG = random.randint(7, 10)

    elif rngM == 9:
        kickPRNG = random.randint(5, 7)

    elif rngM == 10:
            kickPRNG = random.randint(9, 13)

    elif rngM == 11:
        kickPRNG = random.randint(10, 17)

    elif rngM == 12:
        kickPRNG = random.randint(9, 11)

    elif rngM == 13:
        kickPRNG = random.randint(7, 15)

    elif rngM == 14:
        kickPRNG = random.randint(11, 17)

    elif rngM == 15:
        kickPRNG = random.randint(12, 14)

    elif rngM == 16:
        kickPRNG = random.randint(7, 13)

    elif rngM == 17:
        kickPRNG = random.randint(11, 16)

    elif rngM == 18:
        kickPRNG = random.randint(8, 12)

    elif rngM == 19:
        kickPRNG = random.randint(7, 12)

    elif rngM == 20:
        kickPRNG = random.randint(6, 14)

    elif rngM == 21:
        kickPRNG = random.randint(4, 12)

    elif rngM == 22:
        kickPRNG = random.randint(7, 11)


    elif rngM == 23:
        kickPRNG = random.randint(5, 17)

    elif rngM == 24:
        kickPRNG = random.randint(2, 7)

    elif rngM == 25:
        kickPRNG = random.randint(4, 11)

    elif rngM == 26:
    	kickPRNG = random.randint(4, 17)

    else:
        kickPRNG = 1

    return kickPRNG