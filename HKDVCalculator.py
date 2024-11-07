import argparse
import os 
os.system("HKDVCalculator 0.0")


logo = """
 _   _         _  _          _   __ _ 
 | | | |  ___  | || |  ___   | | / /(_)  _     _ 
 | |_| | / _ \ | || | / _ \  | |/ /  _ _| |_ _| |_  _  _ 
 |  _  |/ /_\ \| || |/ / \ \ |   /  | |_   _|_   _|| |/ /
 | | | |\ ,___/| || |\ \_/ / | |\ \ | | | |_  | |_ | / /
 |_| |_| \___/ |_||_| \___/  |_| \_\|_| \___| \___||  / 
                         created by github.com/djjunko            
"""


print("\033[38;5;13m" + logo + "\033[0m")






#main code 

while True:
  
    rarity_value = 0
    source_value = 0
    time_factor = 0
    supply_demand_factor = 0

   
    reset_choice = input("Welcome, Press enter to start! :)").strip().lower()
    
    if reset_choice == 'y':
        print(" You can restart.")
     

  
    rarity = input("Enter the item's rarity (Super Rare, Rare, Common): ").strip().lower()
    source = input("Enter the item's source (Event, Regular, Limited-Time): ").strip().lower()
    time_factor = float(input("Enter the time factor (e.g., 1 for recent, 2 for older items): "))
    supply_demand_factor = float(input("Enter the supply and demand factor (e.g., 1 for low demand, 2 for high demand): "))

  
    if rarity == "super rare":
        rarity_value = 4
    elif rarity == "rare":
        rarity_value = 2
    elif rarity == "common":
        rarity_value = 1
    else:
        print("Invalid rarity input. Assuming 'Common' value.")
        rarity_value = 1


    if source == "event":
        source_value = 2
    elif source == "regular":
        source_value = 1
    elif source == "limited-time":
        source_value = 3
    else:
        print("Invalid source input. Assuming 'Regular' source.")
        source_value = 1

   
    projected_value = rarity_value * source_value * time_factor

  
    community_value = projected_value * supply_demand_factor

   
    print(f"\nProjected Value of the item: {projected_value}")
    print(f"Community Value of the item: {community_value}")

  
    again = input("\nDo you want to enter another item? (y/n): ").strip().lower()
    if again != 'y':
        break