# Python Workshop 3: Scenario 2
print("Welcome to the game!")
b = input("Would you want to play the game? Say Yes or No: ")

loading_screen = 0
if b == "Yes":
    while loading_screen < 101:
        print(loading_screen)
        loading_screen += 1
else:
    print("Exiting the game")
    exit