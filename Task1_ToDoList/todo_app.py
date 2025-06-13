import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        del tasks[selected[0]]
        save_tasks(tasks)
        update_list()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def mark_done():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]]["done"] = not tasks[selected[0]]["done"]
        save_tasks(tasks)
        update_list()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def update_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔️ " if t["done"] else "❌ "
        listbox.insert(tk.END, status + t["task"])

# Main GUI
root = tk.Tk()
root.title("To-Do List App")

# Entry
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack(pady=2)
tk.Button(root, text="Delete Task", command=delete_task).pack(pady=2)
tk.Button(root, text="Mark Done/Undone", command=mark_done).pack(pady=2)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Load tasks on start
tasks = load_tasks()
update_list()

root.mainloop()
