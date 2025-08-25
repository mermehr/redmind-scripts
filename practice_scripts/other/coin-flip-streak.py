import random

number_of_streaks = 0
total_experiments = 10000

for experiment_number in range(total_experiments):
    # Generate a list of 100 coin flips
    coin_flips = []
    for i in range(100):
        flip = 'H' if random.randint(0, 1) == 1 else 'T'
        coin_flips.append(flip)

    # Check for a streak of 6 in a row
    current_streak = 1  # start with 1 because we always compare to the previous flip
    found_streak = False

    for i in range(1, len(coin_flips)):
        if coin_flips[i] == coin_flips[i - 1]:
            current_streak += 1
            if current_streak == 6:
                found_streak = True
                break  # no need to check more; we found a streak
        else:
            current_streak = 1  # reset streak count

    if found_streak:
        number_of_streaks += 1

# Calculate chance
percentage = (number_of_streaks / total_experiments) * 100
print('Chance of streak: %s%%' % round(percentage, 2))
