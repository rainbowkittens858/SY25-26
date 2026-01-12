lineup = [("Code Play", "Indie", 30), 
          ("The Pythonistas", "Rock", 45),
          ("Syntax Error", "Metal", 60)]

def add_to_lineup(band):
    lineup.append(band)

def emergency_swap(band):
    lineup.pop(0)
    lineup.append(band)

def remove_band(index):
    lineup.remove(lineup[index])

def calculate_time():
    totaltime = 0
    for i in range(len(lineup)):
        try:
            time = lineup[i][2]
        except IndexError:
            time = 0
        totaltime = totaltime + time
    return totaltime

print(lineup)
add_to_lineup(("The Byte Beats",))
print(lineup)
emergency_swap(lineup[0])
print(lineup)
remove_band(0)
print(lineup)
print(calculate_time())