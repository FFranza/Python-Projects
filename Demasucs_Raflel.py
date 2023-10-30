import random
import tkinter as tk
import time
participants = ['Juiccy', 'Juiccy', 'Ferzie', 'Ferzie', 'Seb', 'Seb', 'Neey', 'Neey', 'Neey', 'Hues', 'Hues', 'Sal', 'Sal', 'Dove', 'Dove', 'Tim', 'Xy', 'Xy', 'Phoebe', 'Gian', 'Gian', 'Jack', 'Jack', 'Zeek', 'Brad', 'Brad' ] # Dictionary Variable that contains all names for the raffle

def create_confetti(canvas): # Function that creates the confetti used when someone wins and controls the flow of confetti going down
    colors = ['red', 'green', 'blue', 'yellow', 'orange'] # Sets the colors of what the confetti will be using
    confetti_list = []

    for _ in range(100):
        x = random.randint(0,400)
        y = random.randint(0,400)
        color = random.choice(colors)
        size = random.randint(5, 20)
        confetti_list.append([x, y, size, color])
    
    while any (y < 400 for _, y, _, _ in confetti_list): # Allows for constant update on confetti slowly dropping down
        canvas.delete("confetti")
        for i, confetti in enumerate(confetti_list):
            x, y, size, color = confetti
            y += 1
            canvas.create_oval(x, y, x + size, y + size, fill=color, tags='confetti') # Creates the shape of the confetti
            confetti_list[i] = [x, y, size, color]
        canvas.update()
        time.sleep(0.02)

def conduct_raffle(): # Function that handles on performing the whole raffle and randomizes participants in the raffle
    global participants
    start_button.config(state=tk.DISABLED)
    
    canvas.delete("all")
                
    box_size = 200
    box_x = (canvas.winfo_width() - box_size) / 2
    box_y = (canvas.winfo_width() - box_size) / 2
    canvas.create_rectangle(box_x, box_y, box_x + box_size, box_y + box_size, fill="brown")
    
    random.shuffle(participants)
    
    for participant in participants:
        for i in range(len(participant) + 1):
            canvas.delete("all")
            
            canvas.create_rectangle(box_x, box_y, box_x + box_size, box_y + box_size, fill="brown")
            
            canvas.create_text(box_x + box_size / 2, box_y + box_size / 2, text=participant[:i], font=('Times New Roman', 16), fill='White')
            canvas.update()
            time.sleep(0.05)
        time.sleep(0.3)

    winner_lable.config(text="The Winner of the 2023 Hallooween Raflle is " + participant + "!", fg='Green')
    start_button.config(state=tk.NORMAL)
    create_confetti(canvas) 

root = tk.Tk() # Ties tk import to root variable
root.title("Raffle") # Set's title of GUI
root.configure(bg='black') # Set's GUI background color

canvas = tk.Canvas(root, width=400, height=400, bg='Black', highlightthickness=0) # Creating the canvas to input the box inside
canvas.pack(pady=20)

title_lable = tk.Label(root, text = "The Demasucs 2023 Hallooween Sweater Raffle Drawing", font=('Times New Roman', 18), fg='Dark Red', bg='Black')
title_lable.pack(pady=20)

start_button = tk.Button(root, text = "Start Raffle", command=conduct_raffle, font=('Times New Roman', 14), fg='Orange', bg='Black')
start_button.pack(pady=20)

winner_lable = tk.Label(root, text="", font=('Times New Roman', 16), fg ='White', bg='Black')
winner_lable.pack()

root.mainloop() # Calls the function for the program