import random

choices = {1: 10, 2: 100, 3: 1000, 4: 10000, 5: 100000}  # Available Options and their box numbers
keys = list(choices.keys())
values = list(choices.values())
# random.shuffle(keys)
# random.shuffle(values)

# Algorithm for shuffling the numbers and their values
newChoices = dict()
for i in range(1, 6):  # 'i' is an iterating variable for FOR loop
    x = random.choice(keys)  # 'x' and 'y' are variables to update keys and values of choices
    keys.remove(x)
    y = random.choice(values)
    values.remove(y)
    newChoices.update({x: y})

txt = f"The available boxes are: {list(choices.keys())}\nThe available prizes are: {list(choices.values())}\n"
print(txt)
print("These amounts are jumbled in the given boxes randomly.")


def choose():
    global userChoice
    userChoice = int(input("Choose a box:"))
    return userChoice


ans = "n"
while (ans.upper() == "N"):
    choose()
    ans = input("Do you confirm your choice?[Y/N]")
else:
    print("Congratulations, You have chosen box number", userChoice)
saveBox = (userChoice, newChoices[userChoice])

keys = list(choices.keys())
values = list(choices.values())
keys.remove(userChoice)


def round(num, boxNum):
    global prompt
    txt = f'Welcome to Round {num}. You have to choose {boxNum} boxes.'
    print(txt)
    for i in range(boxNum):
        choose()
        ans = 'n'
        while (ans.upper() == "N"):
            ans = input("Do you confirm your choice?[Y/N]:")
        # ans = "n"
        # while (ans.upper() == "N"):
        #     if (newChoices[userChoice] > 1000):
        #         prompt = input("Do you want to exchange boxes?")
        #         ans = input("Do you confirm your choice?[Y/N]:")
        txt = f'You chose box number {userChoice}. The prize inside box number was {newChoices[userChoice]}'
        print(txt)
        keys.remove(userChoice)
        values.remove(newChoices[userChoice])
        txt = f"The available boxes are: {keys}\nThe available prizes are: {values}\n"
        print(txt)
    print("\n")


# # print(newChoices)
# round(1, 2)
# round(2, 1)
# round(3, 1)

round_number = 0
while (len(keys) != 0):
    round_number += 1
    round(round_number, 1)

print(f"Your box was {saveBox[0]}. You have won {saveBox[1]}")
if (saveBox[1>1000]):
    print("Congratulations!")
else:
    print("Better luck next time!")
