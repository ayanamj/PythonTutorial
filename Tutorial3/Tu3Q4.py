import tkinter as tk
def fc():
    far = float(f.get())
    cel = (far - 32) * 5/9
    c.delete(0, tk.END)
    c.insert(0, f"{cel:.2f}")
def cf():
    cel = float(c.get())
    far = (cel * 9/5) + 32
    f.delete(0, tk.END)
    f.insert(0, f"{far:.2f}")
root = tk.Tk()
root.title("Temperature Converter")
tk.Label(root, text="Fahrenheit").grid(row=0, column=0)
tk.Label(root, text="Celsius").grid(row=0, column=1)
f = tk.Entry(root)
f.grid(row=1, column=0)
f.insert(0, "32")
c = tk.Entry(root)
c.grid(row=1, column=1)
c.insert(0, "0.0")
tk.Button(root, text="-->", command=fc).grid(row=2, column=0)
tk.Button(root, text="<--", command=cf).grid(row=2, column=1)
root.mainloop()
