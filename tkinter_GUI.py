import tkinter as tk
def on_button_click():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

root = tk.Tk()
root.title("Simple GUI")
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="submit", command=on_button_click)
button.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()
