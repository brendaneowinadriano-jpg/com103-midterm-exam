**This program is a Mobile Legends match tracker that records and analyzes your performance across 4 matches.**

**When you run it, it will ask for your:**
- In-game name (IGN).
- Current rank (e.g., Epic, Legend, Mythic).

**Then it shows a hero roster (Layla, Tigreal, Gusion, Kagura, Chou) using a loop.**

**After that, it lets you input data for 4 matches:**

- You choose a hero by number (or type 0 to skip a match).
- Enter kills, deaths, assists.
- Enter result (W or L).

 ** For each valid match, the program clculates your KDA using the formula:**
  - (kills + assists) ÷ deaths.
  (if deaths = 0, it uses 1 to avoid division error.
  
  - Performance tags:
  High KDA + Win → DOMINATION!
  High KDA + Loss → Carried Hard
  Low KDA + Win → Team Effort
  Low KDA + Loss → Better Luck Next Game

After all of the 4 matches, it:
- Counts total wins and losses.
- Computes your win rate (%).
- Finds the best match (highest KDA).

Finally, it prints a formatted match log showing:

- Your IGN and rank.
- Each match (hero, KDA, result, tag).
- Total matches played.
- Win/loss record.
- Win rate.
- Best match.
