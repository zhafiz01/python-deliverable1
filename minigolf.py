print("Welcome to GC mini golf!")
player_name = input("What is your name?\n")
num_holes = int(input(f"Hi, {player_name}! Would you like to play 3 or 6 holes?\n"))

total_par = num_holes * 3
total_putts = 0

for hole in range(1, num_holes + 1):
    putts = int(input(f"How many putts for hole {hole}? (par: 3) \n"))
    total_putts += putts

par_score = total_putts - total_par
#Changes
if par_score > 0:
    print(f"Nice try, {player_name}... Your total score was: +{par_score}.")
elif par_score < 0:
    print(f"Great job, {player_name}! Your total score was: {par_score}.")
else:
    print(f"Good game, {player_name}. Your total score was: 0.")