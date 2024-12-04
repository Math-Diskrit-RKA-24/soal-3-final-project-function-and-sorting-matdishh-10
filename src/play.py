import game as gm
import random as rd

gm.initPClass()
def inputData():
    jumlah_player = 2
    gm.initPlayers()

    for i in range(1, jumlah_player + 1):
        print(f"\nMasukkan data untuk pemain ke-{i}")
        name = input("Nama pemain: ")
        try:
            damage = int(input("Damage pemain [1-20]: "))
            defense_power = int(input("Defense Power pemain [1-10]: "))
            gm.ChooseClass(name)
            
        except ValueError:
            print("Harap masukkan angka yang valid untuk damage dan defense power!")
            return
        gm.addPlayer(gm.createNewPlayer(name, damage, defense_power))
        
    gm.Class_Status(gm.PlayerList)

    print("\nSemua pemain berhasil ditambahkan!")
    print("Daftar Pemain:")

    for player in gm.PlayerList:
        print(f"Nama: {player['name']}, Score: {player['score']}, Damage: {player['damage']}, Health: {player['health']}, Defense Power: {player['defensePower']}, Defense: {player['defense']}, Class: {gm.player_class[player['name']]}")

# manual play
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
        print("(1) Serang")
        print("(2) Bertahan")
        print("(3) Gunakan Item")
        
        try:
            dodge = 0
            action = int(input("Masukkan pilihan Anda: "))
            gm.Passive(attacker, target)
            if action == 1:
                # Serangan
                print(f"{attacker['name']} menyerang {target['name']}.")
                # dodge = gm.Passive(attacker, target)
                if gm.player_class[attacker['name']] == "Assassin":
                    dodge = gm.Passive(attacker, target)
                
                if dodge:
                    print(f"{target['name']} berhasil menghindar!")
                else:
                    gm.attackPlayer(attacker, target)
                    print(f"{attacker['name']} menyerang {target['name']}!")
                
                new_item = gm.get_random_item()
                if new_item: 
                    print(f"Anda mendapatkan item: {new_item['name']} - {new_item['description']}")
            elif action == 2:
                # Bertahan
                gm.setPlayer(attacker, 'defense', True)
                print(f"{attacker['name']} memilih untuk bertahan!")
            elif action == 3:
                if new_item:
                    if 'Health Potion' in new_item:
                        attacker['health'] += new_item['heal']
                        print(f"{attacker['name']} menggunakan {new_item['name']} dan menyembuhkan {new_item['heal']} HP!")
                    elif 'Damage Potion' in new_item:
                        attacker['damage'] += new_item['damage_boost']
                        print(f"{attacker['name']} menggunakan {new_item['name']} dan meningkatkan damage sebesar {new_item['damage_boost']}!")
        except ValueError:
            print("Masukkan angka yang valid. Giliran dilewati.")
        
        # Menampilkan status pemain
        print(f"\nStatus {attacker['name']}: Health = {attacker['health']}, Score = {attacker['score']}")
        print(f"Status {target['name']}: Health = {target['health']}, Score = {target['score']}")
        
        # Perpindahan giliran
        turn += 1

    # Menampilkan hasil pertandingan
    print("\n==========Pertandingan selesai!==========")
    gm.displayMatchResult()

# Panggil fungsi manual gameplay
inputData()
manualGamePlay()
