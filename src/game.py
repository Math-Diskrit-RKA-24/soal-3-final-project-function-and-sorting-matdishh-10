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
