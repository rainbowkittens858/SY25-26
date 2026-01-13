def add_to_lineup(lineup):
    band_name = input("Enter the band name: ")
    band_genre = input("Enter the band genre: ")
    band_time = int(input("Enter the time the band will perform: "))
    band_info = (band_name, band_genre, band_time)
    lineup.append(band_info)
    print(f"{band_name} added successfully! View the new list by choosing option 1.")
    return lineup

def emergency_swap(lineup):
    band_name = lineup[0][0]
    first_band = lineup.pop(0)
    lineup.append(first_band)
    print(f"{band_name} moved to the end. View the new list by choosing option 1.")
    return lineup

def remove_band(lineup):
    band_name = input("What is the name of the band?: ")
    for item in lineup:
        if item[0] == band_name:
            band = item
    index = lineup.index(band)
    lineup.remove(lineup[index])
    print(f"{band_name} removed from the list. View the new list by choosing option 1.")
    return lineup

def move_band(lineup):
    index = int(input("What is the current place of the band?: "))
    index -= 1
    new_index = int(input("Where would you like to move the band to?: "))
    new_index -= 1
    band_name = lineup[index][0]
    band_info = lineup.pop(index)
    lineup.insert(new_index, band_info)
    print(f"{band_name} moved from {index + 1} to {new_index + 1}. View the new list by choosing option 1.")
    return lineup

def calculate_time():
    totaltime = 0
    for i in range(len(lineup)):
        try:
            time = lineup[i][2]
        except IndexError:
            time = 0
        totaltime = totaltime + time
    return totaltime

def view_lineup(lineup):
    print("")
    print("Pyfest 2026 Lineup:")
    for i in range(len(lineup)):
        print(f"{(i + 1)}. {lineup[i][0]} ({lineup[i][1]}) - {lineup[i][2]} mins")
    total_time = calculate_time()
    print(f"Total Festival Duration: {total_time} minutes")

def pyfest_menu():
    print("--- Pyfest 2026 Stage Manager ---")
    print("1. View Lineup & Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival).")
    print("4. Remove a Band by Name")
    print("5. Move Band to Specific Position")
    print("6. Exit")

print("Welcome to the Pyfest Stage Manager!")

lineup = [("Code Play", "Indie", 30), 
          ("The Pythonistas", "Rock", 45),
          ("Syntax Error", "Metal", 60)]

while True:
    print("")
    pyfest_menu()
    choice = int(input("Choose an option(1-6): "))
    if choice == 1:
        view_lineup(lineup)
    elif choice == 2:
        lineup = add_to_lineup(lineup)
    elif choice == 3:
        lineup = emergency_swap(lineup)
    elif choice == 4:
        lineup = remove_band(lineup)
    elif choice == 5:
        lineup = move_band(lineup)
    elif choice == 6:
        print("Shutting down Pyfest Manager . . .")
        break