import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionnaire de Tâches")
        self.root.geometry("800x600")
        self.root.configure(bg="#e6f0ff")

        self.todo_list = {}
        self.task_id_counter = 1

        title = tk.Label(root, text="📝 Ma To-Do List", font=("Helvetica", 24, "bold"), bg="#e6f0ff", fg="#003366")
        title.pack(pady=15)

        main_frame = tk.Frame(root, bg="#f9fbff")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        task_frame = tk.LabelFrame(main_frame, text="Tâches", font=("Helvetica", 14), bg="#f9fbff", fg="#003366", padx=10, pady=10)
        task_frame.place(relx=0.02, rely=0.05, relwidth=0.6, relheight=0.85)

        self.tasks_canvas = tk.Canvas(task_frame, bg="white", highlightthickness=0)
        self.tasks_canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=self.tasks_canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.tasks_canvas.configure(yscrollcommand=scrollbar.set)
        self.task_list_frame = tk.Frame(self.tasks_canvas, bg="white")
        self.tasks_canvas.create_window((0, 0), window=self.task_list_frame, anchor="nw")
        self.task_list_frame.bind("<Configure>", lambda e: self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all")))

        form_frame = tk.LabelFrame(main_frame, text="Ajouter une tâche", font=("Helvetica", 14), bg="#f9fbff", fg="#003366", padx=10, pady=10)
        form_frame.place(relx=0.65, rely=0.05, relwidth=0.33, relheight=0.85)

        self.task_name_entry = self._make_entry(form_frame, "Nom de la tâche :")
        self.task_desc_entry = self._make_text(form_frame, "Description :", 4)
        self.task_due_date_entry = self._make_entry(form_frame, "Date limite (JJ/MM/AAAA) :")
        self.task_duration_entry = self._make_entry(form_frame, "Durée estimée (ex: 2h, 45min) :")

        self.add_button = tk.Button(form_frame, text="Ajouter", font=("Helvetica", 14, "bold"), bg="#0059b3", fg="white",
                                    activebackground="#004080", command=self.add_task)
        self.add_button.pack(pady=20, ipadx=10, ipady=5)

    def _make_entry(self, parent, label):
        tk.Label(parent, text=label, bg="#f9fbff", font=("Helvetica", 12)).pack(anchor="w", pady=(5, 2))
        entry = tk.Entry(parent, font=("Helvetica", 12))
        entry.pack(fill="x", pady=(0, 10))
        return entry

    def _make_text(self, parent, label, height):
        tk.Label(parent, text=label, bg="#f9fbff", font=("Helvetica", 12)).pack(anchor="w", pady=(5, 2))
        text = tk.Text(parent, height=height, font=("Helvetica", 12))
        text.pack(fill="x", pady=(0, 10))
        return text

    def add_task(self):
        name = self.task_name_entry.get().strip()
        desc = self.task_desc_entry.get("1.0", "end").strip()
        due_date = self.task_due_date_entry.get().strip()
        duration = self.task_duration_entry.get().strip()

        if not name:
            messagebox.showwarning("Attention", "Le nom de la tâche est requis.")
            return

        try:
            parsed_date = datetime.strptime(due_date, "%d/%m/%Y") if due_date else None
        except ValueError:
            messagebox.showerror("Erreur", "Format de date invalide. Utilisez JJ/MM/AAAA.")
            return

        self.todo_list[self.task_id_counter] = {
            "task": name,
            "description": desc,
            "due": due_date,
            "duration": duration,
            "done": False
        }
        self.task_id_counter += 1
        self.clear_entries()
        self.refresh_tasks()

    def clear_entries(self):
        self.task_name_entry.delete(0, 'end')
        self.task_desc_entry.delete("1.0", "end")
        self.task_due_date_entry.delete(0, 'end')
        self.task_duration_entry.delete(0, 'end')

    def refresh_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        if not self.todo_list:
            tk.Label(self.task_list_frame, text="Aucune tâche pour le moment.", font=("Helvetica", 14), fg="#999999",
                     bg="white", justify="center").pack(pady=100)
            return

        for tid, info in sorted(self.todo_list.items()):
            frame = tk.Frame(self.task_list_frame, bg="#f0f5ff", bd=1, relief="solid", padx=10, pady=5)
            frame.pack(fill="x", pady=6, padx=8)

            var = tk.BooleanVar(value=info["done"])
            check = tk.Checkbutton(frame, variable=var, command=lambda tid=tid, var=var: self.toggle_done(tid, var),
                                   bg="#f0f5ff")
            check.grid(row=0, column=0, rowspan=3, padx=(0, 10))

            task_label = tk.Label(frame, text=info["task"], font=("Helvetica", 13, "bold"),
                                  fg="#009933" if info["done"] else "#003366", bg="#f0f5ff")
            task_label.grid(row=0, column=1, sticky="w")

            desc_label = tk.Label(frame, text=info["description"], font=("Helvetica", 11), fg="#555555", bg="#f0f5ff",
                                  wraplength=320, justify="left")
            desc_label.grid(row=1, column=1, sticky="w")

            deadline_color = "red" if self._is_overdue(info["due"]) and not info["done"] else "#003366"
            deadline_text = f"⏳ Durée : {info['duration']} | 📅 Limite : {info['due']}" if info["due"] else f"⏳ Durée : {info['duration']}"
            extra_label = tk.Label(frame, text=deadline_text, font=("Helvetica", 10), fg=deadline_color, bg="#f0f5ff")
            extra_label.grid(row=2, column=1, sticky="w", pady=(0, 5))

            tk.Button(frame, text="✏️ Modifier", command=lambda tid=tid: self.edit_task(tid),
                      font=("Helvetica", 10), bg="#ffc107", fg="black").grid(row=0, column=2, rowspan=3, padx=5)
            tk.Button(frame, text="🗑️ Supprimer", command=lambda tid=tid: self.delete_task(tid),
                      font=("Helvetica", 10), bg="#dc3545", fg="white").grid(row=0, column=3, rowspan=3, padx=5)

    def _is_overdue(self, due_date_str):
        try:
            due = datetime.strptime(due_date_str, "%d/%m/%Y")
            return datetime.now().date() > due.date()
        except:
            return False

    def toggle_done(self, tid, var):
        self.todo_list[tid]["done"] = var.get()
        self.refresh_tasks()

    def delete_task(self, tid):
        if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer cette tâche ?"):
            del self.todo_list[tid]
            self.refresh_tasks()

    def edit_task(self, tid):
        current = self.todo_list[tid]
        new_task = simpledialog.askstring("Modifier tâche", "Nom de la tâche :", initialvalue=current["task"])
        if not new_task:
            return
        new_desc = simpledialog.askstring("Modifier description", "Description :", initialvalue=current["description"])
        new_due = simpledialog.askstring("Modifier date limite", "Date (JJ/MM/AAAA) :", initialvalue=current["due"])
        new_duration = simpledialog.askstring("Modifier durée", "Durée estimée :", initialvalue=current["duration"])
        self.todo_list[tid].update({"task": new_task, "description": new_desc, "due": new_due, "duration": new_duration})
        self.refresh_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
