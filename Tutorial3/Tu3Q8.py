import tkinter as tk
l, h = 1, 100
guess = (l + h) // 2
def small():
    global l, guess
    l = guess + 1
    update()
def large():
    global h, guess
    h = guess - 1
    update()
def correct():
    result.set(f"Computer guessed it: {guess}")
def update():
    global guess
    guess = (l + h) // 2
    result.set(f"Is it {guess}?")
root = tk.Tk()
root.title("Computer Guesses Number")
result = tk.StringVar()
result.set(f"Is it {guess}?")
tk.Label(root, textvariable=result).pack()
tk.Button(root, text="Too Small, try again", command=small).pack()
tk.Button(root, text="Too Large, try again", command=large).pack()
tk.Button(root, text="Correct", command=correct).pack()
root.mainloop()
