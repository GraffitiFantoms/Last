import random
def MonsterDrops(rngM):

	if rngM == 1:
		MDropGolden = random.randint(20, 31)

	elif rngM == 2:
		MDropGolden = random.randint(3, 9)

	elif rngM == 3:
		MDropGolden = random.randint(12, 22)

	elif rngM == 4:
		MDropGolden = random.randint(4, 12)

	elif rngM == 5:
		MDropGolden = random.randint(1, 3)

	elif rngM == 6:
		MDropGolden = random.randint(1, 5)

	elif rngM == 7:
		MDropGolden = random.randint(1, 3)

	elif rngM == 8:
		MDropGolden = random.randint(0, 7)

	elif rngM == 9:
		MDropGolden = random.randint(0, 3)

	elif rngM == 10:
		MDropGolden = random.randint(1, 7)

	elif rngM == 11:
		MDropGolden = random.randint(11, 14)

	elif rngM == 12:
		MDropGolden = random.randint(0, 4)

	elif rngM == 13:
		MDropGolden = random.randint(1, 4)

	elif rngM == 14:
		MDropGolden = random.randint(0, 5)

	elif rngM == 15:
		MDropGolden = random.randint(1, 22)

	elif rngM == 16:
		MDropGolden = random.randint(11, 17)

	elif rngM == 17:
		MDropGolden = random.randint(1, 7)

	elif rngM == 18:
		MDropGolden = random.randint(0, 5)

	elif rngM == 19:
		MDropGolden = random.randint(0, 4)

	elif rngM == 20:
		MDropGolden = random.randint(0, 5)

	elif rngM == 21:
		MDropGolden = random.randint(0, 3)

	elif rngM == 22:
		MDropGolden = random.randint(3, 4)

	elif rngM == 23:
		MDropGolden = random.randint(0, 5)

	elif rngM == 24:
		MDropGolden = random.randint(2, 7)

	elif rngM == 25:
		MDropGolden = random.randint(4, 21)

	else:
		MDropGolden = random.randint(0, 0)
    
	return MDropGolden

def Mdrop_Dobicha(dobicha):
	if dobicha == 0:
		RNGmDobicha = random.randint(0,25)
	if dobicha == 1:
		RNGmDobicha = random.randint(0,15)
