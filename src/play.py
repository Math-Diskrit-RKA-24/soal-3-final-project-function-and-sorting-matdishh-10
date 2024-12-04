import game as gm
import random as rd

player_class = {}

def inputData():
    jumlah_player = 2
    gm.initPlayers()

    for i in range(1, jumlah_player + 1):
        print(f"\nMasukkan data untuk pemain ke-{i}")
        name = input("Nama pemain: ")
        try:
            damage = int(input("Damage pemain: "))
            defense_power = int(input("Defense Power pemain: "))
            choose_class = int(input("(1) Warrior\n(2) Assassin\n(3) Archer\n(4) Paladin\n(5) Tanker\n(6) Wizard\nMasukkan kelas pemain : "))
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
            else:
                print("Harap masukkan angka yang valid untuk kelas pemain!")
                return
        except ValueError:
            print("Harap masukkan angka yang valid untuk damage dan defense power!")
            return
        gm.addPlayer(gm.createNewPlayer(name, damage, defense_power))

    for i in range(jumlah_player):
        if player_class[gm.PlayerList[i]['name']] == "Warrior":
            gm.setPlayer(gm.PlayerList[i], 'damage', gm.PlayerList[i]['damage'] + int(gm.PlayerList[i]['damage'] * 0.1))
            gm.setPlayer(gm.PlayerList[i], 'health', gm.PlayerList[i]['health'] + 10)

        elif player_class[gm.PlayerList[i]['name']] == "Assassin":
            gm.setPlayer(gm.PlayerList[i], 'health', gm.PlayerList[i]['health'] - 25)

        elif player_class[gm.PlayerList[i]['name']] == "Archer":
            gm.setPlayer(gm.PlayerList[i], 'health', gm.PlayerList[i]['health'] - 25)
        
        elif player_class[gm.PlayerList[i]['name']] == "Tanker":
            gm.setPlayer(gm.PlayerList[i], 'damage', gm.PlayerList[i]['damage'] - int(gm.PlayerList[i]['damage'] * 0.2))
            gm.setPlayer(gm.PlayerList[i], 'health', gm.PlayerList[i]['health'] + 50)

        elif player_class[gm.PlayerList[i]['name']] == "Wizard":
            gm.setPlayer(gm.PlayerList[i], 'health', gm.PlayerList[i]['health'] - 25)

    print("\nSemua pemain berhasil ditambahkan!")
    print("Daftar Pemain:")

    for player in gm.PlayerList:
        print(f"Nama: {player['name']}, Score: {player['score']}, Damage: {player['damage']}, Health: {player['health']}, Defense Power: {player['defensePower']}, Defense: {player['defense']}, Class: {player_class[player['name']]}")

def Passive(attacker, target):
    player_class_attacker = player_class[attacker['name']]
    player_class_target = player_class[target['name']]

    if player_class_target == "Assassin" and rd.random() < 0.4:
        print(f"{target['name']} berhasil menghindari serangan!")
        return True

    if player_class_attacker == "Archer" and rd.random() < 0.25:
        attacker['damage'] = int(attacker['damage'] * 2)
        print(f"{attacker['name']} mendapatkan critical hit dengan damage {attacker['damage']}!")

    if player_class_attacker == "Paladin":
        heal = int(attacker['damage'] * 0.1)
        attacker['health'] = min(100, attacker['health'] + heal)
        print(f"{attacker['name']} mendapatkan heal sebesar {heal}!")

    if player_class_attacker == "Wizard" and rd.random() < 0.5:
        burn_damage = int(target['health'] * 0.1)
        target['health'] -= burn_damage
        print(f"{target['name']} terkena burn damage sebesar {burn_damage}!")
    
    return False

inputData()

# ================================ Auto Gameplay ===============================
# first_attacker = rd.choice(gm.PlayerList)
# second_attacker = gm.PlayerList[1] if first_attacker == gm.PlayerList[0] else gm.PlayerList[0]

# print(f"\nPemain pertama yang menyerang adalah {first_attacker['name']}!")

# turn = 0
# while gm.PlayerList[0]['health'] > 0 and gm.PlayerList[1]['health'] > 0:
#     attacker = first_attacker if turn % 2 == 0 else second_attacker
#     target = second_attacker if turn % 2 == 0 else first_attacker

#     # Cek apakah attacker menjadi defensif
#     if rd.random() < 0.5:
#         gm.setPlayer(attacker, 'defense', True)
#         print(f"{attacker['name']} memilih untuk menjadi defensif dan tidak menyerang!")
#         turn += 1
#         continue

#     print(f"\n{attacker['name']} menyerang {target['name']}.")
#     dodge = Passive(attacker, target)
#     if dodge:
#         turn += 1
#         continue

#     gm.attackPlayer(attacker, target)

#     print(f"Status {attacker['name']}: Health = {attacker['health']}, Score = {attacker['score']}")
#     print(f"Status {target['name']}: Health = {target['health']}, Score = {target['score']}")

#     turn += 1

# ============================== Manual Gameplay =============================
def manualGamePlay():
    # Memilih penyerang pertama secara acak
    first_attacker = rd.choice(gm.PlayerList)
    second_attacker = gm.PlayerList[1] if first_attacker == gm.PlayerList[0] else gm.PlayerList[0]

    print(f"\nPemain pertama yang menyerang adalah {first_attacker['name']}!")

    turn = 0
    while gm.PlayerList[0]['health'] > 0 and gm.PlayerList[1]['health'] > 0:
        attacker = first_attacker if turn % 2 == 0 else second_attacker
        target = second_attacker if turn % 2 == 0 else first_attacker

        print(f"\nGiliran {attacker['name']}")
        print("Pilih tindakan:")
        print("1. Serang")
        print("2. Bertahan")
        print("3. Kemampuan Pasif")
        
        try:
            action = int(input("Masukkan pilihan Anda: "))
            if action == 1:
                # Serangan
                print(f"{attacker['name']} menyerang {target['name']}.")
                dodge = Passive(attacker, target)
                if dodge:
                    print(f"{target['name']} berhasil menghindar!")
                else:
                    gm.attackPlayer(attacker, target)
                    print(f"{attacker['name']} menyerang {target['name']}!")
            elif action == 2:
                # Bertahan
                gm.setPlayer(attacker, 'defense', True)
                print(f"{attacker['name']} memilih untuk bertahan!")
            elif action == 3:
                # Kemampuan Pasif
                print(f"{attacker['name']} mencoba menggunakan kemampuan pasif.")
                Passive(attacker, target)
            else:
                print("Pilihan tidak valid. Lewati giliran.")
        except ValueError:
            print("Masukkan angka yang valid. Giliran dilewati.")
        
        # Menampilkan status pemain
        print(f"\nStatus {attacker['name']}: Health = {attacker['health']}, Score = {attacker['score']}")
        print(f"Status {target['name']}: Health = {target['health']}, Score = {target['score']}")
        
        # Perpindahan giliran
        turn += 1

    # Menampilkan hasil pertandingan
    print("\nPertandingan selesai!")
    gm.displayMatchResult()

# Panggil fungsi manual gameplay
manualGamePlay()

# Display Result
print("\nPertandingan selesai!")
gm.displayMatchResult()
