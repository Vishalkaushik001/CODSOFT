import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from random import choice
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

root = tk.Tk()
root.title("Rock Paper Scissors")
root.attributes("-fullscreen", True)
root.configure(bg="#f0f8ff")

player_name = simpledialog.askstring("Welcome!", "Enter your name:")
if not player_name:
    player_name = "Player"


options = ["rock", "paper", "scissor"]
image_size = (150, 150)

# add three .png image named as rock.png , paper.png and scissor.png
images = {
    opt: ImageTk.PhotoImage(Image.open(f"{opt}.png").resize(image_size))
    for opt in options
}

tk.Label(
    root, text=f"Welcome, {player_name}! Let's Play Rock - Paper - Scissors",
    font=("Helvetica", 32, "bold"), bg="#f0f8ff", fg="#333"
).pack(pady=30)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

player_label = tk.Label(frame, text=f"{player_name}'s Choice", font=("Arial", 20), bg="#f0f8ff")
player_label.grid(row=0, column=0, padx=50)

cpu_label = tk.Label(frame, text="CPU's Choice", font=("Arial", 20), bg="#f0f8ff")
cpu_label.grid(row=0, column=2, padx=50)

player_image_label = tk.Label(frame, bg="#f0f8ff")
player_image_label.grid(row=1, column=0)

vs_label = tk.Label(frame, text="VS", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="black")
vs_label.grid(row=1, column=1)

cpu_image_label = tk.Label(frame, bg="#f0f8ff")
cpu_image_label.grid(row=1, column=2)

result_label = tk.Label(root, text="", font=("Arial", 26, "bold"), fg="blue", bg="#f0f8ff")
result_label.pack(pady=30)

def determine_winner(player, cpu):
    if player == cpu:
        return "It's a Tie!"
    elif (player == "rock" and cpu == "scissor") or \
         (player == "paper" and cpu == "rock") or \
         (player == "scissor" and cpu == "paper"):
        return f"{player_name} Wins!"
    else:
        return "CPU Wins!"

def play(choice_made):
    cpu_choice = choice(options)
    player_image_label.config(image=images[choice_made])
    cpu_image_label.config(image=images[cpu_choice])
    result = determine_winner(choice_made, cpu_choice)
    result_label.config(text=f"CPU chose {cpu_choice.capitalize()}\n{result}")

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=20)

for opt in options:
    btn = tk.Button(
        button_frame,
        image=images[opt],
        command=lambda opt=opt: play(opt),
        bd=0,
        bg="#f0f8ff",
        activebackground="#d1e0e0"
    )
    btn.pack(side=tk.LEFT, padx=30)

def reset_game():
    player_image_label.config(image="")
    cpu_image_label.config(image="")
    result_label.config(text="")

def exit_game():
    if messagebox.askyesno("Exit Game", "Do you really want to quit?"):
        root.destroy()

control_frame = tk.Frame(root, bg="#f0f8ff")
control_frame.pack(pady=20)

tk.Button(
    control_frame, text="Reset", command=reset_game,
    font=("Arial", 16), bg="#32cd32", fg="white", padx=20, pady=10
).pack(side=tk.LEFT, padx=20)

tk.Button(
    control_frame, text="Exit", command=exit_game,
    font=("Arial", 16), bg="red", fg="white", padx=20, pady=10
).pack(side=tk.LEFT, padx=20)

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
