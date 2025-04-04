import tkinter as tk
import random
n = random.randint(1, 100)
attempts = 0
def check():
    global attempts
    guess = int(entry.get())
    attempts += 1
    if guess > n:
        result.set("Too large, try again.")
    elif guess < n:
        result.set("Too small, try again.")
    else:
        result.set(f"Correct! Number of attempts: {attempts}")
root = tk.Tk()
root.title("Guess the number")
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Check", command=check).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
root.mainloop()
