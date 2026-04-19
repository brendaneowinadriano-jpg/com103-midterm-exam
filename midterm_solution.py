print("Mobile Legends Quick Match Log")
print("")

#IGN and RANK
ign=input("In-game Username: ")
rank=input("Rank: ")

#Hero Roster
print(f"==========================================")
print(f"      MOBILE LEGENDS -- HERO ROSTER       ")
print(f"==========================================")
print(f" 1. Layla       [Marksman]")
print(f" 2. Tigreal     [Tank]")
print(f" 3. Gusion      [Assassin]")
print(f" 4. Kagura      [Mage]")
print(f" 5. Chou        [Fighter]")
print(f"==========================================")

hero_roster=["",
            "Layla",
            "Tigreal",
            "Gusion",
            "Kagura",
            "Chou"]

match=1
log_number=0
match_log=[]
match_history=[]



while match <5:
    print("")
    print(f"---Match {match}---")
    
    hero_number= int(input("Hero number (0 to skip): "))
    if hero_number == 0:
        print("")
    
        
        
    
    if hero_number > 0 and hero_number <=5:
        
        #Kills
        kills= int(input("Kills: "))
        
        #Deaths
        deaths= int(input("Deaths: "))
        
        #Denominate 0 to 1
        if deaths == 0:
            deaths=1


        #Assists
        assists= int(input("Assists: "))

        #Results
        results= input("Result (W/L): ").upper()
        if results == "W":
            results= "Win"

        elif results == "L":
            results= "Loss"

        #Compute KDA
        kda=(kills+assists)/deaths

        #Performace Tags
        if kda >=5 and results == "Win":
            tag="DOMINATION!"
        if kda >=5 and results == "Loss":
            tag="Carried Hard"
        if kda <5 and results == "Win":
            tag="Team Effort"
        if kda <5 and results == "Loss":
            tag="Better Luck Next Game"
        
        #Log Number
        log_number +=1

       

    hero_name= hero_roster[hero_number]


    if hero_number > 0 and hero_number <=5:
        match_log.append([log_number, hero_name, kda , results, tag])

    
    match +=1

#Computing Wins, Losses, Best KDA, Best Matc
wins = 0
losses = 0
best_kda = 0
best_match = None

print("=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for log in match_log:
    log_num, hero, kda, result, tag = log

    # Count wins/losses
    if result == "Win":
        wins += 1
        result_display = "WIN "
    else:
        losses += 1
        result_display = "LOSS"

    # Track best match
    if kda > best_kda:
        best_kda = kda
        best_match = log

    
    print(f"[{log_num}] {hero:<11} | KDA: {kda:.2f} | {result_display} | {tag}")

# Summary
total_matches = len(match_log)
win_rate = int((wins / total_matches) * 100)

print("---------------------------------------------")
print(f"Matches Played : {total_matches}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

# Best match display
if best_match:
    log_num, hero, kda, _, _ = best_match
    print(f"Best Match     : [{log_num}] {hero}  (KDA: {kda:.2f})")

print("=============================================")


