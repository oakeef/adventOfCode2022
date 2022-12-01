elvesTotalCalories = []
calories = 0
with open('day1input.txt') as elvesList:
    for food in elvesList:
        if food.strip() != '':
            calories += int(food.strip())
        else: 
            elvesTotalCalories.append(calories)
            calories = 0

elvesTotalCalories.sort(reverse=True)
print(elvesTotalCalories[0])

top3ElvesCalories = elvesTotalCalories[0] + elvesTotalCalories[1] + elvesTotalCalories[2]
print(top3ElvesCalories)

