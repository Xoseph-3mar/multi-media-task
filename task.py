import tkinter as tk

def change_text():
    lbl.config(text="✅ Button Clicked!", fg="#00ff99")

root = tk.Tk()
root.geometry("420x500")
root.title("Home")
root.resizable(False, False)
root.configure(bg="#121212")

title = tk.Label(
    root,
    text="Welcome",
    font=("Arial", 22, "bold"),
    bg="#121212",
    fg="white"
)
title.pack(pady=30)

lbl = tk.Label(
    root,
    text="Hello",
    width=18,
    height=2,
    bg="#2a2a2a",
    fg="white",
    font=("Arial", 16, "bold"),
    relief="ridge",
    bd=2
)
lbl.pack(pady=20)

btn = tk.Button(
    root,
    text="Click Me",
    width=14,
    height=2,
    bg="#007acc",
    fg="white",
    font=("Arial", 14, "bold"),
    activebackground="#005f99",
    activeforeground="white",
    cursor="hand2",
    command=change_text
)
btn.pack(pady=20)

root.mainloop()
