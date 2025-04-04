import tkinter as tk
def main():
    h = float(height.get())
    b = float(bounce.get())
    n = int(count.get())
    dist = h
    for _ in range(n):
        h *= b
        dist += 2 * h
    result.set(f"Total Distance: {dist:.2f}")
root = tk.Tk()
root.title("Bouncy Ball Distance")
tk.Label(root, text="Height").pack()
height = tk.Entry(root)
height.pack()
tk.Label(root, text="Bounciness Index").pack()
bounce = tk.Entry(root)
bounce.pack()
tk.Label(root, text="Bounces").pack()
count = tk.Entry(root)
count.pack()
tk.Button(root, text="Calculate", command=main).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
root.mainloop()
