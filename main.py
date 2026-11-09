import random
import sys
import time

def typewriter(text, speed=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()


# ---------------------------------------------------------------------------
# MARKET DATA (Hardware & Software - Casual Edition)
# ---------------------------------------------------------------------------
hardware_parts = {
    # LEVEL 1 — BASIC
    "Standard Arm": ["basic arm, gets the job done and doesnt break easy", 100, {"strength": 10, "durability": 10}],
    "Heavy Arm": ["thick metal arm, a bit heavy but hits harder", 125, {"strength": 15, "durability": 15}],
    "Lightweight Arm": ["skinny arm, swings fast but snaps if you hit something too hard", 125, {"strength": 12, "durability": 5}],
    "Standard Leg": ["regular ol leg, keeps you balanced", 100, {"speed": 10, "stability": 10}],
    "Reinforced Leg": ["sturdy leg frame, wont wobble when you land", 125, {"speed": 8, "stability": 15}],
    "Lightweight Leg": ["light leg built for running fast", 125, {"speed": 15, "stability": 5}],
    "Basic Torso": ["standard bot body, nothing fancy", 150, {"health": 100, "energy": 50}],
    "Reinforced Torso": ["thick chest plating, takes a decent beating", 175, {"health": 140, "energy": 40}],
    "Basic Head": ["simple head casing with basic sensors", 100, {"brain_slots": 2}],
    "Focus Head": ["head with a slightly better view of things", 125, {"brain_slots": 3}],

    # LEVEL 2 — IMPROVED
    "Hydraulic Arm": ["pumped-up arm with some real hydro power behind it", 350, {"strength": 25, "durability": 20}],
    "Rapid Arm": ["fast arm with quick mechanical joints", 375, {"strength": 20, "durability": 15}],
    "Impact Arm": ["arm built to absorb shock so your joints dont rattle", 400, {"strength": 30, "durability": 25}],
    "Spring Leg": ["springy leg that cushions landings nicely", 350, {"speed": 20, "stability": 18}],
    "Stabilizer Leg": ["leg with extra joints to keep you planted", 375, {"speed": 18, "stability": 25}],
    "Sprint Leg": ["fast leg with high-output actuators for zooming around", 400, {"speed": 28, "stability": 12}],
    "Armored Torso": ["body bolted down with extra metal plates", 450, {"health": 200, "energy": 60}],
    "Compact Torso": ["smaller body frame, lighter overall mass", 400, {"health": 170, "energy": 80}],
    "Scanner Head": ["head with a wider sensor reach", 350, {"brain_slots": 4}],
    "Targeting Head": ["head with a sharp optical lens for spotting enemies", 425, {"brain_slots": 5}],

    # LEVEL 3 — ADVANCED
    "Titanium Arm": ["lightweight titanium alloy arm, super strong", 900, {"strength": 45, "durability": 40}],
    "Dual-Piston Arm": ["double piston setup, hits like a sledgehammer", 1000, {"strength": 55, "durability": 35}],
    "Precision Arm": ["high-end arm with smooth joints and zero lag", 950, {"strength": 50, "durability": 45}],
    "Shock Absorber Leg": ["leg packed with heavy shock absorbers to eat up impact", 900, {"speed": 35, "stability": 40}],
    "Reflex Leg": ["twitchy responsive leg that reacts super quick", 950, {"speed": 40, "stability": 35}],
    "Power Leg": ["heavy leg driven by heavy-duty hydraulics", 1000, {"speed": 45, "stability": 50}],
    "Titanium Torso": ["solid titanium chest piece, great weight-to-strength ratio", 1200, {"health": 320, "energy": 100}],
    "Reinforced Core Torso": ["multi-layer frame protecting your middle real good", 1300, {"health": 380, "energy": 90}],
    "Thermal Scanner Head": ["head with built-in thermal heat vision", 950, {"brain_slots": 6}],
    "Tactical Head": ["head loaded with a bunch of detection gear", 1100, {"brain_slots": 7}],

    # LEVEL 4 — ELITE
    "Ceramic Alloy Arm": ["arm lined with heat-resistant ceramic and tough alloy", 2500, {"strength": 75, "durability": 70}],
    "Industrial Crusher Arm": ["industrial-grade crusher arm with a massive reinforced piston", 2700, {"strength": 85, "durability": 65}],
    "Speed-Frame Arm": ["super responsive arm built from light composite materials", 2600, {"strength": 70, "durability": 60}],
    "Carbon Fiber Leg": ["advanced carbon composite leg, super light and tough", 2400, {"speed": 65, "stability": 60}],
    "Boost Leg": ["leg strapped with mini thrusters for explosive dashes", 2800, {"speed": 80, "stability": 65}],
    "Stomp Leg": ["heavy leg with thick foot plating for landing hard", 2500, {"speed": 60, "stability": 80}],
    "Layered Composite Torso": ["layered armor body mixing light alloys with impact-resistant stuff", 3000, {"health": 550, "energy": 150}],
    "Reactor Torso": ["body housing a huge power cell and cooling system", 3200, {"health": 480, "energy": 220}],
    "Multi-Lens Head": ["head equipped with optical, infrared, and depth sensors", 2600, {"brain_slots": 8}],
    "Shielded Command Head": ["protected head assembly with internal wiring guarded against interference", 2900, {"brain_slots": 9}],

    # LEVEL 5 — LEGENDARY
    "Titanium-Carbon Arm": ["ultra-dense titanium-carbon arm, absolute beast of a limb", 7500, {"strength": 110, "durability": 100}],
    "Overdrive Arm": ["experimental arm with variable pressure hydraulics that flex on demand", 8500, {"strength": 130, "durability": 90}],
    "Rigid Strike Arm": ["precision frame built for maximum energy absorption on impact", 8000, {"strength": 120, "durability": 110}],
    "Magnetic Suspension Leg": ["experimental leg using magnetic suspension to float over bumps", 8500, {"speed": 110, "stability": 100}],
    "Mag-Drive Leg": ["ultra-light carbon leg with magnetic assisted actuators", 8000, {"speed": 125, "stability": 85}],
    "Juggernaut Leg": ["massive reinforced leg with industrial hydraulics", 9000, {"speed": 95, "stability": 130}],
    "Adamantium Torso": ["legendary dense alloy body with layered armor and heavy framing", 10000, {"health": 800, "energy": 300}],
    "Core Reactor Torso": ["torso packed with a high-density energy reactor and safe containment", 12000, {"health": 700, "energy": 450}],
    "Panoramic Sensor Head": ["high-end head housing panoramic optical arrays and infrared", 8500, {"brain_slots": 10}],
    "Overclocked Brain Head": ["experimental head with a fully shielded network and fast processing hardware", 11000, {"brain_slots": 12}]
}

software_market = {
    "Targeting v1.0": ["Improves attack accuracy and critical hit chance.", 150, 1, {"accuracy_boost": 10}],
    "Reflex Subroutine": ["Reduces incoming damage via predictive dodging.", 300, 2, {"defense_boost": 10}],
    "Overclock OS": ["Increases total energy pool and attack power.", 600, 3, {"energy_boost": 40, "power_boost": 15}],
    "AI Neural Net": ["Legendary core software providing maximum autonomous combat efficiency.", 2000, 5, {"accuracy_boost": 20, "defense_boost": 20, "power_boost": 30}]
}

# ---------------------------------------------------------------------------
# PLAYER & BOT CLASSES
# ---------------------------------------------------------------------------
class PlayerRobot:
    def __init__(self, name):
        self.name = name
        self.credits = 300  
        self.inventory = [] 
        self.software = []  
        
        self.max_health = 100
        self.health = 100
        self.max_energy = 50
        self.energy = 50
        self.strength = 15
        self.speed = 10
        self.durability = 10
        self.brain_slots = 2  
        self.used_slots = 0
        
        self.accuracy_boost = 0
        self.defense_boost = 0

    def recalculate_stats(self):
        self.max_health = 100
        self.max_energy = 50
        self.strength = 15
        self.speed = 10
        self.durability = 10
        self.brain_slots = 2
        self.accuracy_boost = 0
        self.defense_boost = 0

        for item in self.inventory:
            stats = hardware_parts[item][2]
            self.max_health += stats.get("health", 0)
            self.max_energy += stats.get("energy", 0)
            self.strength += stats.get("strength", 0)
            self.speed += stats.get("speed", 0)
            self.durability += stats.get("durability", 0)
            self.brain_slots += stats.get("brain_slots", 0)

        for sw in self.software:
            sw_stats = software_market[sw][3]
            self.max_energy += sw_stats.get("energy_boost", 0)
            self.strength += sw_stats.get("power_boost", 0)
            self.accuracy_boost += sw_stats.get("accuracy_boost", 0)
            self.defense_boost += sw_stats.get("defense_boost", 0)

        self.health = min(self.health, self.max_health)
        self.energy = min(self.energy, self.max_energy)

class EnemyRobot:
    def __init__(self, level):
        names = ["IronClaw", "ByteSmasher", "Vaporizer", "Crankshaft", "Nullifier", "CyberStalker", "Titanium Terror"]
        self.name = f"Unit-{random.randint(100,999)} {random.choice(names)}"
        self.level = level
        
        self.max_health = 80 + (level * 45)
        self.health = self.max_health
        self.max_energy = 40 + (level * 20)
        self.energy = self.max_energy
        self.strength = 12 + (level * 10)
        self.speed = 10 + (level * 8)
        self.durability = 8 + (level * 6)

# ---------------------------------------------------------------------------
# MENUS & STATUS
# ---------------------------------------------------------------------------
def view_status(player):
    print("\n" + "="*40)
    print(f" ROBOT STATUS: {player.name}")
    print("="*40)
    print(f" Credits     : {player.credits}")
    print(f" Health      : {player.health}/{player.max_health}")
    print(f" Energy      : {player.energy}/{player.max_energy}")
    print(f" Strength    : {player.strength}")
    print(f" Speed       : {player.speed}")
    print(f" Durability  : {player.durability}")
    print(f" Brain Slots : {player.used_slots}/{player.brain_slots}")
    print("-" * 40)
    print(" Hardware Installed:", player.inventory if player.inventory else "None (Barebones)")
    print(" Software Installed:", player.software if player.software else "None")
    print("="*40)

def hardware_store(player):
    while True:
        print("\n--- HARDWARE MARKET ---")
        print("1. Browse & Buy Components")
        print("2. Exit to Garage")
        choice = input("Select an option: ")
        
        if choice == "1":
            print("\nAvailable Parts:")
            parts_list = list(hardware_parts.keys())
            for idx, part in enumerate(parts_list, 1):
                desc, cost, stats = hardware_parts[part]
                print(f"[{idx}] {part} - {cost}¢ | {desc} | Stats: {stats}")
            
            p_choice = input("\nEnter part number to buy (or 'b' to go back): ")
            if p_choice.lower() == 'b':
                continue
            if p_choice.isdigit() and 1 <= int(p_choice) <= len(parts_list):
                chosen_part = parts_list[int(p_choice) - 1]
                cost = hardware_parts[chosen_part][1]
                if player.credits >= cost:
                    player.credits -= cost
                    player.inventory.append(chosen_part)
                    player.recalculate_stats()
                    print(f"\nSUCCESS: Installed {chosen_part}!")
                else:
                    print("\nERROR: Not enough credits!")
            else:
                print("\nInvalid choice.")
        elif choice == "2":
            break

def software_store(player):
    while True:
        print("\n--- SOFTWARE MARKET (Brain Upgrade) ---")
        print(f"Brain Slots Available: {player.brain_slots - player.used_slots}")
        print("1. Browse & Install Software")
        print("2. Exit to Garage")
        choice = input("Select an option: ")
        
        if choice == "1":
            print("\nAvailable Software:")
            sw_list = list(software_market.keys())
            for idx, sw in enumerate(sw_list, 1):
                desc, cost, slots_needed, stats = software_market[sw]
                print(f"[{idx}] {sw} - {cost}¢ | Slots: {slots_needed} | {desc}")
            
            s_choice = input("\nEnter software number to install (or 'b' to go back): ")
            if s_choice.lower() == 'b':
                continue
            if s_choice.isdigit() and 1 <= int(s_choice) <= len(sw_list):
                chosen_sw = sw_list[int(s_choice) - 1]
                desc, cost, slots_needed, stats = software_market[chosen_sw]
                
                if chosen_sw in player.software:
                    print("\nYou already have this software installed")
                elif (player.used_slots + slots_needed) > player.brain_slots:
                    print("\nERROR: Not enough brain capacity! Upgrade your Head hardware.")
                elif player.credits < cost:
                    print("\nERROR: Not enough credits!")
                else:
                    player.credits -= cost
                    player.software.append(chosen_sw)
                    player.used_slots += slots_needed
                    player.recalculate_stats()
                    print(f"\nSUCCESS: Uploaded {chosen_sw} to brain!")
            else:
                print("\nInvalid choice.")
        elif choice == "2":
            break

# ---------------------------------------------------------------------------
# FULLY AUTONOMOUS AI COMBAT
# ---------------------------------------------------------------------------
def run_combat(player):
    level = max(1, min(5, player.strength // 30 + 1))
    enemy = EnemyRobot(level)
    
    print(f"\n MATCH FOUND: {player.name} will be fighting -> Level {level} {enemy.name}!")
    typewriter(f"Time to see if {player.name} will do this for you.")
    time.sleep(1)
    print("-" * 50)
    
    player.health = player.max_health
    player.energy = player.max_energy
    
    turn = 1 if player.speed >= enemy.speed else 2
    round_num = 1
    
    while player.health > 0 and enemy.health > 0:
        print(f"\n--- Round {round_num} ---")
        time.sleep(1) 
        
        if turn == 1:
            if player.energy < 15:
                player.energy = min(player.max_energy, player.energy + 25)
                print(f".. .. {player.name}'s AI low-power protocol triggered: Recalibrating power cells (+25 Energy).")
            else:
                if player.energy >= 20 and (random.random() < 0.6 or "AI Neural Net" in player.software):
                    player.energy -= 20
                    base_dmg = random.randint(player.strength, player.strength + 25)
                    damage = base_dmg + int(player.accuracy_boost * 0.5)
                    enemy.health -= damage
                    print(f"POW! {player.name} executed a calculated hook, dealing {damage} damage!")
                else:
                    player.energy -= 8
                    damage = random.randint(player.strength // 2, player.strength)
                    enemy.health -= damage
                    print(f"SWOOSH... {player.name} lunged forward with a jab, landing for {damage} damage!")
            turn = 2
        else:
            if enemy.energy < 15:
                enemy.energy = min(enemy.max_energy, enemy.energy + 20)
                print(f"{enemy.name} steps back to recharge.")
            else:
                if enemy.energy >= 15 and random.random() < 0.5:
                    enemy.energy -= 15
                    mitigation = (player.durability // 4) + (player.defense_boost // 2)
                    damage = max(5, random.randint(enemy.strength, enemy.strength + 15) - mitigation)
                    player.health -= damage
                    print(f"POW!!! {enemy.name} threw a brutal hook! {player.name} has taken {damage} damage.")
                else:
                    enemy.energy -= 5
                    mitigation = (player.durability // 6) + (player.defense_boost // 3)
                    damage = max(3, random.randint(enemy.strength // 2, enemy.strength) - mitigation)
                    player.health -= damage
                    print(f"Thwack!.! {enemy.name} landed a fast jab for {damage} damage.")
            turn = 1

        print(f"   ↳ [Status] {player.name} HP: {max(0, player.health)}/{player.max_health} (EN: {player.energy}) | {enemy.name} HP: {max(0, enemy.health)}/{enemy.max_health} (EN: {enemy.energy})")
        round_num += 1

    print("\n" + "="*50)
    if player.health > 0:
        reward = level * 200
        player.credits += reward
        print(f"VICTORY! {player.name} was able to defeat {enemy.name}!")
        print(f"Reward: +{reward} credits.")
    else:
        penalty = 60
        player.credits = max(0, player.credits - penalty)
        print(f"DEFEAT... {player.name} was turned into scrap metal.")
        print(f"Emergency towing & repair fees cost you {penalty} credits :(")
    print("="*50)

# ---------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# ---------------------------------------------------------------------------
def main():
    print("========================================")
    print("            BOT SCRIPT ARENA            ")
    print("========================================")
    bot_name = input("Enter your robot's name: ").strip()
    while not bot_name:
        print("\nCome on! Stop being lazy and give your bot a name!\n")
        bot_name = input("Enter your robot's name: ").strip()
        
    my_bot = PlayerRobot(bot_name)
    typewriter(f"\nBefore creating your robot, we must ask something very important.")
    time.sleep(2)
    typewriter(f"Do you promise to us that you will treat {my_bot.name} well?")
    time.sleep(1)
    treat_well_inp = input("Answer: ")
    while treat_well_inp.lower().strip() != "yes":
        print("\nJust say 'yes'.")
        treat_well_inp = input("Answer: ")

    typewriter(f"Say HELLO to, {my_bot.name}! You have 300 credits to get {my_bot.name} geared up")
    time.sleep(1)
    typewriter("Spend it wisely.")
    time.sleep(2)
    

    while True:
        print(f"\n=== {my_bot.name.upper()} ===")
        print("1. View Robot Stats")
        print("2. Hardware Market (Arms, Legs, Torso, Head)")
        print("3. Software Market (Brain Upgrades & AI)")
        print("4. Enter Battle")
        print("5. Retire / Quit Game")
        
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == "1":
            view_status(my_bot)
        elif choice == "2":
            hardware_store(my_bot)
        elif choice == "3":
            software_store(my_bot)
        elif choice == "4":
            if not my_bot.inventory:
                print(f"\n WARNING: {my_bot.name} doesn't have any installations. Do you really want to do this?!")
                proceed = input("Send it into battle anyway? (y/n): ")
                if proceed.lower() != 'y':
                    continue
            run_combat(my_bot)
        elif choice == "5":
            print(f"\nPowering down {my_bot.name}. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid choice. Please pick between 1 and 5.")

if __name__ == "__main__":
    main()