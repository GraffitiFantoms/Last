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
from modulePower import wait_mana
from moduleHPpDamage import kickPlayerRNG
from moduleMdrop import MonsterDrops


WORK_PATH = os.path.abspath(os.getcwd())
FILE_INGR = "D:\\Python\\ButtleArena\\text\\all_ingr.txt"
FILE_ALL_WEAPON = "D:\\Python\\ButtleArena\\text\\all_weapon.txt"

global Inventory_bar

#kickB.config(state='disabled')
	
	#серебрянная цепь
	#серебрянный меч
	#улучшенный серебрянный меч
	#серебрянные шарики
	#серебранная кольчуга
	#серебрянный пластинчатый доспец



ordinary = False

all_weapon = {
	'железный меч': [[30, 45], ordinary, []],
	'серебряный меч': [[60, 85], ordinary, []],
	'гибкий лук': [[30, 100], ordinary, []],
	'деревянный посох': [[0, 0], ordinary, []],
	'стальной лук': [[50, 150], ordinary, []],
}




all_monsters = {
#Лесные:
###index     0            1           2        3       4          5
###id : ['rus name', [how golden], [health], [ingr], [q_ingr], [damage]
	1 : ['Гаргулия', [0, 7], 50, 'blood_stone', [1, 1], [4, 14]],
	2 : ['Снорк', [5, 5], 45, 'blood_naker', [2, 2], [3, 11]],
	3 : ['Бондит', [4, 25], 70, 'kogo_pangolin', [3, 3], [5, 17]],
	4 : 'КровоСос',
	5 : 'Вепрь',
	6 : ['Волк', [0, 3], 30, 'kogo_pangolin', [1, 1], [3, 7]],
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
	'Леса'
	#'Болота',
	#'Луга',
	#'Древние Леса',
	#'Кладбища',
	#'Горы',
	#'Пещеры',
	#'Замок',
	#'Развалинные пещеры' #Сюжетные
]

Inventory = []

inventory_dict = {}

InventoryHot = [
	'железный меч',
	'Малый Элексир молодости',
	'Меч РАЗРАБОТЧИКА',
	'Элексир Воскрешения',
	'серебряный меч',
]

diary_receipt = [
	'Рецепт травиного раствора',
	'Рецепт Малый Элексир молодости',
]

Ivents = {
	0: 'солнечно',
	1: 'Дождь',
	2: 'Ливень',
	3: 'none',
	4: 'Жара',
	5: 'Бурелом',
}

MobDrops = {
	1 : 'none'
}

#Переменные способностей
BaseScillPER = 0
Fortress = 0
Dobicha = 0
shild = 0

#Переменные

rng = random.randint(1, 25)
health_monster = IfMonster(rng)
health_player = 100
max_health_player = 100
ManaBAR = 50
powerUssing = 0
motion = 0
score = 0
MBattel = 1
# killMm = killM(health_monster)
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

#начало для монстра
random_id_battle_monsers = random.randint(1, 3)
who_battle_monster_from_list = all_monsters.get(random_id_battle_monsers)[0]
health_monster_from_list = all_monsters.get(random_id_battle_monsers)[2]
get_monsters_golden_from_list = random.randint(all_monsters.get(random_id_battle_monsers)[1][0], all_monsters.get(random_id_battle_monsers)[1][1])
get_monster_ingr_from_list = all_monsters.get(random_id_battle_monsers)[3]
quantity_monster_ingr_from_list = random.randint(all_monsters.get(random_id_battle_monsers)[4][0], all_monsters.get(random_id_battle_monsers)[4][0])

print(who_battle_monster_from_list)


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

Battle_control.add(battle, text='Сражение')
Battle_control.add(Crafting, text='Создание')
Battle_control.add(Scills, text='Навыки')
Battle_control.add(Diary_Tab, text="Дневник")

#Ветка навыков
lbl3 = Label(Scills, text='Ветка навыков')
lbl3.grid(column=0, row=0)
Battle_control.pack(expand=1, fill='both')

#надписи(информация о монстре)
InfoM = Label(battle, text="вы сражаетесь с: " + who_battle_monster_from_list)
InfoM.grid(column=0, row=3)

#Информация о событиях
InfoIvent = Label(battle, text="Сейчас: " + Ivents[iventRNG])
InfoIvent.grid(column=3, row=3)

#Надпись MANA и health_player
InfoMana = Label(battle, text="Магия: ")
InfoMana.grid(column=0, row=0)

Info_health_player = Label(battle, text="Жизни: ")
Info_health_player.grid(column=0, row=1)

#Inventory
InventoryInfo = Label(battle, text="Быстрый доступ: ")
InventoryInfo.grid(column=3, row=0)

GoldenInfo = Label(battle, text='Золото: ' + str(golden))
GoldenInfo.grid(column=3, row=4)

#Очки
ScoreInfo = Label(battle, text='Убийства: ' + str(score))
ScoreInfo.grid(column=3, row=5)

#Локация
LocationInfo = Label(battle, text='Локация: ' + str(location))
LocationInfo.grid(column=3, row=20)

#Бар инвенторя
InventoryHotBar = Combobox(battle)
InventoryHotBar['values'] = (InventoryHot)
InventoryHotBar.current(0)
InventoryHotBar.grid(column=4, row=0)
InventoryHotPER = InventoryHotBar.get()



#Меню выбора оружия
# rightI = ImageTk.PhotoImage(file=r"D:\Python\ButtleArena\imagine\right.png", master=battle)
# rightInv = Button(battle, image=rightI, height=50, width=50, command=rightIC)
# rightInv.grid(column=100, row=100)


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

#Mana BAR
barMana = Progressbar(battle, length=50)
barMana['value'] = ManaBAR
barMana.grid(column=1, row=0)

#HP BAR монстра
barM = Progressbar(battle, length=200)
barM['value'] = IfMonster(rng)
barM.grid(column=0, row=4)

#HP BAR player
health_player_bar = Progressbar(battle, length=100)
health_player_bar['value'] = health_player
health_player_bar.grid(column = 1, row = 1)


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

#инвентарь
Inventory_bar = Combobox(battle)
Inventory_bar.grid(column=4, row=1)

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
		global max_health_player
		BaseScill.config(state='disabled')
		BaseScillPER = 1
		max_health_player = 110
		tolant -= 1
		health_player = max_health_player
		TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
	else:
		print('NOOO!')

def FortressClick():
	global Fortress
	global tolant
	global max_health_player
	global health_player
	global BaseScillPER
	if tolant > 0 and BaseScillPER == 1:
		if Fortress == 0:
			Fortress = 1
			max_health_player = 120
			tolant  -= 1
			health_player = max_health_player
			TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
			time.sleep(0.3)
		elif Fortress == 1:
			FortressScill.config(state='disabled')
			Fortress = 2
			max_health_player = 170
			print(max_health_player)
			tolant -= 1
			health_player = max_health_player
			time.sleep(0.3)
	else:
		print('NOOO!')

# def rightIC():
# 	global InventoryHotPER
# 	print('right')
# 	print(InventoryHotPER)
# 	InventoryHotPER -= 1
# 	if InventoryHotPER < 1:
# 		InventoryHotPER = 1

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

	global health_monster
	global health_player
	global max_health_player


	global who_battle_monster_from_list
	global health_monster_from_list
	global random_id_battle_monsers

	global Inventory_bar


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

	print(InventoryHotPER)

	who_damage_from_monster = random.randint(all_monsters.get(random_id_battle_monsers)[5][0], all_monsters.get(random_id_battle_monsers)[5][1])
	who_damage_from_player = random.randint(all_weapon.get(InventoryHotPER)[0][0], all_weapon.get(InventoryHotPER)[0][1])
	print('урон: ' + str(who_damage_from_player))


	health_monster -= who_damage_from_player
	health_player -= who_damage_from_monster

	if check_if_monster_died(health_monster):
		random_id_battle_monsers = random.randint(1, 3)
		who_battle_monster_from_list = all_monsters.get(random_id_battle_monsers)[0]
		health_monster_from_list = all_monsters.get(random_id_battle_monsers)[2]
		get_monster_ingr_from_list = all_monsters.get(random_id_battle_monsers)[3]
		quantity_monster_ingr_from_list = random.randint(all_monsters.get(random_id_battle_monsers)[4][0], all_monsters.get(random_id_battle_monsers)[4][1])
		get_monsters_golden_from_list = random.randint(all_monsters.get(random_id_battle_monsers)[1][0], all_monsters.get(random_id_battle_monsers)[1][1])

		health_monster = health_monster_from_list
		inventory_dict_variable[get_monster_ingr_from_list][0] += quantity_monster_ingr_from_list
		print(see_tab_inventory(inventory_dict_variable))

	ScoreInfo.configure(text='Убийства: ' + str(score))
	InfoM.configure(text="вы сражаетесь с: " + who_battle_monster_from_list)
	print('жизни монстра: ' + str(health_monster))

	health_player_bar['value'] = health_player
	barM['value'] = health_monster
	Inventory_bar['values'] = see_tab_inventory(inventory_dict_variable)


	if ScoreTolant > MAXscoreTolant or ScoreTolant == MAXscoreTolant:
		level += 1

	if level > LevelProshlii:
		MAXscoreTolant *= 1.5
		tolant += 1
		LevelProshlii = level




	if health_player > max_health_player: 
			health_player = max_health_player
			health_player_bar['value'] = health_player

	# if InventoryHotPER == 'железный меч':
	# 	kickMRNG = random.randint(10, 30)
	# 	health_monster -= kickMRNG
	# 	barM['value'] = health_monster_from_list
	# 	UseHotI = InventoryHot.index('железный меч')
	# 	InventoryHotBar.current(0)
	# 	killMm = check_if_monster_died(health_monster_from_list)

	if InventoryHotPER == 'Меч РАЗРАБОТЧИКА':
		health_monster -= 9999
		health_player += 100
		barM['value'] = health_monster_from_list
		UseHotI = InventoryHot.index('Меч РАЗРАБОТЧИКА')
		InventoryHotBar.current(UseHotI)
		killMm = check_if_monster_died(health_monster_from_list)

	# if InventoryHotPER == 'Элексир Воскрешения':
	# 	UseElicVoskreshenie = 6
	# 	InventoryHotBar.current(0)
	# 	InventoryHot.remove('Элексир Воскрешения')
	# 	InventoryHotBar['values'] = (InventoryHot)


	if InventoryHotPER == 'Малый Элексир молодости':
		UseYoungElic = 3
		health_player += 25
		InventoryHot.remove('Малый Элексир молодости')
		InventoryHotBar.current(0)
		health_player_bar['value'] = health_player
		InventoryHotBar['values'] = (InventoryHot)

	if InventoryHotPER == 'Средний Элексир молодости':
		UseYoungNormalElic = 4
		health_player += 50
		InventoryHot.remove('Средний Элексир молодости')
		InventoryHotBar.current(0)
		health_player_bar['value'] = health_player
		InventoryHotBar['values'] = (InventoryHot)

	if InventoryHotPER == 'Мастерский Элексир молодости':
		health_player += 80
		InventoryHot.remove('Мастерский Элексир молодости')
		InventoryHotBar.current(0)
		health_player_bar['value'] = health_player
		InventoryHotBar['values'] = (InventoryHot)


	if InventoryHotPER == 'Травинной Раствор':
		InventoryHot.remove('Травинной Раствор')

	# if killMm == 1:
		# randomDrop = random.randint(0,10)
		# if rng == 10 or rng == 21 or rng == 26 or rng == 27 or rng == 28 or rng == 56 or rng == 57:
		# 	blood_naker_copy = Blood_Naker
		# 	Blood_Naker += random.randint(4, 8)
		# if rng == 8 or rng == 23:
		# 	SAS_GulCopy = SAS_Gul
		# 	SAS_Gul += 1
		# if rng == 52:
		# 	blood_VivernaCopy = blood_Viverna
		# 	boothVivernaCopy = boothViverna
		# 	crystal_WindCopy = crystal_Wind
		# 	blood_Viverna += random.randint(10, 30)
		# 	boothViverna += random.randint(0, 2)
		# 	crystal_Wind += random.randint(0, 2)
		# if rng == 4 or rng == 15 or rng == 31:
		# 	blood_StoneCopy = blood_Stone
		# 	blood_Stone += 1
		# if rng == 57:
		# 	Ground_SilverCopy = Ground_Silver
		# 	Silver_oreCopy = Silver_ore
		# 	Iron_OreCopy = Iron_Ore
		# 	Ground_Silver += random.randint(0, 8)
		# 	Silver_ore += random.randint(0,2)
		# 	Iron_Ore += random.randint(0, 2)
		# if rng == 25 or rng == 24 or rng == 27 or rng == 14:
		# 	Koren_MandragoraCopy = Koren_Mandragora
		# 	Koren_Mandragora += random.randint(0, 1)
		# if rng == 3 or rng == 9 or rng == 11:
		# 	RomashkaCopy = Romashka
		# 	Romashka += random.randint(0, 6)
		# if rng == 60 or rng == 55:
		# 	Light_DustCopy = Light_Dust
		# 	Light_Dust += random.randint(0, 2)
		# if rng == 5 or rng == 17 or rng == 30:
		# 	gland_veprCopy = gland_vepr
		# 	gland_vepr += 1
		# if rng == 49:
		# 	kogo_IherCopy = kogo_Iher
		# 	kogo_Iher += random.randint(2, 5)
		# if rng == 14 or rng == 16 or rng == 23 or rng == 24:
		# 	BolotnaiTravaCopy = BolotnaiTrava
		# 	BolotnaiTrava += random.randint(0, 4)
		# if rng == 43:
		# 	liver_GarkainCopy = liver_Garkain
		# 	liver_Garkain += random.randint(0, 1)
		# Inventory_bar['values'] = (Inventory)
		# score += 1
		# ScoreTolant += ((MAXscoreTolant / 5) + level)
		# print('Убил')



		killMm = 0
		golden += get_monsters_golden_from_list
		GoldenInfo.configure(text = 'Золото: ' + str(golden))


	# if shild == 0:
	# 	health_player = health_player - kickPlayerRNG(random_id_battle_monsers)
	# 	health_player_bar['value'] = health_player
	# if shild == 1:
	# 	health_player = health_player - (round(kickPlayerRNG(random_id_battle_monsers)/1.5))
	# 	health_player_bar['value'] = health_player
	# if shild == 2:
	# 	health_player = health_player - (round(kickPlayerRNG(random_id_battle_monsers)/1.8))
	# 	health_player_bar['value'] = health_player

	# locationUse = 0
	# print(locationUse)
	# LevelInfo.configure(text = 'Уровень: ' + str(level))
	# MaxScoreInfo.configure(text = 'Опыта надо для следующего уровня ' + str(round(MAXscoreTolant)))
	# ScoreTolantInfo.configure(text = 'Очков: ' + str(ScoreTolant))
	# TolantInfo.configure(text = 'Очков умений: ' + str(tolant))
	# LocationInfo.configure(text = 'Локация: ' + str(location[locationUse]))
	# LocationComboBox['values'] = (location)



	A = max_health_player - health_player
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
		health_player += 10
	if UseYoungElic < 1:
		UseYoungElic = 0
		InfoUseYoungElic.configure(text = '')

	if UseYoungNormalElic > 0:
		UseYoungNormalElic -= 1
		InfoUseYoungElic.configure(text = 'Используется Элексир Средней молодости, ходов: ' + str(UseYoungNormalElic))
		health_player += 20
	if UseYoungNormalElic < 1:
		UseYoungNormalElic = 0
		InfoUseYoungElic.configure(text = '')


	if health_player < 1:
		if score < 12 and Ivan == 0:
			messagebox.showinfo('Через несколько часов...', 'Эй парень, приди в себя. Я слышал вой, похоже волчья стая не далеко от нас. Я местный охотник Иван, нам нужно уйти подальше от них, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я проведу тебя туда, проживёшь на неделю дольше.')
			health_player += 54
			health_player_bar['value'] = health_player
			Ivan = 1
			random_id_battle_monsers = 6
			health_monster_from_list = IfMonster(random_id_battle_monsers)
			InfoM.configure(text = "вы сражаетесь с: " + who_battle_monster_from_list)
		if score > 12 and Ivan == 0:
			messagebox.showinfo('Через несколько часов...', 'Эй парень, приди в себя. Я местный охотник Иван, пришёл на звуки битвы. Это ты один столько вырезал? Что ж, моё почтение, но в таком состоянии ты далеко не уйдёшь. На вот, выпей. Это должно помочь. Здесь не подалёку замок моего господина, я покажу тебе путь туда, думаю у князя найдётся работа для такого сильного война как ты.')
			health_player += 70
			health_player_bar['value'] = health_player
			Ivan = 1
			random_id_battle_monsers = 6
			health_monster_from_list = IfMonster(random_id_battle_monsers)
			InfoM.configure(text = "вы сражаетесь с: " + who_battle_monster_from_list)
		if health_player < 1:
			if UseElicVoskreshenie > 0:
				health_player += 75
				UseElicVoskreshenie = 0
				InfoUseRevivalElic.configure(text = '')
				health_player_bar['value'] = health_player
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
		location = ["Болота"]
	if score > 37 and Lore_Dialog == 1:
		messagebox.showinfo('Новая локация', 'За болотами оказались поля, видно замок')
		Lore_Dialog = 2
		locationUse = 2
		onion = 1
		location = ["Поля"]
	if score > 44 and Lore_Dialog == 2:
		messagebox.showinfo('Новая локация', 'Наконецто! Замок')
		messagebox.showinfo('Стража Замка', 'Если ищешь работу, поговори с местными, может им нужна помощь.')
		locationUse = 8
		Lore_Dialog = 3
		castle = 1
		location = ["Замок"]
	if castle == 1:
		print('замок')

	if 'рецепт малый элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой молодости:  Для создания малого элексира молодости мне нужно смешать: один камень крови и кровь накера(1).', DiaryLabelReceipt))
	if 'рецепт средний элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира средней молодости:  Для создания среднего элексира молодости мне нужно смешать: два камня крови и кровь накера(3).', DiaryLabelReceipt))
	if 'рецепт мастерский элексир молодости' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира мастерской молодости:  Для создания мастерского элексира молодости мне нужно смешать: один  корень мандрагоры, кровь виверны(3) и добавить это к эфиру в банке.', DiaryLabelReceipt))

	if 'рецепт малый элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой магии:  Для создания малого элексира магии мне нужно смешать: один синий гриб и один глаз змеи.', DiaryLabelReceipt))
	if 'рецепт средний элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира средней магии:  Для создания среднего элексира молодости мне нужно смешать: три синих гриба и одну гланду вепря.', DiaryLabelReceipt))
	if 'рецепт мастерский элексир магии' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира мастерской магии:  Для создания мастерского элексира магии мне нужно смешать: 6 синих грибов, 2 пера феникса и кровь виверны(5).', DiaryLabelReceipt))

	if 'рецепт Элексир малой бестелесности' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой бестелесности:  Для создания элексира малой бестелесности мне нужно смешать: один камень ветра и 2 болотныйх травы.', DiaryLabelReceipt))
	if 'рецепт элексир полной бестелесности' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира полной бестелесности:  Для создания элексира полной бестелесности мне нужно смешать: три осколка ветра, два пера феникса и 2 эфира в банке.', DiaryLabelReceipt))

	if 'рецепт лечебный травяной раствор' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт лечебного травяного раствора:  Для создания лечебного травяного раствора мне нужно смешать: 10 ромашек и 2 болотных травы.', DiaryLabelReceipt))

	if 'рецепт элексир малой силы' in  diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира малой силы:  Для создания элексира малой силы мне нужно смешать: один жезыл магмы и одну эссенцию могущества.', DiaryLabelReceipt))
	if 'рецепт элексир сложной силы' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт элексира сложной силы:  Для создания элексира сложной силы мне нужно смешать: 3 эсеенции могущества, два осколка инферны, одио перо феникса', DiaryLabelReceipt))

	if 'рецепт угосающий элексир воскрешения' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт угосающего элексира воскрешения:  Для создания угосающего элексира воскрешения мне нужно смешать: одну эссенцию жизни и эфир в банке', DiaryLabelReceipt))
	if 'рецепт долгий элексир воскрешения' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт долгого элексира воскрешения:  Для создания долгого элексира воскрешения мне нужно смешать: три эссенции жизни и оживлённая кровь накера(3)', DiaryLabelReceipt))

	if 'рецепт порошок подченения' in diary_receipt:
		DiaryLabelReceipt.config(update_diary("D:\\Python\\ButtleArena\\text\\DiaryReceipt.txt", '\n Рецепт порошка подченения:  Для создания порошка подченения мне нужно смешать: один камень ветра и 2 болотных травы.', DiaryLabelReceipt))



#кнопка удара
kickBIco = tk.PhotoImage(file=r"D:\Python\ButtleArena\imagine\HOD.png", master=battle)
kickB = Button(battle, image=kickBIco, command=clicked1, height=25, width=50)
kickB.grid(column=1, row=4)


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
		receipt_elixir('Малый Элексир молодости', 'blood_naker', 0, 'blood_Stone', 0, 'none', 0)

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
	# 		Inventory_bar['values'] = (Inventory)

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
	# 		Inventory_bar['values'] = (Inventory)

	# if CraftReceptPER == 'Рецепт травиного раствора':
	# 	if Romashka > 2 and liver_Garkain > 0:
	# 		InventoryHot.append('Травинной Раствор')
	# 		Romashka -= 3
	# 		liver_Garkain -= 1
	# 		InventoryHotBar['values'] = (InventoryHot)
	# 		Inventory_bar['values'] = (Inventory)


def see_tab_inventory(my_dict):
	ingr_list = []
	for key in my_dict:
		if my_dict[key][0] > 0:
			ingr_list.append(my_dict[key][1] + str(my_dict[key][0]))
	return(ingr_list)

def ingr_filing_dict(file_path):
	inventory_dict = {}
	with open(file_path, 'r') as f:
		for line in f:
			if '#' not in line:
				continue
			sharp_split = line.split('#')
			ingr_ENG = sharp_split[0].split(' ')[0]
			ingr_RUS = sharp_split[1][ : -1]
			inventory_dict[ingr_ENG] = [0, ingr_RUS]
	# for k, v in inventory_dict.items():
	# 	print(k, v)
	return inventory_dict
ingr_filing_dict(FILE_INGR)
inventory_dict_variable = ingr_filing_dict(FILE_INGR)



def check_if_monster_died(health_monster):
	'''
	:param health_monster: жизни монстра
	:False: если живой
	:True: если умер
	'''
	return False if health_monster >= 0 else True


# def who_weapon_attak():
# 	'''
# 	:return: жизни монстра
# 	'''
# 	global all_weapon
# 	global health_monster
# 	global InventoryHotPER
# 	damage_from_weapon_attak = random.randint(all_weapon.get(InventoryHotPER)[0][0], all_weapon.get(InventoryHotPER)[0][1])
# 	health_monster -= damage_from_weapon_attak
# 	print('жизни монстра после фуекции: ' + str(health_monster))
# 	print('урон: ' + str(damage_from_weapon_attak))
#
# 	return health_monster

#Функция крафта
def receipt_elixir(elixir, ingr_1, ingr_1_q, ingr_2, ingr_2_q, ingr_3, ingr_3_q):
	if ingr_1 >= ingr_1_q and ingr_2 >= ingr_2_q and ingr_3 >= ingr_3_q:
		InventoryHot.append(elixir)
		ingr_1 -= ingr_1_q
		ingr_2 -= ingr_2_q
		ingr_3 -= ingr_3_q
		InventoryHotBar['values'] = (InventoryHot)
		# Inventory_bar['values'] = (Inventory)






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



#кнопка использования способности
UseB = Button(battle, text="Use!", command=clicked2)
UseB.grid(column=0, row=6)

#кнопка крафта
UseB = Button(Crafting, text="Craft", command=CraftingDEF)
UseB.grid(column=0, row=1)

#инвентарь
# Inventory_bar['values'] = see_tab_inventory(inventory_dict_variable)

	#Раздел скилов
#Кнопки способностей
BaseScill = Button(Scills, text = "Базовый", command=BasaClick)
BaseScill.grid(column = 20, row = 20)

FortressScill = Button(Scills, text = "Крепкость", command=FortressClick)
FortressScill.grid(column = 20, row = 18)

shildBTN = Button(Scills, text = "Щитоносец", command=shildClick)
shildBTN.grid(column = 21, row = 20)


Arena.mainloop()
