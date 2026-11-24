
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
import csv

# ==========================================
# CRIMSON AMETHYST NIGHTFALL THEME
# ==========================================

BG = "#160F20"
PANEL = "#251832"
CARD = "#30203F"
PURPLE = "#70418C"
LIGHT_PURPLE = "#B98AD8"
PINK = "#D99ABF"
WHITE = "#F8F0FA"
MUTED = "#C4B2CE"
RED = "#B94D70"
GREEN = "#658F79"

FILE_NAME = "studentMarks.txt"

INITIAL_DATA = [
    ["1345", "John Curry", 8, 15, 7, 45],
    ["2345", "Sam Sturtivant", 14, 15, 14, 77],
    ["9876", "Lee Scott", 17, 11, 16, 99],
    ["3724", "Matt Thompson", 19, 11, 15, 81],
    ["1212", "Ron Herrema", 14, 17, 18, 66],
    ["8439", "Jake Hobbs", 10, 11, 10, 43],
    ["2344", "Jo Hyde", 6, 15, 10, 55],
    ["9384", "Gareth Southgate", 5, 6, 8, 33],
    ["8327", "Alan Shearer", 20, 20, 20, 100],
    ["2983", "Les Ferdinand", 15, 17, 18, 92]
]


# ==========================================
# STUDENT MANAGER CLASS
# ==========================================

class StudentManager:

    def __init__(self, root):

        self.root = root
        self.root.title("Student Manager - Crimson Amethyst Nightfall")

        # Open maximised on Windows
        try:
            self.root.state("zoomed")
        except tk.TclError:
            self.root.geometry("1250x750")

        self.root.minsize(1050, 650)
        self.root.configure(bg=BG)

        self.students = []

        self.load_data()
        self.setup_styles()
        self.create_interface()
        self.view_all()

    # ======================================
    # FILE HANDLING
    # ======================================

    def load_data(self):

        if not os.path.exists(FILE_NAME):
            self.students = [s.copy() for s in INITIAL_DATA]
            self.save_data()
            return

        try:
            with open(FILE_NAME, "r", newline="") as file:

                reader = csv.reader(file)
                rows = list(reader)

            self.students = []

            for row in rows[1:]:

                if len(row) != 6:
                    continue

                student = [
                    row[0],
                    row[1],
                    int(row[2]),
                    int(row[3]),
                    int(row[4]),
                    int(row[5])
                ]

                self.students.append(student)

        except (ValueError, OSError, csv.Error):

            messagebox.showerror(
                "File Error",
                "There was a problem loading studentMarks.txt."
            )

            self.students = [s.copy() for s in INITIAL_DATA]

    def save_data(self):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([len(self.students)])

            writer.writerows(self.students)

    # ======================================
    # MARK CALCULATIONS
    # ======================================

    def coursework(self, student):

        return student[2] + student[3] + student[4]

    def total(self, student):

        return self.coursework(student) + student[5]

    def percentage(self, student):

        return (self.total(student) / 160) * 100

    def grade(self, student):

        mark = self.percentage(student)

        if mark >= 70:
            return "A"
        elif mark >= 60:
            return "B"
        elif mark >= 50:
            return "C"
        elif mark >= 40:
            return "D"
        else:
            return "F"

    # ======================================
    # TABLE STYLES
    # ======================================

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=PANEL,
            foreground=WHITE,
            fieldbackground=PANEL,
            rowheight=32,
            font=("Segoe UI", 9)
        )

        style.configure(
            "Treeview.Heading",
            background=PURPLE,
            foreground=WHITE,
            font=("Segoe UI", 9, "bold"),
            padding=7
        )

        style.map(
            "Treeview",
            background=[("selected", PURPLE)],
            foreground=[("selected", WHITE)]
        )

        style.configure(
            "Vertical.TScrollbar",
            background=PURPLE,
            troughcolor=BG,
            arrowcolor=WHITE
        )

    # ======================================
    # MAIN INTERFACE
    # ======================================

    def create_interface(self):

        # HEADER
        header = tk.Frame(self.root, bg=BG)
        header.pack(fill="x", padx=20, pady=(12, 7))

        tk.Label(
            header,
            text="STUDENT MANAGER",
            font=("Segoe UI", 23, "bold"),
            bg=BG,
            fg=LIGHT_PURPLE
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Manage student records, marks and academic performance",
            font=("Segoe UI", 10),
            bg=BG,
            fg=MUTED
        ).pack(anchor="w", pady=2)

        # MAIN CONTENT
        main = tk.Frame(self.root, bg=BG)
        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 10)
        )

        # ==================================
        # LEFT MENU
        # ==================================

        menu = tk.Frame(
            main,
            bg=PANEL,
            width=245,
            padx=12,
            pady=12
        )

        menu.pack(side="left", fill="y", padx=(0, 14))
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="MAIN MENU",
            font=("Segoe UI", 13, "bold"),
            bg=PANEL,
            fg=PINK
        ).pack(pady=(0, 7))

        # All eight main buttons

        self.create_menu_button(
            menu, "1. View All Students",
            self.view_all, PURPLE
        )

        self.create_menu_button(
            menu, "2. View Individual",
            self.view_individual, CARD
        )

        self.create_menu_button(
            menu, "3. Highest Overall Mark",
            self.highest_student, CARD
        )

        self.create_menu_button(
            menu, "4. Lowest Overall Mark",
            self.lowest_student, CARD
        )

        self.create_menu_button(
            menu, "5. Sort Student Records",
            self.sort_students, CARD
        )

        # DIVIDER
        tk.Frame(
            menu,
            bg="#55405F",
            height=2
        ).pack(fill="x", pady=7)

        tk.Label(
            menu,
            text="RECORD MANAGEMENT",
            font=("Segoe UI", 9, "bold"),
            bg=PANEL,
            fg=PINK
        ).pack(pady=(0, 5))

        self.create_menu_button(
            menu, "6. Add Student",
            self.add_student, GREEN
        )

        self.create_menu_button(
            menu, "7. Delete Student",
            self.delete_student, RED
        )

        self.create_menu_button(
            menu, "8. Update Student",
            self.update_student, PURPLE
        )

        self.create_menu_button(
            menu, "Clear Display",
            self.clear_display, CARD
        )

        # ==================================
        # RIGHT SIDE
        # ==================================

        right = tk.Frame(main, bg=BG)
        right.pack(side="left", fill="both", expand=True)

        # SUMMARY CARDS
        cards = tk.Frame(right, bg=BG)
        cards.pack(fill="x", pady=(0, 10))

        self.student_count = tk.Label(
            cards,
            text="Students: 0",
            bg=CARD,
            fg=WHITE,
            font=("Segoe UI", 11, "bold"),
            padx=10,
            pady=11
        )

        self.student_count.pack(
            side="left",
            fill="x",
            expand=True,
            padx=3
        )

        self.average_label = tk.Label(
            cards,
            text="Class Average: 0%",
            bg=CARD,
            fg=WHITE,
            font=("Segoe UI", 11, "bold"),
            padx=10,
            pady=11
        )

        self.average_label.pack(
            side="left",
            fill="x",
            expand=True,
            padx=3
        )

        # TABLE TITLE
        tk.Label(
            right,
            text="STUDENT RECORDS",
            font=("Segoe UI", 14, "bold"),
            bg=BG,
            fg=LIGHT_PURPLE
        ).pack(anchor="w", pady=(3, 8))

        # TABLE
        table_frame = tk.Frame(right, bg=PANEL)
        table_frame.pack(fill="both", expand=True)

        columns = (
            "code",
            "name",
            "coursework",
            "exam",
            "total",
            "percentage",
            "grade"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headings = {
            "code": "Student No.",
            "name": "Student Name",
            "coursework": "Coursework /60",
            "exam": "Exam /100",
            "total": "Total /160",
            "percentage": "Percentage",
            "grade": "Grade"
        }

        widths = {
            "code": 85,
            "name": 150,
            "coursework": 105,
            "exam": 85,
            "total": 90,
            "percentage": 95,
            "grade": 65
        }

        for col in columns:

            self.tree.heading(
                col,
                text=headings[col]
            )

            self.tree.column(
                col,
                width=widths[col],
                minwidth=55,
                anchor="center"
            )

        self.tree.column("name", anchor="w")

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<Double-1>",
            lambda event: self.update_student()
        )

        # OUTPUT BOX
        self.output = tk.Text(
            right,
            height=6,
            bg=PANEL,
            fg=WHITE,
            font=("Consolas", 9),
            relief="flat",
            padx=10,
            pady=8,
            wrap="word"
        )

        self.output.pack(
            fill="x",
            pady=(10, 0)
        )

        self.output.insert(
            "end",
            "Welcome to Student Manager!\n"
            "Choose an option from the menu."
        )

        self.output.config(state="disabled")

        # ==================================
        # BOTTOM STATUS
        # ==================================

        self.status = tk.Label(
            self.root,
            text="Ready | Crimson Amethyst Nightfall",
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 9),
            anchor="w",
            padx=15,
            pady=6
        )

        self.status.pack(fill="x", side="bottom")

    # ======================================
    # MENU BUTTON FUNCTION
    # ======================================

    def create_menu_button(self, parent, text, command, color):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg=WHITE,
            activebackground=LIGHT_PURPLE,
            activeforeground=BG,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=4,
            pady=6
        )

        button.pack(
            fill="x",
            pady=2
        )

    # ======================================
    # DISPLAY STUDENT RECORDS
    # ======================================

    def display_students(self, records):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for student in records:

            values = (
                student[0],
                student[1],
                self.coursework(student),
                student[5],
                self.total(student),
                f"{self.percentage(student):.2f}%",
                self.grade(student)
            )

            self.tree.insert(
                "",
                "end",
                values=values
            )

        self.student_count.config(
            text=f"Students: {len(self.students)}"
        )

        if self.students:

            average = sum(
                self.percentage(s) for s in self.students
            ) / len(self.students)

        else:
            average = 0

        self.average_label.config(
            text=f"Class Average: {average:.2f}%"
        )

    # ======================================
    # OUTPUT AND STATUS FUNCTIONS
    # ======================================

    def show_message(self, message):

        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("end", message)
        self.output.config(state="disabled")

    def update_status(self, message):

        self.status.config(text=message)

    def student_details(self, student):

        return (
            f"Student Name:       {student[1]}\n"
            f"Student Number:     {student[0]}\n"
            f"Coursework Total:   {self.coursework(student)}/60\n"
            f"Examination Mark:   {student[5]}/100\n"
            f"Overall Total:      {self.total(student)}/160\n"
            f"Overall Percentage: {self.percentage(student):.2f}%\n"
            f"Student Grade:      {self.grade(student)}"
        )

    # ======================================
    # 1. VIEW ALL STUDENTS
    # ======================================

    def view_all(self):

        self.display_students(self.students)

        if not self.students:

            self.show_message("No student records available.")
            return

        average = sum(
            self.percentage(s) for s in self.students
        ) / len(self.students)

        message = (
            "ALL STUDENT RECORDS\n"
            "--------------------------------\n"
            f"Number of students: {len(self.students)}\n"
            f"Class average: {average:.2f}%\n"
            "All student records are displayed in the table."
        )

        self.show_message(message)
        self.update_status("Showing all student records")

    # ======================================
    # 2. VIEW INDIVIDUAL STUDENT
    # ======================================

    def view_individual(self):

        search = simpledialog.askstring(
            "Find Student",
            "Enter student name or student number:",
            parent=self.root
        )

        if not search:
            return

        search = search.strip().lower()

        matches = [
            s for s in self.students
            if search == s[0].lower()
            or search in s[1].lower()
        ]

        if not matches:

            messagebox.showwarning(
                "Not Found",
                "No student found with that name or number."
            )
            return

        self.display_students(matches)

        details = "\n\n".join(
            self.student_details(s) for s in matches
        )

        self.show_message(
            "INDIVIDUAL STUDENT RECORD\n\n" + details
        )

        self.update_status("Showing individual student record")

    # ======================================
    # 3. HIGHEST OVERALL MARK
    # ======================================

    def highest_student(self):

        if not self.students:

            messagebox.showinfo(
                "No Records",
                "No students available."
            )
            return

        student = max(
            self.students,
            key=self.total
        )

        self.display_students([student])

        self.show_message(
            "STUDENT WITH HIGHEST OVERALL MARK\n\n"
            + self.student_details(student)
        )

        self.update_status("Highest overall student displayed")

    # ======================================
    # 4. LOWEST OVERALL MARK
    # ======================================

    def lowest_student(self):

        if not self.students:

            messagebox.showinfo(
                "No Records",
                "No students available."
            )
            return

        student = min(
            self.students,
            key=self.total
        )

        self.display_students([student])

        self.show_message(
            "STUDENT WITH LOWEST OVERALL MARK\n\n"
            + self.student_details(student)
        )

        self.update_status("Lowest overall student displayed")

    # ======================================
    # 5. SORT STUDENT RECORDS
    # ======================================

    def sort_students(self):

        if not self.students:

            messagebox.showinfo(
                "No Records",
                "No students available."
            )
            return

        descending = messagebox.askyesno(
            "Sort Records",
            "Choose sorting order:\n\n"
            "YES = Highest to Lowest\n"
            "NO = Lowest to Highest"
        )

        sorted_students = sorted(
            self.students,
            key=self.total,
            reverse=descending
        )

        self.display_students(sorted_students)

        order = (
            "Descending" if descending
            else "Ascending"
        )

        self.show_message(
            "STUDENT RECORDS SORTED\n\n"
            f"Sorting order: {order}\n"
            "Students sorted by overall marks."
        )

        self.update_status(
            f"Records sorted in {order} order"
        )

    # ======================================
    # STUDENT FORM
    # ======================================

    def student_form(self, title, old_student=None):

        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("430x510")
        window.configure(bg=PANEL)
        window.resizable(False, False)
        window.transient(self.root)
        window.grab_set()

        tk.Label(
            window,
            text=title.upper(),
            font=("Segoe UI", 18, "bold"),
            bg=PANEL,
            fg=LIGHT_PURPLE
        ).pack(pady=(15, 10))

        fields = [
            ("Student Number", 0),
            ("Student Name", 1),
            ("Coursework 1 /20", 2),
            ("Coursework 2 /20", 3),
            ("Coursework 3 /20", 4),
            ("Examination /100", 5)
        ]

        entries = []

        for label, index in fields:

            tk.Label(
                window,
                text=label,
                bg=PANEL,
                fg=WHITE,
                font=("Segoe UI", 10, "bold")
            ).pack(
                anchor="w",
                padx=35,
                pady=(4, 2)
            )

            entry = tk.Entry(
                window,
                bg=BG,
                fg=WHITE,
                insertbackground=WHITE,
                relief="flat",
                font=("Segoe UI", 10)
            )

            entry.pack(
                fill="x",
                padx=35,
                ipady=6
            )

            if old_student:
                entry.insert(
                    0,
                    str(old_student[index])
                )

            entries.append(entry)

        def submit():

            try:

                code = entries[0].get().strip()
                name = entries[1].get().strip()

                if (
                    not code.isdigit()
                    or not 1000 <= int(code) <= 9999
                ):
                    raise ValueError(
                        "Student number must be between 1000 and 9999."
                    )

                if not name or "," in name:
                    raise ValueError(
                        "Please enter a valid student name."
                    )

                marks = []
                limits = [20, 20, 20, 100]

                for i in range(2, 6):

                    value = entries[i].get().strip()

                    if not value.isdigit():
                        raise ValueError(
                            "Marks must be whole numbers."
                        )

                    mark = int(value)

                    if not 0 <= mark <= limits[i - 2]:
                        raise ValueError(
                            f"Marks must be between 0 and {limits[i - 2]}."
                        )

                    marks.append(mark)

                for s in self.students:

                    if s[0] == code:

                        if old_student is None or s != old_student:

                            raise ValueError(
                                "This student number already exists."
                            )

                new_student = [
                    code,
                    name,
                    marks[0],
                    marks[1],
                    marks[2],
                    marks[3]
                ]

                if old_student is None:

                    self.students.append(new_student)
                    action = "added"

                else:

                    index = self.students.index(old_student)
                    self.students[index] = new_student
                    action = "updated"

                self.save_data()
                self.view_all()

                self.show_message(
                    f"STUDENT SUCCESSFULLY {action.upper()}\n\n"
                    + self.student_details(new_student)
                )

                self.update_status(
                    f"Student {action} successfully"
                )

                window.destroy()

                messagebox.showinfo(
                    "Success",
                    f"Student record {action} successfully!"
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Information",
                    str(error)
                )

        tk.Button(
            window,
            text="SAVE STUDENT",
            command=submit,
            bg=PURPLE,
            fg=WHITE,
            activebackground=LIGHT_PURPLE,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            pady=9
        ).pack(
            fill="x",
            padx=35,
            pady=(15, 6)
        )

        tk.Button(
            window,
            text="CANCEL",
            command=window.destroy,
            bg=RED,
            fg=WHITE,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            pady=8
        ).pack(
            fill="x",
            padx=35
        )

        entries[0].focus_set()

    # ======================================
    # 6. ADD STUDENT
    # ======================================

    def add_student(self):

        self.student_form("Add New Student")

    # ======================================
    # GET SELECTED STUDENT
    # ======================================

    def get_selected_student(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Select Student",
                "Please select a student from the table first."
            )
            return None

        code = self.tree.item(
            selected[0],
            "values"
        )[0]

        for student in self.students:

            if student[0] == code:
                return student

        return None

    # ======================================
    # 7. DELETE STUDENT
    # ======================================

    def delete_student(self):

        student = self.get_selected_student()

        if student is None:
            return

        confirm = messagebox.askyesno(
            "Delete Student",
            f"Are you sure you want to delete:\n\n"
            f"{student[1]} ({student[0]})?"
        )

        if confirm:

            self.students.remove(student)

            self.save_data()
            self.view_all()

            self.show_message(
                f"Student {student[1]} has been deleted successfully."
            )

            self.update_status("Student record deleted")

            messagebox.showinfo(
                "Deleted",
                "Student record deleted successfully!"
            )

    # ======================================
    # 8. UPDATE STUDENT
    # ======================================

    def update_student(self):

        student = self.get_selected_student()

        if student is None:
            return

        self.student_form(
            "Update Student Record",
            student
        )

    # ======================================
    # CLEAR DISPLAY
    # ======================================

    def clear_display(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        self.show_message(
            "Display cleared.\n"
            "Your student records are still safely saved."
        )

        self.update_status("Display cleared")


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    app = StudentManager(root)

    root.mainloop()
