import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AffiliateData:
    def __init__(self, id_type, id_number, full_name, current_income, employment_type, desired_service, affiliation_tariff, affiliation_date):
        self.id_type = id_type
        self.id_number = id_number
        self.full_name = full_name
        self.current_income = current_income
        self.employment_type = employment_type
        self.desired_service = desired_service
        self.affiliation_tariff = affiliation_tariff
        self.affiliation_date = affiliation_date

class CompensationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login — Compensándote")
        self.root.geometry("600x670")
        self.root.config(bg="#0b1d2a")
        self.root.resizable(False, False)

        # Data structures collections in main memory
        self.stack_collection = []
        self.queue_collection = []
        self.list_collection = []

        self.create_login_widgets()

    def create_login_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        about_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Info", command=self.show_about_dialog)

        # Title
        title_label = tk.Label(self.root, text="Compensándote", font=("Arial", 24, "bold"), fg="#00b4d8", bg="#0b1d2a")
        title_label.pack(pady=20)

        subtitle_label = tk.Label(self.root, text="Family Compensation Fund — Affiliation Control", font=("Arial", 11), fg="#adb5bd", bg="#0b1d2a")
        subtitle_label.pack(pady=5)

        # Card frame
        card_frame = tk.Frame(self.root, bg="#1b263b", bd=2, relief="groove")
        card_frame.pack(pady=15, padx=40, fill="both", expand=True)

        current_date_str = datetime.now().strftime("%B %d, %Y")
        info_text = (
            "Application:      Fase3\n"
            "Student:          Cristian Stiven Cuero Caicedo\n"
            "Group:            301305_155\n"
            "Course:           Data Structures · 301305\n"
            f"Date:             {current_date_str}"
        )
        info_label = tk.Label(card_frame, text=info_text, font=("Consolas", 10), fg="#e0fbfc", bg="#1b263b", justify="left")
        info_label.pack(pady=15, padx=20)

        # Password Section
        pwd_label = tk.Label(self.root, text="Password", font=("Arial", 11, "bold"), fg="#ffffff", bg="#0b1d2a")
        pwd_label.pack(anchor="w", padx=50)

        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 14), bg="#0d1b2a", fg="#ffffff", insertbackground="white")
        self.password_entry.pack(fill="x", padx=50, pady=5, ipady=5)

        pwd_hint = tk.Label(self.root, text="Password masked ( * * * ) [Hint: Caja]", font=("Arial", 9), fg="#8d99ae", bg="#0b1d2a")
        pwd_hint.pack(anchor="w", padx=50, pady=2)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#0b1d2a")
        btn_frame.pack(pady=25, fill="x", padx=50)

        login_btn = tk.Button(btn_frame, text="Login →", font=("Arial", 11, "bold"), bg="#00b4d8", fg="#ffffff", bd=0, cursor="hand2", command=self.validate_login)
        login_btn.pack(side="left", fill="x", expand=True, ipadx=10, ipady=8, padx=(0, 10))

        exit_btn = tk.Button(btn_frame, text="Exit", font=("Arial", 11, "bold"), bg="#e63946", fg="#ffffff", bd=0, cursor="hand2", command=self.root.quit)
        exit_btn.pack(side="right", fill="x", expand=True, ipadx=10, ipady=8, padx=(10, 0))

        footer_label = tk.Label(self.root, text="UNAD · ECBTI · Systems Engineering", font=("Arial", 8), fg="#6c757d", bg="#0b1d2a")
        footer_label.pack(side="bottom", pady=10)

    def show_about_dialog(self):
        current_date_str = datetime.now().strftime("%B %d, %Y")
        messagebox.showinfo(
            "About",
            "ℹ  Course: Data Structures — 301305\n\n"
            "👤 Student: Cristian Stiven Cuero Caicedo\n\n"
            "👥 Collaborative Group: 301305_155\n\n"
            "🏛️ UNAD · ECBTI · Systems Engineering\n\n"
            f"📅 Date: {current_date_str}"
        )

    def validate_login(self):
        entered_password = self.password_entry.get()
        if entered_password == "Caja":
            self.open_main_application()
        else:
            messagebox.showerror("Access Denied", "Incorrect password. Please try again (Hint: Caja).")

    def open_main_application(self):
        self.root.destroy()
        self.main_window = tk.Tk()
        self.main_window.title("Caja Compensándote – Affiliation Control")
        self.main_window.geometry("1180x700")
        self.main_window.config(bg="#0b1d2a")

        # Top Bar
        top_bar = tk.Frame(self.main_window, bg="#1b263b", height=50)
        top_bar.pack(fill="x", side="top")
        
        app_title = tk.Label(top_bar, text="🏢 Compensándote — Affiliation Control", font=("Arial", 14, "bold"), fg="#00b4d8", bg="#1b263b")
        app_title.pack(side="left", padx=15, pady=10)

        user_info = tk.Label(top_bar, text="Cristian Stiven Cuero Caicedo (Group: 301305_155)", font=("Arial", 9), fg="#adb5bd", bg="#1b263b")
        user_info.pack(side="right", padx=15, pady=10)

        # Content Layout
        content_frame = tk.Frame(self.main_window, bg="#0b1d2a")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # LEFT FRAME: Form
        form_frame = tk.LabelFrame(content_frame, text=" 📋 Identification & Data ", font=("Arial", 10, "bold"), fg="#00b4d8", bg="#0b1d2a", bd=2, relief="groove")
        form_frame.pack(side="left", fill="y", padx=5, pady=5, ipadx=10)

        # Data Structure Selector
        tk.Label(form_frame, text="Data Structure:", font=("Arial", 9, "bold"), fg="#ffffff", bg="#0b1d2a").grid(row=0, column=0, sticky="w", pady=2)
        self.structure_var = tk.StringVar(value="Stack")
        self.structure_combo = ttk.Combobox(form_frame, textvariable=self.structure_var, values=["Stack", "Queue", "List"], state="readonly", width=24)
        self.structure_combo.grid(row=1, column=0, sticky="w", pady=2)
        self.structure_combo.bind("<<ComboboxSelected>>", self.on_structure_changed)

        # ID Type
        tk.Label(form_frame, text="ID Type:", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=2, column=0, sticky="w", pady=2)
        self.id_type_var = tk.StringVar(value="CC")
        self.id_type_combo = ttk.Combobox(form_frame, textvariable=self.id_type_var, values=["CC", "CE", "NUIP", "PAS"], state="readonly", width=24)
        self.id_type_combo.grid(row=3, column=0, sticky="w", pady=2)

        # ID Number
        tk.Label(form_frame, text="ID Number (digits only):", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=4, column=0, sticky="w", pady=2)
        self.id_number_entry = tk.Entry(form_frame, width=27, font=("Arial", 10))
        self.id_number_entry.grid(row=5, column=0, sticky="w", pady=2)
        self.id_number_entry.config(validate="key", validatecommand=(self.main_window.register(self.validate_digits), '%P'))

        # Full Name
        tk.Label(form_frame, text="Full Name (letters only):", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=6, column=0, sticky="w", pady=2)
        self.full_name_entry = tk.Entry(form_frame, width=27, font=("Arial", 10))
        self.full_name_entry.grid(row=7, column=0, sticky="w", pady=2)
        self.full_name_entry.config(validate="key", validatecommand=(self.main_window.register(self.validate_letters), '%P'))

        # Economic Data Frame
        eco_frame = tk.LabelFrame(form_frame, text=" 💰 Economic & Service Data ", font=("Arial", 9, "bold"), fg="#00b4d8", bg="#0b1d2a", bd=1, relief="groove")
        eco_frame.grid(row=8, column=0, sticky="we", pady=8)

        tk.Label(eco_frame, text="Current Income ($):", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=0, column=0, sticky="w", pady=2)
        self.income_entry = tk.Entry(eco_frame, width=25, font=("Arial", 10))
        self.income_entry.grid(row=1, column=0, sticky="w", pady=2)
        self.income_entry.config(validate="key", validatecommand=(self.main_window.register(self.validate_digits), '%P'))

        tk.Label(eco_frame, text="Employment Type:", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=2, column=0, sticky="w", pady=2)
        self.employment_var = tk.StringVar(value="Employee")
        emp_frame = tk.Frame(eco_frame, bg="#0b1d2a")
        emp_frame.grid(row=3, column=0, sticky="w", pady=2)
        tk.Radiobutton(emp_frame, text="Employee", variable=self.employment_var, value="Employee", bg="#0b1d2a", fg="#ffffff", selectcolor="#1b263b", command=self.calculate_tariff).pack(side="left", padx=5)
        tk.Radiobutton(emp_frame, text="Independent", variable=self.employment_var, value="Independent", bg="#0b1d2a", fg="#ffffff", selectcolor="#1b263b", command=self.calculate_tariff).pack(side="left", padx=5)

        tk.Label(form_frame, text="Desired Service:", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=9, column=0, sticky="w", pady=2)
        self.service_var = tk.StringVar(value="Unemployment Subsidy")
        self.service_combo = ttk.Combobox(form_frame, textvariable=self.service_var, values=["Unemployment Subsidy", "Park Entry", "Training Course", "Travel Package", "Preventive Medicine"], state="readonly", width=24)
        self.service_combo.grid(row=10, column=0, sticky="w", pady=2)
        self.service_combo.bind("<<ComboboxSelected>>", lambda e: self.calculate_tariff())

        self.income_entry.bind("<KeyRelease>", lambda e: self.calculate_tariff())

        tk.Label(form_frame, text="Affiliation Tariff ($) — read only:", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=11, column=0, sticky="w", pady=2)
        self.tariff_entry = tk.Entry(form_frame, width=27, font=("Arial", 10, "bold"), state="readonly", bg="#e9ecef")
        self.tariff_entry.grid(row=12, column=0, sticky="w", pady=2)

        # Date Entry (Spinbox dd/mm/yyyy)
        tk.Label(form_frame, text="Affiliation Date (dd/mm/yyyy):", font=("Arial", 9), fg="#ffffff", bg="#0b1d2a").grid(row=13, column=0, sticky="w", pady=2)
        date_spin_frame = tk.Frame(form_frame, bg="#0b1d2a")
        date_spin_frame.grid(row=14, column=0, sticky="w", pady=2)

        self.day_spin = tk.Spinbox(date_spin_frame, from_=1, to=31, width=3, font=("Arial", 9))
        self.day_spin.pack(side="left", padx=2)
        self.month_spin = tk.Spinbox(date_spin_frame, from_=1, to=12, width=3, font=("Arial", 9))
        self.month_spin.pack(side="left", padx=2)
        self.year_spin = tk.Spinbox(date_spin_frame, from_=2024, to=2030, width=5, font=("Arial", 9))
        self.year_spin.pack(side="left", padx=2)
        
        now = datetime.now()
        self.day_spin.delete(0, "end"); self.day_spin.insert(0, str(now.day))
        self.month_spin.delete(0, "end"); self.month_spin.insert(0, str(now.month))
        self.year_spin.delete(0, "end"); self.year_spin.insert(0, str(now.year))

        # RIGHT FRAME: Treeview & Action Buttons
        right_frame = tk.Frame(content_frame, bg="#0b1d2a")
        right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.tree_frame = tk.LabelFrame(right_frame, text=" 📊 Registered Affiliates (Stack View Active) ", font=("Arial", 10, "bold"), fg="#00b4d8", bg="#0b1d2a", bd=2, relief="groove")
        self.tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

        columns = ("ID Type", "ID Number", "Full Name", "Income ($)", "Service", "Employment", "Tariff ($)", "Date")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", height=16)
        
        col_widths = [65, 95, 160, 95, 140, 95, 85, 85]
        for col, width in zip(columns, col_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor="center")

        tree_scroll = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        self.tree.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        tree_scroll.pack(side="right", fill="y", pady=5)

        # Action Buttons
        action_btn_frame = tk.Frame(right_frame, bg="#0b1d2a")
        action_btn_frame.pack(fill="x", pady=10, padx=5)

        btn_configs = [
            ("Register", "#00b4d8", self.register_affiliate),
            ("Delete", "#e63946", self.delete_affiliate),
            ("Report", "#2a9d8f", self.show_report),
            ("Clear", "#f4a261", self.clear_form),
            ("Exit", "#6c757d", self.main_window.quit)
        ]

        for text, color, cmd in btn_configs:
            b = tk.Button(action_btn_frame, text=text, font=("Arial", 10, "bold"), bg=color, fg="#ffffff", bd=0, cursor="hand2", command=cmd)
            b.pack(side="left", fill="x", expand=True, padx=4, ipady=8)

        self.main_window.mainloop()

    def validate_digits(self, text):
        return text.isdigit() or text == ""

    def validate_letters(self, text):
        return all(c.isalpha() or c.isspace() for c in text) or text == ""

    def calculate_tariff(self):
        try:
            income_str = self.income_entry.get().strip()
            if not income_str:
                self.set_tariff_text("")
                return 0.0
            
            income = float(income_str)
            emp_type = self.employment_var.get()
            service = self.service_var.get()

            base_tariff = 0.0
            if emp_type == "Employee":
                if 1000000 <= income <= 2000000: base_tariff = 45000
                elif income <= 3000000: base_tariff = 60000
                elif income <= 4000000: base_tariff = 75000
                elif income <= 5000000: base_tariff = 90000
                elif income > 5000000: base_tariff = 150000
                else: base_tariff = 45000
            else: # Independent
                if 1000000 <= income <= 2000000: base_tariff = 10000
                elif income <= 3000000: base_tariff = 20000
                elif income <= 4000000: base_tariff = 30000
                elif income <= 5000000: base_tariff = 40000
                elif income > 5000000: base_tariff = 80000
                else: base_tariff = 10000

            # Service additions
            if service == "Park Entry":
                base_tariff += 2500
            elif service == "Training Course":
                base_tariff += 7500
            elif service == "Travel Package":
                base_tariff += 10000
            elif service == "Preventive Medicine":
                base_tariff += (income * 0.10)

            self.set_tariff_text(f"{base_tariff:.2f}")
            return base_tariff
        except ValueError:
            self.set_tariff_text("")
            return 0.0

    def set_tariff_text(self, text):
        self.tariff_entry.config(state="normal")
        self.tariff_entry.delete(0, tk.END)
        self.tariff_entry.insert(0, text)
        self.tariff_entry.config(state="readonly")

    def on_structure_changed(self, event):
        structure = self.structure_var.get()
        self.tree_frame.config(text=f" 📊 Registered Affiliates ({structure} View Active) ")
        self.refresh_treeview()

    def register_affiliate(self):
        id_type = self.id_type_var.get()
        id_number = self.id_number_entry.get().strip()
        full_name = self.full_name_entry.get().strip()
        income_str = self.income_entry.get().strip()
        emp_type = self.employment_var.get()
        service = self.service_var.get()
        tariff = self.calculate_tariff()
        date_str = f"{self.day_spin.get()}/{self.month_spin.get()}/{self.year_spin.get()}"
        structure = self.structure_var.get()

        if not id_number or not full_name or not income_str:
            messagebox.showwarning("Validation Error", "Please fill in all required fields.")
            return

        affiliate = AffiliateData(id_type, id_number, full_name, float(income_str), emp_type, service, tariff, date_str)

        if structure == "Stack":
            self.stack_collection.append(affiliate) # LIFO
        elif structure == "Queue":
            self.queue_collection.append(affiliate) # FIFO
        elif structure == "List":
            self.list_collection.append(affiliate)  # Append

        messagebox.showinfo("Success", f"Affiliate successfully registered in {structure}!")
        self.refresh_treeview()
        self.clear_form_fields()

    def delete_affiliate(self):
        structure = self.structure_var.get()

        if structure == "Stack":
            if not self.stack_collection:
                messagebox.showwarning("Empty", "Stack is empty.")
                return
            if messagebox.askyesno("Confirm", "Are you sure you want to pop (remove) the top affiliate from the Stack?"):
                removed = self.stack_collection.pop()
                messagebox.showinfo("Removed", f"Popped affiliate: {removed.full_name}")

        elif structure == "Queue":
            if not self.queue_collection:
                messagebox.showwarning("Empty", "Queue is empty.")
                return
            if messagebox.askyesno("Confirm", "Are you sure you want to dequeue (remove) the first affiliate from the Queue?"):
                removed = self.queue_collection.pop(0)
                messagebox.showinfo("Removed", f"Dequeued affiliate: {removed.full_name}")

        elif structure == "List":
            if not self.list_collection:
                messagebox.showwarning("Empty", "List is empty.")
                return
            target_id = tk.simpledialog.askstring("Delete by ID", "Enter the ID number of the affiliate to delete:")
            if target_id:
                found = False
                for aff in self.list_collection:
                    if aff.id_number == target_id:
                        if messagebox.askyesno("Confirm", f"Affiliate found: {aff.full_name}. Proceed with deletion?"):
                            self.list_collection.remove(aff)
                            found = True
                            messagebox.showinfo("Deleted", "Affiliate successfully deleted from List.")
                        break
                if not found:
                    messagebox.showerror("Not Found", "No affiliate found with that ID number.")

        self.refresh_treeview()

    def show_report(self):
        structure = self.structure_var.get()

        if structure == "Stack":
            total_tariff = sum(aff.affiliation_tariff for aff in self.stack_collection) if self.stack_collection else 0.0
            messagebox.showinfo("Stack Report", f"📊 Sum of affiliation tariffs in Stack:\n\n$ {total_tariff:,.2f}")

        elif structure == "Queue":
            count = len(self.queue_collection)
            messagebox.showinfo("Queue Report", f"📊 Total records in Queue:\n\n{count} affiliates")

        elif structure == "List":
            avg_income = (sum(aff.current_income for aff in self.list_collection) / len(self.list_collection)) if self.list_collection else 0.0
            messagebox.showinfo("List Report", f"📊 Average current income in List:\n\n$ {avg_income:,.2f}")

    def refresh_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        structure = self.structure_var.get()
        active_data = []

        if structure == "Stack":
            active_data = list(reversed(self.stack_collection)) # Top first
        elif structure == "Queue":
            active_data = self.queue_collection
        elif structure == "List":
            active_data = self.list_collection

        for aff in active_data:
            self.tree.insert("", "end", values=(aff.id_type, aff.id_number, aff.full_name, f"${aff.current_income:,.2f}", aff.desired_service, aff.employment_type, f"${aff.affiliation_tariff:,.2f}", aff.affiliation_date))

    def clear_form(self):
        self.clear_form_fields()

    def clear_form_fields(self):
        self.id_number_entry.delete(0, tk.END)
        self.full_name_entry.delete(0, tk.END)
        self.income_entry.delete(0, tk.END)
        self.set_tariff_text("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CompensationApp(root)
    root.mainloop()