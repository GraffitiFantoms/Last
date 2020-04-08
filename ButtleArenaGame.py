#BattleArenaGame
#импортируем модули
import os
import random
import time

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, Label, ttk, Button, Tk
from tkinter.ttk import Combobox, Progressbar

from moduleHPm import IfMonster
from moduleKillM import killM
from modulePower import wait_mana
from moduleHPpDamage import kickPlayerRNG
from moduleMdrop import MonsterDrops


WORK_PATH = os.path.abspath(os.getcwd())

#kickB.config(state='disabled')
	
	#серебрянная цепь
	#серебрянный меч
	#улучшенный серебрянный меч
	#серебрянные шарики
	#серебранная кольчуга
	#серебрянный пластинчатый доспец


#Переменные способностей
BaseScillPER = 0
Fortress = 0
Dobicha = 0
shild = 0

#Переменные
rng = random.randint(1, 25)
HPm = IfMonster(rng)
HPp = 100
MaxHPp = 100
ManaBAR = 50
powerUssing = 0
motion = 0
score = 0
MBattel = 1
killMm = killM(HPm)
golden = 10
InventoryHotPER = 1
UseHotI = 0
location = 1
locationUse = 0

level = 1    #данный уровень'''
LevelProshlii = level    ##прошлый уровень'''
tolant = 0    #Очков толанта'''
ScoreTolant = 0    #сколько у игрока'''
MAXscoreTolant = 20    #Надо для достижения след. ур'''

'''Ингридиенты'''
blood_naker = 0           #кровь накера
eye_guls = 0              #глаз гуля
blood_viverna = 0         #кровь виверны
mandrake_root = 0         #корень мандрагоры
light_dust = 0            #свето пыль
marsh_grass = 0           #болотная трава
booth_viverna = 0         #зуб виверны
kogo_pangolin = 0         #коготь ящера
gland_vepr = 0            #гланда вепря
liver_garkain = 0         #печень гаркаина
blood_stone = 0           #камень крови
crystal_wind = 0          #кристал ветра
chamomile = 0             #ромашка
phoenix_feather = 0       #перо феникса
magma_rod = 0             #жезл магмы
fire_light = 0            #огненный свет
ether_in_the_bank = 0     #эфир в банке
snake_eye = 0             #глаз змеи


inferna_shard = 0         #осколок инферны
terra_shard = 0           #осколок земли
shard_of_darkness = 0     #осколок тьмы
air_shard = 0             #осколок воздуха
shard_of_the_sun = 0      #осколок солнца
moon_shard = 0            #осколок луны


iron_ore = 0         #железная руда
silver_ore = 0       #серебряная руда
steel = 0            #сталь
dark_steel = 0       #тёмная сталь
lunar_metal = 0      #лунный металл
bronze = 0           #бронза


essence_of_air = 0          #эссенция воздуха
essence_of_darkness = 0     #эссенция тьмы
essence_of_space = 0        #эссенция пространства
essence_of_thought = 0      #эссенция мысли
essence_of_life = 0         #эссенция жизни
water_essence = 0           #эссенция воды
essence_of_fire = 0         #эссенция огня
ice_essence = 0             #эссенция льда
essence_of_earth = 0        #эссенция земли

none = 0
'''Копии Ингридиентов'''
blood_naker_copy = 0           #кровь накера
eye_guls_copy = 0              #глаз гуля
blood_viverna_copy = 0         #кровь виверны
mandrake_root_copy = 0         #корень мандрагоры
light_dust_copy = 0            #свето пыль
marsh_grass_copy = 0           #болотная трава
booth_viverna_copy = 0         #зуб виверны
kogo_pangolin_copy = 0         #коготь ящера
gland_vepr_copy = 0            #гланда вепря
liver_garkain_copy = 0         #печень гаркаина
blood_stone_copy = 0           #камень крови
crystal_wind_copy= 0          #кристал ветра
chamomile_copy = 0             #ромашка
phoenix_feather_copy = 0       #перо феникса
magma_rod_copy = 0             #жезл магмы
fire_light_copy = 0            #огненный свет
ether_in_the_bank_copy = 0     #эфир в банке
snake_eye_copy = 0             #глаз змеи
blue_mushroom = 0              #синий гриб

inferna_shard_copy = 0         #осколок инферны
terra_shard_copy = 0           #осколок земли
shard_of_darkness_copy = 0     #осколок тьмы
air_shard_copy = 0             #осколок воздуха
shard_of_the_sun_copy = 0      #осколок солнца
moon_shard_copy = 0            #осколок луны


iron_ore_copy = 0         #железная руда
silver_ore_copy = 0       #серебряная руда
steel_copy = 0            #сталь
dark_steel_copy = 0       #тёмная сталь
lunar_metal_copy = 0      #лунный металл
bronze_copy = 0           #бронза


essence_of_air_copy = 0          #эссенция воздуха
essence_of_darkness_copy = 0     #эссенция тьмы
essence_of_space_copy = 0        #эссенция пространства
essence_of_thought_copy = 0      #эссенция мысли
essence_of_life_copy = 0         #эссенция жизни
water_essence_copy = 0           #эссенция воды
essence_of_fire_copy = 0         #эссенция огня
ice_essence_copy = 0             #эссенция льда
essence_of_earth_copy = 0        #эссенция земли

none_copy = 0


#переменные разговоров
Ivan = 0
Neznakomec = 0
Lore_Dialog = 0

#Изучение Мест
forest = 1 #Лес
boloto = 0 #Болото
onion = 0 #Луг
castle = 0 #Замок
caves = 0 #Пещеры
ancientforest = 0 #Древние Леса
caves_Plot = 0 #Сюжетные пещеры
mountains = 0 #Горы
cemetery = 0 #Кладбище

#Счетчик использования способностей, элексиров
UseElicVoskreshenie = 0    #Счетчик использования Элексира воскрешения
UseYoungElic = 0	#Счетчик использования Малого Элексира молодости
UseYoungNormalElic = 0

#переменные ивентов
i = 1
ivent = 0
iventRNGwait = random.randint(5, 6)
iventRNG = random.randint(0, 5)

#Начало игры
#messagebox.showinfo('History', 'Ты отважный герой отправившийся на исследование земли, байки раскажут тебе зачем ты идёшь...\n Взяв свой меч, ты отправился... "Удачи!"')
#messagebox.showinfo('Управление', 'Слева есть Полоса здоровья монстра')

#кнопки скилов def:
def shildClick():
	global tolant
	global BaseScillPER
	global shild
	if tolant > 0 and BaseScillPER == 1:
		if shild == 0:
			shild = 1
			tolant  -= 1
			TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
			time.sleep(0.3)
		elif shild == 1:
			shildBTN.config(state='disabled')
			shild = 2
			tolant -= 1
			time.sleep(0.3)
	else:
		print('NOOO!')

def BasaClick():
	global tolant
	global BaseScillPER
	if tolant > 0:
		global MaxHPp
		BaseScill.config(state='disabled')
		BaseScillPER = 1
		MaxHPp = 110
		tolant -= 1
		HPp = MaxHPp
		TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
	else:
		print('NOOO!')

def FortressClick():
	global Fortress
	global tolant
	global MaxHPp
	global HPp
	global BaseScillPER
	if tolant > 0 and BaseScillPER == 1:
		if Fortress == 0:
			Fortress = 1
			MaxHPp = 120
			tolant  -= 1
			HPp = MaxHPp
			TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
			time.sleep(0.3)
		elif Fortress == 1:
			FortressScill.config(state='disabled')
			Fortress = 2
			MaxHPp = 170
			print(MaxHPp)
			tolant -= 1
			HPp = MaxHPp
			time.sleep(0.3)
	else:
		print('NOOO!')

def rightIC():
	global InventoryHotPER
	print('right')
	print(InventoryHotPER)
	InventoryHotPER -= 1
	if InventoryHotPER < 1:
		InventoryHotPER = 1

# def MenuInventoryCommand(MenuInventoryPer):
# 	MenuInventoryPer += 1 if len(MenuInventoryList) > MenuInventoryPer else 0
# 	# MenuInventoryPer += 1
# 	# if len(MenuInventoryList) <= MenuInventoryPer:
# 	# 	MenuInventoryPer = 0
# 	MenuInventoryButton.config(image=MenuInventoryList[MenuInventoryPer])

def MenuInventoryCommand(MenuInventoryButton):
	global MenuInventoryPer
	MenuInventoryPer += 1
	if len(MenuInventoryList) <= MenuInventoryPer:
		MenuInventoryPer = 0
	MenuInventoryButton.config(image=MenuInventoryList[MenuInventoryPer])

#по нажатию на кнопку "kick"
def clicked1():
	InventoryHotPER = InventoryHotBar.get()

	global level
	global tolant
	global LevelProshlii
	global ScoreTolant
	global MAXscoreTolant
	global Lore_Dialog

	global forest #Лес
	global boloto #Болото
	global onion #Луг
	global castle #Замок
	global caves #Пещеры
	global ancientforest #Древние Леса
	global caves_Plot #Сюжетные пещеры
	global mountains #Горы
	global cemetery #Кладбище

	global HPm
	global HPp
	global MaxHPp

	global Ivan
	global Neznakomec
	global UseHotI
	global rng
	global score
	global golden
	global killMm

	global UseElicVoskreshenie
	global UseYoungElic
	global UseYoungNormalElic
	global locationUse
	global location

	global blood_Viverna, blood_VivernaCopy
	global Blood_Naker, Blood_NakerCopy
	global SAS_Gul, SAS_GulCopy
	global Koren_Mandragora, Koren_MandragoraCopy
	global blood_Stone, blood_StoneCopy
	global crystal_Wind, crystal_WindCopy
	global BolotnaiTrava, BolotnaiTravaCopy
	global Romashka, RomashkaCopy
	global Light_Dust, Light_DustCopy
	global boothViverna, boothVivernaCopy
	global kogo_Iher, kogo_IherCopy 
	global gland_vepr, gland_veprCopy
	global liver_Garkain, liver_GarkainCopy
	global Iron_Ore, Iron_OreCopy
	global Ground_Silver, Ground_SilverCopy
	global Silver_ore, Silver_oreCopy

	locationUse = (len(location) - 1)

	if ScoreTolant > MAXscoreTolant or ScoreTolant == MAXscoreTolant:
		level += 1
		print('level: ' + str(level))

	if level > LevelProshlii:
		MAXscoreTolant *= 1.5
		tolant += 1
		print('MAXtolant:' + str(MAXscoreTolant))
		LevelProshlii = level


	print('MaxHP: ' + str(MaxHPp))

	if HPp > MaxHPp: 
			HPp = MaxHPp
			HPpBar['value'] = HPp

	if InventoryHotPER == 'Железный меч':
		kickMRNG = random.randint(10, 30)
		HPm -= kickMRNG
		barM['value'] = HPm
		UseHotI = InventoryHot.index('Железный меч')
		InventoryHotBar.current(0) 
		killMm = killM(HPm)

	if InventoryHotPER == 'Меч РАЗРАБОТЧИКА':
		HPm -= 9999
		HPp += 100
		barM['value'] = HPm
		UseHotI = InventoryHot.index('Меч РАЗРАБОТЧИКА')
		InventoryHotBar.current(UseHotI)
		killMm = killM(HPm)

	if InventoryHotPER == 'Элексир Воскрешения':
		UseElicVoskreshenie = 6
		InventoryHotBar.current(0)
		InventoryHot.remove('Элексир Воскрешения')
		InventoryHotBar['values'] = (InventoryHot)


	if InventoryHotPER == 'Малый Элексир молодости':
		UseYoungElic = 3
		HPp += 25
		InventoryHot.remove('Малый Элексир молодости')
		InventoryHotBar.current(0)
		HPpBar['value'] = HPp
		InventoryHotBar['values'] = (InventoryHot)

	if InventoryHotPER == 'Средний Элексир молодости':
		UseYoungNormalElic = 4
		HPp += 50
		InventoryHot.remove('Средний Элексир молодости')
		InventoryHotBar.current(0)
		HPpBar['value'] = HPp
		InventoryHotBar['values'] = (InventoryHot)

	if InventoryHotPER == 'Мастерский Элексир молодости':
		HPp += 80
		InventoryHot.remove('Мастерский Элексир молодости')
		InventoryHotBar.current(0)
		HPpBar['value'] = HPp
		InventoryHotBar['values'] = (InventoryHot)


	if InventoryHotPER == 'Травинной Раствор':
		InventoryHot.remove('Травинной Раствор')

	if killMm == 1:
		randomDrop = random.randint(0,10)
		if rng == 10 or rng == 21 or rng == 26 or rng == 27 or rng == 28 or rng == 56 or rng == 57:
			Blood_NakerCopy = Blood_Naker
			Blood_Naker += random.randint(4, 8)
		if rng == 8 or rng == 23:
			SAS_GulCopy = SAS_Gul
			SAS_Gul += 1
		if rng == 52:
			blood_VivernaCopy = blood_Viverna
			boothVivernaCopy = boothViverna
			crystal_WindCopy = crystal_Wind
			blood_Viverna += random.randint(10, 30)
			boothViverna += random.randint(0, 2)
			crystal_Wind += random.randint(0, 2)
		if rng == 4 or rng == 15 or rng == 31:
			blood_StoneCopy = blood_Stone
			blood_Stone += 1
		if rng == 57:
			Ground_SilverCopy = Ground_Silver
			Silver_oreCopy = Silver_ore
			Iron_OreCopy = Iron_Ore
			Ground_Silver += random.randint(0, 8)
			Silver_ore += random.randint(0,2)
			Iron_Ore += random.randint(0, 2)
		if rng == 25 or rng == 24 or rng == 27 or rng == 14:
			Koren_MandragoraCopy = Koren_Mandragora
			Koren_Mandragora += random.randint(0, 1)
		if rng == 3 or rng == 9 or rng == 11:
			RomashkaCopy = Romashka
			Romashka += random.randint(0, 6)
		if rng == 60 or rng == 55:
			Light_DustCopy = Light_Dust
			Light_Dust += random.randint(0, 2)
		if rng == 5 or rng == 17 or rng == 30:
			gland_veprCopy = gland_vepr
			gland_vepr += 1
		if rng == 49:
			kogo_IherCopy = kogo_Iher
			kogo_Iher += random.randint(2, 5)
		if rng == 14 or rng == 16 or rng == 23 or rng == 24:
			BolotnaiTravaCopy = BolotnaiTrava
			BolotnaiTrava += random.randint(0, 4)
		if rng == 43:
			liver_GarkainCopy = liver_Garkain
			liver_Garkain += random.randint(0, 1)
		InventoryBar['values'] = (Inventory) 
		score += 1
		ScoreTolant += ((MAXscoreTolant/5)+ level)
		ScoreInfo.configure(text = 'Убийства: ' + str(score))
		print ('Убил')
		if locationUse == 0:
			rng = random.randint(1, 11)
		elif locationUse == 1:
			rng = random.randint(12, 27)
		elif locationUse == 2:
			rng = random.randint(28, 32)
		elif locationUse == 3:
			rng = random.randint(33, 42)
		elif locationUse == 4:
			rng = random.randint(43, 46)
		elif locationUse == 5:
			rng = random.randint(47, 52)
		elif locationUse == 6:
			rng = random.randint(53, 57)
		elif locationUse == 7:
			rng = random.randint(58, 70)
		HPm = IfMonster(rng)
		InfoM.configure(text = "вы сражаетесь с: " + MonsterI[rng])
		barM['value'] = HPm
		killMm = 0
		golden += MonsterDrops(rng)
		GoldenInfo.configure(text = 'Золото: ' + str(golden))
		print('очки: ' + str(score))

	if shild == 0:
		HPp = HPp - kickPlayerRNG(rng)
		HPpBar['value'] = HPp
	if shild == 1:
		HPp = HPp - (round(kickPlayerRNG(rng)/1.5))
		HPpBar['value'] = HPp
	if shild == 2:
		HPp = HPp - (round(kickPlayerRNG(rng)/1.8))
		HPpBar['value'] = HPp

	print(locationUse)
	LevelInfo.configure(text = 'Уровень: ' + str(level))
	MaxScoreInfo.configure(text = 'Опыта надо для следующего уровня ' + str(round(MAXscoreTolant)))
	ScoreTolantInfo.configure(text = 'Очков: ' + str(ScoreTolant))
	TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
	LocationInfo.configure(text = 'Локация: ' + location[locationUse])
	LocationComboBox['values'] = (location)


	A = MaxHPp - HPp
	print('урон по вам: ' + str(A))

	if UseElicVoskreshenie > 0:
		UseElicVoskreshenie -= 1
		InfoUseRevivalElic.configure(text = 'Используется Элексир Воскрешения, ходов: ' + str(UseElicVoskreshenie))
	if UseElicVoskreshenie < 1:
		UseElicVoskreshenie -= 1
		UseElicVoskreshenie = 0
		InfoUseRevivalElic.configure(text = '')

	if UseYoungElic > 0:
		UseYoungElic -= 1
		InfoUseYoungElic.configure(text = 'Используется Элексир Малой молодости, ходов: ' + str(UseYoungElic))
		HPp += 10
	if UseYoungElic < 1:
		UseYoungElic = 0
		InfoUseYoungElic.configure(text = '')

	if UseYoungNormalElic > 0:
		UseYoungNormalElic -= 1
		InfoUseYoungElic.configure(text = 'Используется Элексир Средней молодости, ходов: ' + str(UseYoungNormalElic))
		HPp += 20
	if UseYoungNormalElic < 1:
		UseYoungNormalElic = 0
		InfoUseYoungElic.configure(text = '')

	#красивые переменные энгридиентов
	beautiful_inventory('Кровь Накера: ', Blood_Naker,Blood_NakerCopy)
	beautiful_inventory('Кровь Виверны: ', blood_Viverna, blood_VivernaCopy)
	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	beautiful_inventory('Кровь Накера: ', Blood_Naker, Blood_NakerCopy)

	if 'Глаз Гуля: ' + str(SAS_Gul) not in Inventory:
		if SAS_Gul > 0:
			Inventory.append('Глаз Гуля: ' + str(SAS_Gul))
			Inventory.remove('Глаз Гуля: ' + str(SAS_GulCopy))
	if 'Глаз Гуля: ' + str(SAS_Gul) in Inventory:
		if SAS_Gul < 1:
			Inventory.remove('Глаз Гуля: ' + str(SAS_Gul))

	if 'Ромашек: ' + str(Romashka) not in Inventory:
		if Romashka > 0:
			Inventory.append('Ромашек: ' + str(Romashka))
			Inventory.remove('Ромашек: ' + str(RomashkaCopy))
	if 'Ромашек: ' + str(Romashka) in Inventory:
		if Romashka < 1:
			Inventory.remove('Ромашек: ' + str(Romashka))

	if 'Камень Крови: ' + str(blood_Stone) not in Inventory:
		if blood_Stone > 0:
			Inventory.append('Камень Крови: ' + str(blood_Stone))
			Inventory.remove('Камень Крови: ' + str(blood_StoneCopy))
	if 'Камень Крови: ' + str(blood_Stone) in Inventory:
		if blood_Stone < 1:
			Inventory.remove('Камень Крови: ' + str(blood_Stone))

	if 'Корень мандрагоры: ' + str(Koren_Mandragora) not in Inventory:
		if Koren_Mandragora > 0:
			Inventory.append('Корень мандрагоры: ' + str(Koren_Mandragora))
			Inventory.remove('Корень мандрагоры: ' + str(Koren_MandragoraCopy))
	if 'Корень мандрагоры: ' + str(Koren_Mandragora) in Inventory:
		if Koren_Mandragora < 1:
			Inventory.remove('Корень мандрагоры: ' + str(Koren_Mandragora))

	if 'Свето пыль: ' + str(Light_Dust) not in Inventory:
		if Light_Dust > 0:
			Inventory.append('Свето пыль: ' + str(Light_Dust))
			Inventory.remove('Свето пыль: ' + str(Light_DustCopy))
	if 'Свето пыль: ' + str(Light_Dust) in Inventory:
		if Light_Dust < 1:
			Inventory.remove('Свето пыль: ' + str(Light_Dust))

	if 'Болотная трова: ' + str(BolotnaiTrava) not in Inventory:
		if BolotnaiTrava > 0:
			Inventory.append('Болотная трова: ' + str(BolotnaiTrava))
			Inventory.remove('Болотная трова: ' + str(BolotnaiTravaCopy))
	if 'Болотная трова: ' + str(BolotnaiTrava) in Inventory:
		if BolotnaiTrava < 1:
			Inventory.remove('Болотная трова: ' + str(BolotnaiTrava))

	if 'Зубы виверны: ' + str(boothViverna) not in Inventory:
		if boothViverna > 0:
			Inventory.append('Зубы виверны: ' + str(boothViverna))
			Inventory.remove('Зубы виверны: ' + str(boothVivernaCopy))
	if 'Зубы виверны: ' + str(boothViverna) in Inventory:
		if boothViverna < 1:
			Inventory.remove('Зубы виверны: ' + str(boothViverna))

	if 'Коготь Ящера: ' + str(kogo_Iher) not in Inventory:
		if kogo_Iher > 0:
			Inventory.append('Коготь Ящера: ' + str(kogo_Iher))
			Inventory.remove('Коготь Ящера: ' + str(kogo_IherCopy))
	if 'Коготь Ящера: ' + str(kogo_Iher) in Inventory:
		if kogo_Iher < 1:
			Inventory.remove('Коготь Ящера: ' + str(kogo_Iher))

	if 'Железы Вепря: ' + str(gland_vepr) not in Inventory:
		if gland_vepr > 0:
			Inventory.append('Железы Вепря: ' + str(gland_vepr))
			Inventory.remove('Железы Вепря: ' + str(gland_veprCopy))
	if 'Железы Вепря: ' + str(gland_vepr) in Inventory:
		if gland_vepr < 1:
			Inventory.remove('Железы Вепря: ' + str(gland_vepr))

	if 'Печень Гаркаина: ' + str(liver_Garkain) not in Inventory:
		if liver_Garkain > 0:
			Inventory.append('Печень Гаркаина: ' + str(liver_Garkain))
			Inventory.remove('Печень Гаркаина: ' + str(liver_GarkainCopy))
	if 'Печень Гаркаина: ' + str(liver_Garkain) in Inventory:
		if liver_Garkain < 1:
			Inventory.remove('Печень Гаркаина: ' + str(liver_Garkain))

	if 'Железная руда: ' + str(Iron_Ore) not in Inventory:
		if Iron_Ore > 0:
			Inventory.append('Железная руда: ' + str(Iron_Ore))
			Inventory.remove('Железная руда: ' + str(Iron_OreCopy))
	if 'Железная руда: ' + str(Iron_Ore) in Inventory:
		if Iron_Ore < 1:
			Inventory.remove('Железная руда: ' + str(Iron_Ore))

	if 'Размальчённое Серебро: ' + str(Ground_Silver) not in Inventory:
		if Ground_Silver > 0:
			Inventory.append('Размальчённое Серебро: ' + str(Ground_Silver))
			Inventory.remove('Размальчённое Серебро: ' + str(Ground_SilverCopy))
	if 'Размальчённое Серебро: ' + str(Ground_Silver) in Inventory:
		if Ground_Silver < 1:
			Inventory.remove('Размальчённое Серебро: ' + str(Ground_Silver))

	if 'Кристал Ветра: ' + str(crystal_Wind) not in Inventory:
		if crystal_Wind > 0:
			Inventory.append('Кристал Ветра: ' + str(crystal_Wind))
			Inventory.remove('Кристал Ветра: ' + str(crystal_WindCopy))
	if 'Кристал Ветра: ' + str(crystal_Wind) in Inventory:
		if crystal_Wind < 1:
			Inventory.remove('Кристал Ветра: ' + str(crystal_Wind))

	if 'Серебрянная Руда: ' + str(Silver_ore) not in Inventory:
		if Silver_ore > 0:
			Inventory.append('Серебрянная Руда: ' + str(Silver_ore))
			Inventory.remove('Серебрянная Руда: ' + str(Silver_oreCopy))
	if 'Серебрянная Руда: ' + str(Silver_ore) in Inventory:
		if Silver_ore < 1:
			Inventory.remove('Серебрянная Руда: ' + str(Silver_ore))
	InventoryBar['values'] = (Inventory)

	if HPp < 1:
		if score < 12 and Ivan == 0:
			messagebox.showinfo('Через несколько часов...', 'Эй парень, приди в себя. Я слышал вой, похоже волчья стая не далеко от нас. Я местный охотник Иван, нам нужно уйти подальше от них, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я проведу тебя туда, проживёшь на неделю дольше.')
			HPp += 54
			HPpBar['value'] = HPp
			Ivan = 1
			rng = 9
			HPm = IfMonster(rng)
			InfoM.configure(text = "вы сражаетесь с: " + MonsterI[rng])
		if score > 12 and Ivan == 0:
			messagebox.showinfo('Через несколько часов...', 'Эй парень, приди в себя. Я местный охотник Иван, пришёл на звуки битвы. Это ты один столько вырезал? Что ж, моё почтение, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я покажу тебе путь туда, думаю у князя найдётся работа для такого сильного война как ты.')
			HPp += 70
			HPpBar['value'] = HPp
			Ivan = 1
			rng = 9
			HPm = IfMonster(rng)
			InfoM.configure(text = "вы сражаетесь с: " + MonsterI[rng])
		if HPp < 1:
			if UseElicVoskreshenie > 0:
				HPp += 75
				UseElicVoskreshenie = 0
				InfoUseRevivalElic.configure(text = '')
				HPpBar['value'] = HPp
			else:
				print('died')


	if score > 3 and Neznakomec == 0:
		Neznakomec = 1
		messagebox.showinfo('Незнакомец', 'Пс, парень, нехочешь немного знаний? Упс! Кажись меня нашли, ладно, удачи!')
	if score > 6 and Neznakomec == 1:
		Neznakomec = 2
		messagebox.showinfo('Опять Незнакомец', 'Здравствуй, да, это снова я, на вот, возьми и меня здесь не было! \n\n"Добавлена новая запись в дневник"')
		rngRecept = random.randint(1, 3)
		if rngRecept == 1:
			diary_receipt.append('Рецепт Элексир малой бестелесности')
			CraftReceptBOX['values'] = (diary_receipt)
		if rngRecept == 2:
			diary_receipt.append('Рецепт Средний Элексир молодости')
			CraftReceptBOX['values'] = (diary_receipt)
		if rngRecept == 3:
			diary_receipt.append('Рецепт Малый Элексир силы')
			CraftReceptBOX['values'] = (diary_receipt)

	if score > 19 and Lore_Dialog == 0:
		messagebox.showinfo('Новая локация', 'Леса закончились, пошли спящие болота... Кто знает, что там находится?')
		messagebox.showinfo('Иван', 'ИДИ В ЗАМОК ЧЕРЕЗ БОЛОТА!!!')
		Lore_Dialog = 1
		locationUse = 1
		boloto = 1
		location = [1, "Болота"]
	if score > 37 and Lore_Dialog == 1:
		messagebox.showinfo('Новая локация', 'За болотами оказались поля, видно замок')
		Lore_Dialog = 2
		locationUse = 2
		onion = 1
		location = [2, "Поля"]
	if score > 44 and Lore_Dialog == 2:
		messagebox.showinfo('Новая локация', 'Наконецто! Замок')
		messagebox.showinfo('Стража Замка', 'Если ищешь работу, поговори с местными, может им нужна помощь.')
		locationUse = 8
		Lore_Dialog = 3
		castle = 1
		location = [3, "Замок"]
	if castle == 1:
		print('замок')

	if 'рецепт малый элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой молодости:  Для создания малого элексира молодости мне нужно смешать: один камень крови и кровь накера(1).', DiaryLabelReceipt))
	elif 'рецепт средний элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира средней молодостив:  Для создания среднего элексира молодости мне нужно смешать: два камня крови и кровь накера(3).', DiaryLabelReceipt))
	elif 'рецепт мастерский элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира средней молодостив:  Для создания мастерского элексира молодости мне нужно смешать: один  корень мандрагоры, кровь виверны(3) и добавить это к эфиру в банке.', DiaryLabelReceipt))

	elif 'рецепт малый элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой молодости:  Для создания малого элексира магии мне нужно смешать: один синий гриб и один глаз змеи.', DiaryLabelReceipt))
	elif 'рецепт средний элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой молодости:  Для создания среднего элексира молодости мне нужно смешать: три синих гриба и одну гланду вепря.', DiaryLabelReceipt))
	elif 'рецепт мастерский элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой молодости:  Для создания мастерского элексира магии мне нужно смешать: 6 синих грибов, 2 пера феникса и кровь виверны(5).', DiaryLabelReceipt))

	elif 'Рецепт Элексир малой бестелесности' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой бестелесности:  Для создания элексира малой бестелесности мне нужно смешать: один камень ветра и 2 болотныйх травы.', DiaryLabelReceipt))
	elif 'рецепт элексир полной бестелесности' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой бестелесности:  Для создания элексира полной бестелесности мне нужно смешать: три осколка ветра, два пера феникса и 2 эфира в банке.', DiaryLabelReceipt))

	elif 'Рецепт порошок подченения' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт порошка подченения:  Для создания порошка подченения мне нужно смешать: один камень ветра и 2 болотных травы.', DiaryLabelReceipt))





#ДИАЛОГИ

#Эй парень, приди в себя. Я слышал вой, похоже волчья стая не далеко от нас. Я местный охотник Иван, нам нужно уйти подальше от них, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я покажу тебе путь туда, проживёшь на неделю дольше.

#Легенда:    В неделю пути от этой крепости есть старые руины. Мои маги, изучая древние писания узнали о том, что в этих сельских сказках есть зерно истины. Под теми руинами, согласно этим легендам, хранится оружие, способное переломить ход войны с тварями из леса. Я давно ищу тех, кто не побоится отправиться туда. Если ты действительно не боишься монстров и готов принести мне это орудие, я награжу тебя так, что ты и твои потомки не будут знать бедности. 
#Разговор со стражей замка : Если ищешь работу, поговори с местными, может им нужна помощь.
#>22 :   Эй парень, приди в себя. Я местный охотник Иван, пришёл на звуки битвы. Это ты один столько вырезал? Что ж, моё почтение, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я покажу тебе путь туда, думаю у князя найдётся работа для такого сильного война как ты. 

#при нажатии на кнопку Use!
def clicked2 ():
	global ManaBAR
	if ManaBAR == 25 or 50:
		ManaBAR -= 25
		print('mana - 25')
		print (ManaBAR)
		barMana['value'] = ManaBAR
		print(Inventory)
		print(power)
	else:
		messagebox.showinfo('Недостаток маны')


def CraftingDEF():
	global Blood_Naker
	global SAS_Gul
	global blood_Viverna
	global Romashka
	global Koren_Mandragora
	global Light_Dust
	global BolotnaiTrava
	global boothViverna
	global kogo_Iher
	global gland_vepr
	global liver_Garkain
	global Iron_Ore
	global Ground_Silver
	global blood_Stone
	global crystal_Wind
	global Silver_ore
	global none

	CraftReceptPER = CraftReceptBOX.get()#CraftReceptPER это то что игрок выбрал(какой рецепт использовать)
	print(CraftReceptPER)

	if CraftReceptPER == 'Рецепт Малый Элексир молодости':
		receipt_elixir('Малый Элексир молодости', Blood_Naker, 0, blood_Stone, 0, none, 0)

	if CraftReceptPER == 'Рецепт травиного раствора':
		receipt_elixir('Травинной Раствор', Romashka, 0, liver_Garkain, 0, none, 0)

	if CraftReceptPER == 'Рецепт Элексир малой бестелесности':
		receipt_elixir('Элексир малой бестелесности', Romashka, 0, liver_Garkain, 0, none, 0)

	if CraftReceptPER == 'Рецепт Средний Элексир молодости':
		receipt_elixir('Средний Элексир молодости', Blood_Naker, 0, blood_Stone, 0, none, 0)



	print(InventoryHot)
#Рецепт Средний Элексир молодости
	# if CraftReceptPER == 'Рецепт Средний Элексир молодости':
	# 	if Blood_Naker >= 2 and blood_Stone >= 1:
	# 		InventoryHot.append('Средний Элексир молодости')
	# 		Blood_Naker -= 2
	# 		blood_Stone -= 1
	# 		InventoryHotBar['values'] = (InventoryHot)
	# 		InventoryBar['values'] = (Inventory)

	# if CraftReceptPER == 'Рецепт Элексир малой бестелесности':
	# 	InventoryHot.append('Элексир малой бестелесности')
	# 	InventoryHotBar['values'] = (InventoryHot)

	# if CraftReceptPER == 'Рецепт Малый Элексир силы':
	# 	if crystal_Wind > 0 and gland_vepr > 0:
	# 		InventoryHot.append('Малый Элексир силы')
	# 		InventoryHotBar['values'] = (InventoryHot)

	# if CraftReceptPER == 'Рецепт Малый Элексир молодости':
	# 	if Blood_Naker >= 5 and blood_Stone >= 5:
	# 		InventoryHot.append('Малый Элексир молодости')
	# 		Blood_Naker -= 1
	# 		blood_Stone -= 1
	# 		InventoryHotBar['values'] = (InventoryHot)
	# 		InventoryBar['values'] = (Inventory)

	# if CraftReceptPER == 'Рецепт травиного раствора':
	# 	if Romashka > 2 and liver_Garkain > 0:
	# 		InventoryHot.append('Травинной Раствор')
	# 		Romashka -= 3
	# 		liver_Garkain -= 1
	# 		InventoryHotBar['values'] = (InventoryHot)
	# 		InventoryBar['values'] = (Inventory)


	#надо перенести сюда модуль power и от сюда задовать силу!
#Словарь, списки


MonsterI = {
#Лесные:
	1 : 'Гаргулия',
	2 : 'Снорк',
	3 : 'Бондит',
	4 : 'КровоСос',
	5 : 'Вепрь',
	6 : 'Волк',
	7 : 'Стрыга',
	8 : 'Гуля',
	9 : 'Колдун',
	10 : 'Накер разведчик',
	11 : 'Волколак',
#Болотные:
	12 : 'Гаргулия',
	13 : 'Снорк',
	14 : 'Бондит',
	15 : 'КровоСос',
	16 : 'Гигант',
	17 : 'Вепрь',
	18 : 'Контролёр',
	19 : 'Волк',
	20 : 'Стрыга',
	21 : 'Накер Воин',
	22 : 'Земляной элементаль',
	23 : 'Гуль',
	24 : 'Упырь',
	25 : 'Утопец',
	26 : 'Накер',
	27 : 'Накер разведчик',
#Поляные:
	28 : 'Накер разведчик',
	29 : 'Волк',
	30 : 'Вепрь',
	31 : 'КровоСос',
	32 : 'Грызун',
#Древний Лес:
	33 : 'Альп',
	34 : 'Древний Ворвалф',
	35 : 'Змея',
	36 : 'Древний Энт',
	37 : 'Накер коллекционер',
	38 : '',
	39 : '',
	40 : '',
	41 : '',
	42 : '',
#Кладбища:
	43 : 'Гаркаин',
	44 : 'Альп',
	45 : 'Гробовщик',
	46 : 'Мясо Тёс',
#Горы
	47 : 'Альп',
	48 : 'Василиск',
	49 : 'Ящер',
	50 : 'Боевой дворф',
	51 : 'Грифон',
	52 : 'Виверна',
#Пещеры:
	53 : 'Летучии мыши',
	54 : 'Альп',
	55 : 'Ифрит',
	56 : 'Накер разведчик',
	57 : 'Накер рудокоп',
#Сюжетные пещеры(развалины, катакомбы)
	58 : 'Летучии твари',
	59 : 'Альп',
	60 : 'Ифрит',
	61 : 'Стальная Гаргулия',
	62 : 'Проклятый Волколак',
	63 : 'Призрак доктора',
	64 : 'Призрак обезумевшего',
	65 : 'Каменный Ворвалф',
	66 : 'Оживший труп Волка',
	67 : '',
	68 : '',
	69 : '',
	70 : '',
}

location = [
	'Леса',
	#'Болота',
	#'Луга',
	#'Древние Леса',
	#'Кладбища',
	#'Горы',
	#'Пещеры',
	#'Замок',
	#'Развалинные пещеры' #Сюжетные
]

Inventory = [

]

InventoryHot = [
	'Железный меч',
	'Малый Элексир молодости',
	'Меч РАЗРАБОТЧИКА',
	'Элексир Воскрешения',
]

diary_receipt = [
	'Рецепт травиного раствора',
	'Рецепт Малый Элексир молодости',
]

Ivents = {
	0 : 'none',
	1 : 'Дождь',
	2 : 'Ливень',
	3 : 'none',
	4 : 'Жара',
	5 : 'Бурелом'
}

MobDrops = {
	1 : 'none'
}

#Игра
#Настройки Арены
Arena = Tk()
Arena.overrideredirect(0)
Arena.geometry('1080x720+0+0')
Arena.title("Последний")

#Вкладки battle, craft
Battle_control = ttk.Notebook(Arena)

battle = ttk.Frame(Battle_control)  
Crafting = ttk.Frame(Battle_control) 
Scills = ttk.Frame(Battle_control)
Diary_Tab = ttk.Frame(Battle_control)

Battle_control.add(battle, text='Battle')  
Battle_control.add(Crafting, text='Crafting')
Battle_control.add(Scills, text='Scills')
Battle_control.add(Diary_Tab, text="Дневник")

#Ветка навыков
lbl3 = Label(Scills, text='Ветка навыков')  
lbl3.grid(column=0, row=0)
Battle_control.pack(expand=1, fill='both')  

#надписи(информация о монстре)
InfoM = Label(battle, text = "вы сражаетесь с: " + MonsterI[rng])
InfoM.grid(column=0, row=3)

#Информация о событиях
InfoIvent = Label(battle, text = "Сейчас: " + Ivents[iventRNG])
InfoIvent.grid(column=3, row=3)

#Надпись MANA и HPp
InfoMana = Label(battle, text = "Mana: ")
InfoMana.grid(column = 0, row = 0)

InfoHPp = Label(battle, text = "HP player: ")
InfoHPp.grid(column = 0, row = 1)

#Inventory
InventoryInfo = Label(battle, text = "Быстрый доступ: ")
InventoryInfo.grid(column = 3, row = 0)

GoldenInfo = Label(battle, text = 'Золото: ' + str(golden))
GoldenInfo.grid(column = 3, row = 4)

#Очки
ScoreInfo = Label(battle, text = 'Убийства: ' + str(score))
ScoreInfo.grid(column = 3, row = 5)

#Локация
LocationInfo = Label(battle, text = 'Локация: ' + str(location))
LocationInfo.grid(column = 3, row = 20)

#Бар инвенторя
InventoryHotBar = Combobox(battle)  
InventoryHotBar['values'] = (InventoryHot)  
InventoryHotBar.current(0) 
InventoryHotBar.grid(column = 4, row = 0)
InventoryHotPER = InventoryHotBar.get()

InventoryBar = Combobox(battle)  
InventoryBar['values'] = (Inventory)  
InventoryBar.grid(column = 4, row = 1)

#Меню выбора оружия
rightI = ImageTk.PhotoImage(file=r"D:\Python\ButtleArena\imagine\right.png", master=battle)
rightInv = Button(battle, image = rightI,height=50, width=50, command=rightIC)
rightInv.grid(column=100, row=100)


#кнопка удара
kickBIco = tk.PhotoImage(file=r"D:\Python\ButtleArena\imagine\HOD.png", master=battle)
kickB = Button(battle, image = kickBIco, command=clicked1, height=25, width=50)
kickB.grid(column=1, row=4)

#красивое меню инвенторя
MenuInventoryPer = 0
MenuInventoryList = [
	tk.PhotoImage(file="D:\Python\ButtleArena\imagine\железный меч.png"),
	tk.PhotoImage(file="D:\Python\ButtleArena\imagine\Меч разработчика.png"),
]

MenuInventoryButton = tk.Button(battle)
MenuInventoryButton.config(command=lambda: MenuInventoryCommand(MenuInventoryButton))
MenuInventoryButton.config(heigh=25, width=50)
MenuInventoryButton.grid(column=22, row=22)

#MenuInventoryButton.pack()
#, image= MenuInventoryList[MenuInventoryPer]
# MenuInventoryButton.config(command=lambda: MenuInventoryCommand(MenuInventoryButton))

#выбор способностей способностей
powerBOX = Combobox(battle)  
powerBOX['values'] = ('Квен', 'Ирден', 'Аард', 'Игни', 'Аксий')  
powerBOX.current(0) 
powerBOX.grid(column = 1, row = 6)  
power = powerBOX.get()

#кнопка использования способности
UseB = Button(battle, text="Use!", command=clicked2)  
UseB.grid(column=0, row=6)

#Mana BAR
barMana = Progressbar(battle, length=50)
barMana['value'] = ManaBAR
barMana.grid(column=1, row=0)

#HP BAR монстра
barM = Progressbar(battle, length=200)
barM['value'] = IfMonster(rng)
barM.grid(column=0, row=4)

#HP BAR player
HPpBar = Progressbar(battle, length=100)
HPpBar['value'] = HPp
HPpBar.grid(column = 1, row = 1)


	#раздел крафтов
#Выбор крафта
CraftReceptBOX = Combobox(Crafting)
CraftReceptBOX['values'] = (diary_receipt)
CraftReceptBOX.current(0)
CraftReceptBOX.grid(column = 0, row = 0)  
CraftReceptPER = CraftReceptBOX.get()

#рецепт крафта
CraftReceptInfo = Label(Crafting, text = 'Малый Элексир молодости: 1 Кровь Накера и 1 камень крови')
CraftReceptInfo.grid(column=0, row=10)

#кнопка крафта
UseB = Button(Crafting, text="Craft", command=CraftingDEF)  
UseB.grid(column=0, row=1)

#Функция крафта
def receipt_elixir(elixir, ingr_1, ingr_1_q, ingr_2, ingr_2_q, ingr_3, ingr_3_q):
	if ingr_1 >= ingr_1_q and ingr_2 >= ingr_2_q and ingr_3 >= ingr_3_q:
		InventoryHot.append(elixir)
		ingr_1 -= ingr_1_q
		ingr_2 -= ingr_2_q
		ingr_3 -= ingr_3_q
		InventoryHotBar['values'] = (InventoryHot)
		InventoryBar['values'] = (Inventory)

#красивый инвентарь
def beautiful_inventory(ingr_RUS: str, ingr_per: int, inhr_per_copy: int):
	'''
	:param ingr_RUS: название ингридиента по русски
	:param ingr_per: переменная ингридиента
	:param inhr_per_copy: вторая переманная ингридиента
	'''
	if ingr_RUS + str(ingr_per) not in Inventory:
		if ingr_per > 0:
			Inventory.append(ingr_RUS + str(ingr_per))
			Inventory.remove(ingr_RUS + str(inhr_per_copy))
	if ingr_RUS + str(ingr_per) in Inventory:
		if ingr_per < 1:
			Inventory.remove(ingr_RUS + str(ingr_per))
			ingr_per += 1

	#Раздел скилов
#Кнопки способностей
BaseScill = Button(Scills, text = "Базовый", command=BasaClick)  
BaseScill.grid(column = 20, row = 20)

FortressScill = Button(Scills, text = "Крепкость", command=FortressClick)  
FortressScill.grid(column = 20, row = 18)

shildBTN = Button(Scills, text = "Щитоносец", command=shildClick)  
shildBTN.grid(column = 21, row = 20)

#Информация об уровне
LevelInfo = Label(Scills, text = 'Уровень: ' + str(level))
LevelInfo.grid(column = 0, row = 1)

MaxScoreInfo = Label(Scills, text = 'Опыта надо для следующего уровня ' + str(MAXscoreTolant))
MaxScoreInfo.grid(column = 0, row = 3)

ScoreTolantInfo = Label(Scills, text = 'Очков: ' + str(ScoreTolant))
ScoreTolantInfo.grid(column = 0, row = 2)

TolantInfo = Label(Scills, text = 'Очков умений: ' + str(tolant))
TolantInfo.grid(column = 0, row = 4)
		#Вкладка - Дневник
#Главный текст во вкладке Дневник
with open("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", 'r') as f:
	DiaryReceiptText = f.read()

DiaryLabel = Label(Diary_Tab, text="День первый: Я отправляюсь в путешествие, из аммуниции у меня только Железный меч,одна странная колба(Без понятия что это, но выглядит съедобно.)\n и... всё. ладно, да прибудет со мной сила.")
DiaryLabel.grid(column=0, row=1)

DiaryLabelReceipt = Label(Diary_Tab, text=DiaryReceiptText)
DiaryLabelReceipt.grid(column=0, row=3)
print(DiaryReceiptText)

#Функция по обновлению дневника рецептов
def update_diary(file_path: str, text:str, Label):
	"""
	:param file_path: путь к файлу с рецептами зелий
	:param text: новый рецепт для добавления в файл
	:param Label: объект надписи для конфигурирования
	:return:
	"""
	global DiaryReceiptText
	with open(file_path, 'a') as f_write:
		f_write.write(text)
	with open(file_path, 'r') as f_read:
		DiaryReceiptText = f_read.read()
		Label.config(text=DiaryReceiptText)

#Функция по обновлению дневника рецептов



# информация об использовании элексира, способности
InfoUseRevivalElic = Label(battle, text = '')
InfoUseRevivalElic.grid(column = 0, row = 6)

InfoUseYoungElic = Label(battle, text = '')
InfoUseYoungElic.grid(column = 0, row = 7)



LocationComboBox = Combobox(battle)
LocationComboBox['values'] = (location)
print(location)
LocationComboBox.current(0)
LocationComboBox.grid(column = 0, row = 30)
LocationComboBoxPER = LocationComboBox.get()

LocationComboBoxPER = LocationComboBox.get()
LocationBTN = Button(battle, text = "Переход в " + str(LocationComboBoxPER))
LocationBTN.grid(column = 0, row = 21)

#Локации
#def location_update():



	



Arena.mainloop()
'''
with open("D:\Python\ButtleArena\text\DiaryReceipt.txt", 'r') as f:
	DiaryReceiptText = f.read()
	f.write('fsfd')
'''