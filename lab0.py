counter = 0
with open("siege_log.txt", "r") as f:
    for inp_data in f:
        if inp_data == "# siege log — castle Ravenholm, server GAME-EU-3, 2026-09-05 21:00 UTC" \
        or inp_data == "Player | Base_Damage | Weapon_State | Buffs":
            continue

        if '|' not in inp_data:
            print("[ОШИБКА] Данные имеют неверный разделитель.")
            continue

        inp_data = inp_data.strip().split("|")
        inp_data = [x.strip() for x in inp_data]

        if len(inp_data) < 3:
            print("[ОШИБКА] Недостаточно данных для обработки.")
            continue

        if inp_data[-1] == "N/A":
            inp_data[-1] = 0

        if len(inp_data) == 3:
            inp_data.append(0)

        if len(inp_data) > 4:
            inp_data = inp_data[:4]

        try:
            inp_data[1] = float(inp_data[1])
            inp_data[-1] = float(inp_data[-1])
        except:
            print("[ОШИБКА] Урон и баффы должны быть числами.")
            continue
            

        if inp_data[2].lower() not in ["active", "broken"] or any(x not in inp_data[0] for x in ["[", "]"]):
            print("[ОШИБКА] Неверный формат данных.")
            continue
            
        def damage_counter(base_dam, status, buffs):
            sost = 1.5 if status.lower() == "active" else 0.5
            result = base_dam * sost * (1 + 0.15 * buffs)
            return round(result, 2)

        nickname = inp_data[0].split(']')[1]
        guild = inp_data[0].split(']')[0][1:]
        damage = damage_counter(inp_data[1], inp_data[2], inp_data[3])

        counter += 1
        print(f"Игрок {nickname} из гильдии {guild} нанес {damage} урона по воротам.")

print("Обработано: ", counter)