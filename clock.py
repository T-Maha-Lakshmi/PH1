import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Simple Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), bg='white', fg='black')
label.pack(pady=20)

update_time()

root.mainloop()
