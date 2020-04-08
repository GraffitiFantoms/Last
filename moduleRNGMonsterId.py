import random
def RNG(rng, location):
	if location == 1:
		rng = random.randint(1, 11)
	if location == 2:
		rng = random.randint(12, 27)
	if location == 3:
		rng = random.randint(28, 32)
	if location == 4:
		rng = random.randint(33, 42)
	if location == 5:
		rng = random.randint(43, 46)
	if location == 6:
		rng = random.randint(47, 52)
	if location == 7:
		rng = random.randint(53, 57)
	if location == 8:
		rng = random.randint(58, 70)
	if location == 9:
		rng = 0

	return rng