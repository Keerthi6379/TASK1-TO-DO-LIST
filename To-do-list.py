import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y, END, LEFT, BOTH

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def mark_done():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        if not task.endswith("✔"):
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, f"{task} ✔")
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done.")

# ---------------- Modern UI ----------------
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x450")
root.config(bg="#2E3440")  # dark background

# Title Label
tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"),
         fg="white", bg="#2E3440").pack(pady=10)

# Frame for entry + add button
entry_frame = tk.Frame(root, bg="#2E3440")
entry_frame.pack(pady=5)

task_entry = tk.Entry(entry_frame, width=25, font=("Arial", 12))
task_entry.pack(side=LEFT, padx=5, ipady=5)
task_entry.bind("<Return>", add_task)

add_button = tk.Button(entry_frame, text="➕ Add", command=add_task,
                       font=("Arial", 10, "bold"), bg="#88C0D0", fg="black", width=8)
add_button.pack(side=LEFT)

# Frame for listbox + scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=BOTH, expand=True)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

tasks_listbox = tk.Listbox(list_frame, width=40, height=12,
                           font=("Arial", 12), bg="#ECEFF4",
                           selectbackground="#88C0D0", activestyle="dotbox")
tasks_listbox.pack(side=LEFT, fill=BOTH, expand=True)
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Buttons
btn_frame = tk.Frame(root, bg="#2E3440")
btn_frame.pack(pady=15)

mark_done_button = tk.Button(btn_frame, text="✔ Mark Done", command=mark_done,
                             font=("Arial", 10, "bold"), bg="#A3BE8C", width=12)
mark_done_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(btn_frame, text="🗑 Delete", command=delete_task,
                          font=("Arial", 10, "bold"), bg="#BF616A", width=12)
delete_button.grid(row=0, column=1, padx=10)

root.mainloop()
