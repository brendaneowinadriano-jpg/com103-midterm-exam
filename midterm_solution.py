# HERO ROSTER
heroes = [
    [1, "Layla", "Marksman"],
    [2, "Tigreal", "Tank"],
    [3, "Gusion", "Assassin"],
    [4, "Kagura", "Mage"],
    [5, "Chou", "Fighter"]
]

# IGN and RANK
ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

# HERO ROSTER
print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for hero in heroes:
    print(f" {hero[0]}. {hero[1]:<10} [{hero[2]}]")

print("==========================================\n")

# WINS/LOSSES and Match Logs
match_logs = []
wins = 0
losses = 0

# LOOP FOR 4 MATCHES
for i in range(1, 5):
    print(f"--- MATCH {i} ---")
    hero_num = int(input("Hero number (0 to skip): "))

    if hero_num == 0:
        print()
        continue

    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()

        # FIX DEATHS = 0
        if deaths == 0:
            deaths = 1

        # COMPUTE KDA
        kda = (kills + assists) / deaths

        # PERFORMANCE TAG
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        # COUNT WINS/LOSSES
        if result == "W":
            wins += 1
        else:
            losses += 1

        # GET HERO NAME
        hero_name = heroes[hero_num - 1][1]

        # STORE DATA
        match_logs.append({
            "hero": hero_name,
            "kda": kda,
            "result": result,
            "tag": tag
        })

    print()

# Matches Played
matches_played = len(match_logs)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
else:
    win_rate = 0

# BEST MATCH
best_match = None
highest_kda = 0

for index, match in enumerate(match_logs):
    if match["kda"] > highest_kda:
        highest_kda = match["kda"]
        best_match = (index + 1, match)

# RESULT
print("\n=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i, match in enumerate(match_logs, start=1):
    result_text = "WIN" if match["result"] == "W" else "LOSS"
    print(f"[{i}] {match['hero']:<10} | KDA: {match['kda']:.2f} | {result_text:<4} | {match['tag']}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if best_match:
    print(f"Best Match     : [{best_match[0]}] {best_match[1]['hero']}  (KDA: {best_match[1]['kda']:.2f})")

print("=============================================")
