print("Mobile Legends Quick Match Log")
print("")

#IGN and RANK
ign=input("In-game Username: ")
rank=input("Rank: ")

#Hero Roster Display
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
