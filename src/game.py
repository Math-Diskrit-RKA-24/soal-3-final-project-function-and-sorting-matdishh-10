PlayerList = []
# No 1   
def initPlayers():
    global PlayerList
    PlayerList = []

# No 2
def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False
    )

# No 3
def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

# No 4
def removePlayer(name):
    global PlayerList
    for i in PlayerList:
        if i['name'] == name:
            PlayerList.remove(i)
            return
    return print("There is no player with that name!")

# No 5
def setPlayer(player, key, value):
    player[key] = value

# No 6

def attackPlayer(attacker, target):
    if target['defense'] == True:
        damage = (attacker.get('damage') - target.get('defensePower'))
        setPlayer(attacker, 'score', (round(attacker.get('score') + 1 - 1/target['defensePower'], 2 )))
    else:
        damage = attacker.get('damage')
        setPlayer(attacker, 'score', attacker['score'] + 1)
    setPlayer(target, 'health', target['health'] - damage)
    setPlayer(target, 'defense', False)

# No 7
def displayMatchResult():
    after_sorted = sorted(PlayerList, key=lambda x: (x['score'], x['health']), reverse=True)
    
    # Tampilkan hasilnya dengan format yang diinginkan
    for i, player in enumerate(after_sorted, 1):
        print(f"Rank {i}: {player['name']} | Score: {player['score']} | Health: {player['health']}")
    
    return after_sorted

# Fungsi Class
player_class = {}
def initPClass():
    global player_class
    player_class = {}

def ChooseClass(name):
    choose_class = int(input("(1) Warrior\n(2) Assassin\n(3) Archer\n(4) Paladin\n(5) Tanker\n(6) Wizard\n(7) Berserker\n(8) Lich\nMasukkan kelas pemain : "))
    if choose_class == 1:
        player_class[name] = "Warrior"
    elif choose_class == 2:
        player_class[name] = "Assassin"
    elif choose_class == 3:
        player_class[name] = "Archer"
    elif choose_class == 4:
        player_class[name] = "Paladin"
    elif choose_class == 5:
        player_class[name] = "Tanker"
    elif choose_class == 6:
        player_class[name] = "Wizard"
    elif choose_class == 7:
        player_class[name] = "Berserker"
    elif choose_class == 8:
        player_class[name] = "Lich"
    else:
        print("Harap masukkan angka yang valid untuk kelas pemain!")
        return
    
def Class_Status(PlayerList):
    for i in range(len(PlayerList)):
        if player_class[PlayerList[i]['name']] == "Warrior":
            setPlayer(PlayerList[i], 'damage', PlayerList[i]['damage'] + int(PlayerList[i]['damage'] * 0.1))
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] + 10)

        elif player_class[PlayerList[i]['name']] == "Assassin":
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] - 25)

        elif player_class[PlayerList[i]['name']] == "Archer":
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] - 25)
        
        elif player_class[PlayerList[i]['name']] == "Tanker":
            setPlayer(PlayerList[i], 'damage', PlayerList[i]['damage'] - int(PlayerList[i]['damage'] * 0.2))
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] + 50)

        elif player_class[PlayerList[i]['name']] == "Wizard":
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] - 25)
            
        elif player_class[PlayerList[i]['name']] == "Lich":
            setPlayer(PlayerList[i], 'health', PlayerList[i]['health'] - 25)

def Passive(attacker, target):
    import random as rd
    lich_ressurect = 1
    player_class_attacker = player_class[attacker['name']]
    player_class_target = player_class[target['name']]

    if player_class_target == "Assassin" and rd.random() < 0.4:
        print(f"{target['name']} berhasil menghindari serangan!")
        return True

    if player_class_attacker == "Archer" and rd.random() < 0.25:
        setPlayer(attacker, 'damage', attacker['damage'] * 2)
        print(f"Kamu berhasil meningkatkan damagemu! Damage sekarang: {attacker['damage']}")

    if player_class_attacker == "Paladin":
        heal = int(target['health'] * 0.05)
        setPlayer(attacker, 'health', min(100, attacker['health'] + heal))
        print(f"{attacker['name']} mendapatkan heal sebesar {heal}!")

    if player_class_attacker == "Wizard" and rd.random() < 0.25:
        reflection = int(target['damage'] * 0.5)
        setPlayer(target, 'health', target['health'] - reflection)
        print(f"Woi {target['name']} Rasakan skillmu sendiri\n{target['name']} terkena damage sebesar {reflection}!")
        
    if player_class_attacker == "Berserker" and attacker['health'] < 50:
        setPlayer(attacker, 'damage', attacker['damage']+10)
        print(f"{attacker['name']} menjadi marah dan meningkatkan damage sebesar 10!")

    if player_class_attacker == "Lich":
        if lich_ressurect == 1 and attacker['health'] <= 0 and rd.random() < 0.3:
            setPlayer(attacker, 'health', int(attacker['health']*0.5))
            setPlayer(attacker, 'damage', int(attacker['damage']*0.75))
            lich_ressurect = 0
            print(f"{attacker['name']} berhasil menghidupkan dirinya!")
    
    if player_class_attacker == "Tanker":
        defense_tanker = int(attacker['defense_power']*0.2)
        setPlayer(attacker, 'defense_power', int(attacker['defense_power'] + defense_tanker))
        print(f"{attacker['name']} menambah defense sebesar {defense_tanker}!")
    
items = {
    "health_potion": {"name": "Health Potion", "heal": 20, "description": "Menyembuhkan 20 HP."},
    "damage_potion": {"name": "Damage Potion", "damage_boost": 5, "description": "Meningkatkan damage sebesar 5."},
}

def get_random_item():
    import random as rd
    if rd.random() < 0.5: 
        item_key = rd.choice(list(items.keys()))
        return items[item_key]
    return None
