# Python Workshop 3: Scenario 2
print("Welcome to the game!")
b = input("Would you want to play the game? Say Yes or No: ") # Use input function to take in user response

loading_screen = 0 # Starts the baseline at 0
if b == "Yes": # If response is Yes then conditional statement satisfies with while loop
    while loading_screen < 101: # Specifically 101 because while loop ends a value below
        print(loading_screen)
        loading_screen += 1
else:
    print("Exiting the game") # If statement doesn't match the response, script exits
    exit