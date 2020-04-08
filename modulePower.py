import time

#def clicked2 (MB):
	#if MB == 1 or 2:
		#MB -= 1
		#print('mana - 1')
		#print (MB)

	#return MB


#	if ManaBAR == 1 or 2:
		#if power == 0:
			#Kven = 1
			#return(electricBoard)
			#print('electricBoard active')
			#time.sleep(40)
			#kven = 0
			#return(electricBoard)
			#print('electricBoard desActive')
	#elif ManaBAR == 0:
		#print('недостаток маны!')





def wait_mana (ManaBAR):
	if ManaBAR == 0:
		time.sleep(10)
		ManaBAR + 25
		print('mana + 1')
		print (ManaBAR)

	elif ManaBAR == 1:
		time.sleep(10)
		ManaBAR = 50
		print('mana + 1')
		print (ManaBAR)
	elif ManaBAR == 2:
		ManaBAR = 50

	return(ManaBAR)