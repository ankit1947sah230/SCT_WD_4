import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from datetime import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List App')
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=('Task', 'Due', 'Status'), show='headings')
        self.tree.heading('Task', text='Task')
        self.tree.heading('Due', text='Due Date & Time')
        self.tree.heading('Status', text='Status')
        self.tree.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text='Add Task', command=self.add_task).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text='Edit Task', command=self.edit_task).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text='Mark Complete', command=self.mark_complete).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(btn_frame, text='Delete Task', command=self.delete_task).pack(side=tk.LEFT, padx=5, pady=5)

    def add_task(self):
        task = simpledialog.askstring('Add Task', 'Enter task description:')
        if not task:
            return
        due = simpledialog.askstring('Due Date & Time', 'Enter due date and time (YYYY-MM-DD HH:MM):')
        try:
            due_dt = datetime.strptime(due, '%Y-%m-%d %H:%M') if due else ''
            due_str = due_dt.strftime('%Y-%m-%d %H:%M') if due else ''
        except Exception:
            messagebox.showerror('Error', 'Invalid date/time format!')
            return
        self.tasks.append({'task': task, 'due': due_str, 'status': 'Pending'})
        self.refresh()

    def edit_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo('Edit Task', 'Select a task to edit.')
            return
        idx = self.tree.index(selected[0])
        task = self.tasks[idx]
        new_task = simpledialog.askstring('Edit Task', 'Edit task description:', initialvalue=task['task'])
        if not new_task:
            return
        new_due = simpledialog.askstring('Edit Due Date & Time', 'Edit due date and time (YYYY-MM-DD HH:MM):', initialvalue=task['due'])
        try:
            due_dt = datetime.strptime(new_due, '%Y-%m-%d %H:%M') if new_due else ''
            due_str = due_dt.strftime('%Y-%m-%d %H:%M') if new_due else ''
        except Exception:
            messagebox.showerror('Error', 'Invalid date/time format!')
            return
        self.tasks[idx] = {'task': new_task, 'due': due_str, 'status': task['status']}
        self.refresh()

    def mark_complete(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo('Mark Complete', 'Select a task to mark as complete.')
            return
        idx = self.tree.index(selected[0])
        self.tasks[idx]['status'] = 'Completed'
        self.refresh()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo('Delete Task', 'Select a task to delete.')
            return
        idx = self.tree.index(selected[0])
        del self.tasks[idx]
        self.refresh()

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for task in self.tasks:
            self.tree.insert('', tk.END, values=(task['task'], task['due'], task['status']))

if __name__ == '__main__':
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()