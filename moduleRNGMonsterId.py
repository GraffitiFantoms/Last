import random
def RNG(rng, location_use):
	if location_use == 1:
		rng = random.randint(1, 11)
	if location_use == 2:
		rng = random.randint(12, 27)
	if location_use == 3:
		rng = random.randint(28, 32)
	if location_use == 4:
		rng = random.randint(33, 42)
	if location_use == 5:
		rng = random.randint(43, 46)
	if location_use == 6:
		rng = random.randint(47, 52)
	if location_use == 7:
		rng = random.randint(53, 57)
	if location_use == 8:
		rng = random.randint(58, 70)
	if location_use == 9:
		rng = 0

	return rng