import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime

# =====================================================
# 1. COMPLETE DATA STRUCTURE: 7 MODULES & QUIZZES
# =====================================================

modules_data = [
    # ------------------ MODULE 1 ------------------
    {
        "id": 1,
        "title": "Module 1: Python Fundamentals",
        "topics": [
            ("Introduction to Python", """Python is a high-level, interpreted, and general-purpose programming language.
Developed by Guido van Rossum in 1991.

Key Features:
• Simple and readable syntax
• Dynamic typing & Automatic Memory Management
• Large ecosystem of built-in and third-party libraries
• Platform Independent (Windows, Mac, Linux)

Applications:
• Machine Learning & AI
• Web Development (Django, Flask)
• Automation & Scripting"""),
            ("Syntax & Variables", """Syntax refers to the formal rules of writing Python code.

Variables:
Containers used to store data values in memory.

Example:
name = "Bhargavi"
age = 20
print(f"Name: {name}, Age: {age}")

Rules:
• Case-sensitive (age and Age are different)
• Uses Indentation (spaces) for blocks instead of curly braces."""),
            ("Operators & Data Types", """Data Types:
1. int (Integers: 10, -5)
2. float (Decimals: 10.5)
3. str (Text: "Python")
4. bool (True / False)

Arithmetic Operators:
+ (Addition), - (Subtraction), * (Multiplication), / (Division), % (Modulus), ** (Power)"""),
            ("Input & Output", """input(): Reads data from the user (always returns String).
print(): Displays output to the console.

Example:
name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))
print("Student:", name, "| Marks:", marks)"""),
            ("Code Examples", """Example 1: Check Positive or Negative
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
else:
    print("Non-positive")

Example 2: String Formatting
item = "Book"
price = 150
print(f"Item: {item} costs {price} INR")"""),
            ("Practice Questions", """1. Write a Python program to convert Celsius to Fahrenheit.
2. Take user age as input and print whether they are eligible to vote.
3. Calculate the area of a circle taking radius from user input."""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which function is used to display output in Python?", "opts": ["input()", "print()", "scan()", "display()"], "ans": "print()"},
            {"q": "2. Which data type stores decimal numbers?", "opts": ["int", "float", "str", "bool"], "ans": "float"},
            {"q": "3. Which symbol is used for single-line comments?", "opts": ["//", "#", "/*", "**"], "ans": "#"},
            {"q": "4. Which keyword is used to accept user input?", "opts": ["print()", "input()", "scan()", "read()"], "ans": "input()"},
            {"q": "5. Python uses _______ for code blocks instead of braces.", "opts": ["Indentation", "Semicolons", "Parentheses", "Quotes"], "ans": "Indentation"}
        ]
    },
    # ------------------ MODULE 2 ------------------
    {
        "id": 2,
        "title": "Module 2: Control Flow & Functions",
        "topics": [
            ("Conditional Statements", """Control flow statements alter the execution flow of programs.

Conditional Blocks:
• if statement
• elif (else if)
• else block

Example:
score = 85
if score >= 90:
    print("Grade A")
elif score >= 75:
    print("Grade B")
else:
    print("Grade C")"""),
            ("Loops (for & while)", """Loops iterate through code blocks multiple times.

1. for loop: Used for iterating over a sequence (list, range, str).
2. while loop: Executes as long as a condition remains True.

Example:
for i in range(1, 6):
    print("Count:", i)"""),
            ("Functions & Parameters", """Functions are reusable blocks of code executed when called.
Defined using the 'def' keyword.

Example:
def greet_student(name="Student"):
    return f"Welcome {name} to Python Platform!"

message = greet_student("Rajee")
print(message)"""),
            ("Lambda & Recursion", """Lambda Function:
An anonymous, single-line function.
add = lambda a, b: a + b

Recursion:
A function calling itself to solve smaller instances of a problem.
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)"""),
            ("Practice & Mini Program", """Mini Program: Factorial & Prime Checker
def check_prime(num):
    if num < 2: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

print("Is 17 Prime?", check_prime(17))"""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which keyword defines a function in Python?", "opts": ["func", "def", "function", "lambda"], "ans": "def"},
            {"q": "2. Which keyword exits a loop prematurely?", "opts": ["exit", "continue", "break", "pass"], "ans": "break"},
            {"q": "3. What function generates a sequence of numbers?", "opts": ["seq()", "range()", "series()", "list()"], "ans": "range()"},
            {"q": "4. Anonymous inline functions in Python are called?", "opts": ["Virtual", "Lambda", "Inline", "Dynamic"], "ans": "Lambda"},
            {"q": "5. What statement does nothing and acts as a placeholder?", "opts": ["pass", "skip", "null", "blank"], "ans": "pass"}
        ]
    },
    # ------------------ MODULE 3 ------------------
    {
        "id": 3,
        "title": "Module 3: Data Structures",
        "topics": [
            ("Lists & Operations", """Lists: Ordered, mutable sequence of elements enclosed in square brackets [].

Operations:
• append(x): Add element to end
• insert(i, x): Insert element at specific index
• pop(): Remove last element

Example:
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")"""),
            ("Tuples & Sets", """Tuples (): Ordered, IMMUTABLE collections.
Example: coordinates = (10.5, 20.8)

Sets {}: Unordered collections of UNIQUE elements.
Example: unique_ids = {101, 102, 103, 101} # Stores {101, 102, 103}"""),
            ("Dictionaries", """Dictionaries {}: Unordered Key-Value pairs.

Example:
student = {
    "roll_no": "3EI1",
    "name": "N. Bhargavi",
    "branch": "CSE-AI&DS"
}
print(student["name"])"""),
            ("Indexing & Slicing", """Sequence Slicing [start : stop : step]

Example:
text = "PythonPlatform"
print(text[0:6])   # Output: Python
print(text[::-1])  # Reverses string"""),
            ("Student Record Mini App", """# Mini Inventory / Student Record Storage System
records = []
def add_student(sid, sname):
    records.append({"id": sid, "name": sname})

add_student(101, "K. Rajee")
print("Database Records:", records)"""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which data structure is immutable?", "opts": ["List", "Dictionary", "Tuple", "Set"], "ans": "Tuple"},
            {"q": "2. Which collection stores unique elements only?", "opts": ["List", "Set", "Tuple", "Array"], "ans": "Set"},
            {"q": "3. How do you append element 'x' to list 'L'?", "opts": ["L.add(x)", "L.append(x)", "L.insert(x)", "L.push(x)"], "ans": "L.append(x)"},
            {"q": "4. Dictionaries store data in which format?", "opts": ["Indexes", "Key-Value Pairs", "Tuples", "Objects"], "ans": "Key-Value Pairs"},
            {"q": "5. What is the output of len([10, 20, 30])?", "opts": ["2", "3", "4", "Error"], "ans": "3"}
        ]
    },
    # ------------------ MODULE 4 ------------------
    {
        "id": 4,
        "title": "Module 4: File & Exception Handling",
        "topics": [
            ("File Modes & Operations", """File Handling enables persistent storage.

File Modes:
• 'r': Read mode (default)
• 'w': Write mode (overwrites file)
• 'a': Append mode (adds data to existing content)

Context Manager 'with':
Automatically handles file opening and closing safely."""),
            ("Text & CSV Files", """Reading and Writing Files:

# Writing to Text File
with open("sample.txt", "w") as f:
    f.write("Welcome to Python Learning Platform\\n")

# Reading File
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)"""),
            ("Exception Handling", """Prevents program crashes during runtime errors.

Blocks:
• try: Code that may cause errors
• except: Catches and handles errors
• finally: Always executes regardless of errors

Example:
try:
    res = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")"""),
            ("Log Analyzer Tool", """# Mini Application: Log File Recorder
def log_event(event_message):
    try:
        with open("system.log", "a") as log_file:
            log_file.write(f"LOG: {event_message}\\n")
    except Exception as e:
        print("Logging failed:", e)

log_event("User logged into platform successfully.")"""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which file mode appends content without overwriting?", "opts": ["'r'", "'w'", "'a'", "'x'"], "ans": "'a'"},
            {"q": "2. Which block executes always in error handling?", "opts": ["try", "except", "finally", "else"], "ans": "finally"},
            {"q": "3. What handles 'file closing' automatically in Python?", "opts": ["auto()", "with statement", "close()", "catch()"], "ans": "with statement"},
            {"q": "4. Which keyword raises a manual exception?", "opts": ["throw", "raise", "error", "catch"], "ans": "raise"},
            {"q": "5. Exception raised when dividing a number by zero?", "opts": ["ValueError", "ZeroDivisionError", "TypeError", "IOError"], "ans": "ZeroDivisionError"}
        ]
    },
    # ------------------ MODULE 5 ------------------
    {
        "id": 5,
        "title": "Module 5: Object-Oriented Programming",
        "topics": [
            ("Class & Objects", """OOP models real-world entities into classes and objects.

• Class: Blueprint defining state & behavior.
• Object: Instance of a class.

Example:
class Student:
    pass

s1 = Student()"""),
            ("Constructor & Self", """__init__() Method:
Special constructor method invoked automatically when an object is created.

self Keyword:
Refers to the current instance of the class.

Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age"""),
            ("Four Pillars of OOP", """1. Encapsulation: Restricting direct access to data variables.
2. Inheritance: Deriving child class properties from parent class.
3. Polymorphism: Overriding methods for distinct behavior.
4. Abstraction: Hiding implementation details from users."""),
            ("Banking Management System", """# Mini Application: Account Management System
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance

account = BankAccount("Rajee", 5000)
print("Updated Balance:", account.deposit(1500))"""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which keyword refers to the current class instance?", "opts": ["this", "self", "me", "object"], "ans": "self"},
            {"q": "2. What is the constructor method in Python?", "opts": ["__construct__", "init()", "__init__", "create()"], "ans": "__init__"},
            {"q": "3. Creating child class from parent class is called?", "opts": ["Polymorphism", "Encapsulation", "Inheritance", "Abstraction"], "ans": "Inheritance"},
            {"q": "4. Restricting private access to variables is?", "opts": ["Encapsulation", "Inheritance", "Overriding", "Compilation"], "ans": "Encapsulation"},
            {"q": "5. Can multiple objects be created from one class?", "opts": ["No", "Yes", "Maximum 3", "Only with inheritance"], "ans": "Yes"}
        ]
    },
    # ------------------ MODULE 6 ------------------
    {
        "id": 6,
        "title": "Module 6: Database Connectivity",
        "topics": [
            ("SQLite Connectivity", """Python includes built-in SQLite3 relational database support.

Steps to Connect:
1. import sqlite3
2. conn = sqlite3.connect("database.db")
3. cursor = conn.cursor()
4. cursor.execute("SQL Query")
5. conn.commit()
6. conn.close()"""),
            ("CRUD Operations", """CRUD Operations in SQL:
• Create: CREATE TABLE student (...)
• Read: SELECT * FROM student
• Update: UPDATE student SET marks=90 WHERE id=1
• Delete: DELETE FROM student WHERE id=1"""),
            ("Safe Query Handling", """# Mini App: SQLite Student Score Records
import sqlite3

conn = sqlite3.connect(":memory:") # Temporary DB
cur = conn.cursor()
cur.execute("CREATE TABLE users (id INT, name TEXT)")
# Parameterized query to prevent SQL Injection
cur.execute("INSERT INTO users VALUES (?, ?)", (1, "Bhargavi"))
conn.commit()

cur.execute("SELECT * FROM users")
print("DB Fetch Result:", cur.fetchall())"""),
            ("Interactive Quiz", "QUIZ_MODE"),
        ],
        "quiz": [
            {"q": "1. Which built-in module handles local databases?", "opts": ["mysql", "sqlite3", "dbconnect", "psycopg2"], "ans": "sqlite3"},
            {"q": "2. Which method saves database modifications?", "opts": ["save()", "commit()", "push()", "apply()"], "ans": "commit()"},
            {"q": "3. Parameterized queries ('?') are used to prevent?", "opts": ["Slow speed", "SQL Injection", "Auto Format", "Memory leak"], "ans": "SQL Injection"},
            {"q": "4. Which SQL command retrieves data?", "opts": ["GET", "SELECT", "FETCH", "READ"], "ans": "SELECT"},
            {"q": "5. Which object executes SQL statements in Python?", "opts": ["Connection", "Cursor", "Runner", "Executor"], "ans": "Cursor"}
        ]
    },
    # ------------------ MODULE 7 ------------------
    {
        "id": 7,
        "title": "Module 7: API Integration & Reporting",
        "topics": [
            ("REST APIs & Requests", """APIs (Application Programming Interfaces) allow communication between software applications.

• REST APIs use HTTP methods: GET (Retrieve), POST (Create), PUT (Update), DELETE.
• `requests` library is used to fetch web data."""),
            ("JSON Data & Pandas", """APIs exchange data in JSON (JavaScript Object Notation) format.

Pandas DataFrames convert JSON objects into structured tables for analysis."""),
            ("Reporting & Automation", """# Automation & Dashboard Script Example
import pandas as pd

data = [
    {"Student": "Bhargavi", "Module_Score": 95},
    {"Student": "Rajee", "Module_Score": 98}
]
df = pd.DataFrame(data)
print(df.describe())"""),
            ("Interactive Quiz", "QUIZ_MODE")
        ],
        "quiz": [
            {"q": "1. Which HTTP method retrieves data from an API?", "opts": ["POST", "GET", "PUT", "DELETE"], "ans": "GET"},
            {"q": "2. Which Python library handles DataFrames?", "opts": ["Requests", "Pandas", "Matplotlib", "Tkinter"], "ans": "Pandas"},
            {"q": "3. Standard exchange format returned by REST APIs?", "opts": ["TXT", "CSV", "JSON", "DOCX"], "ans": "JSON"},
            {"q": "4. HTTP Status Code representing successful response?", "opts": ["404", "500", "200", "301"], "ans": "200"},
            {"q": "5. Library used for data visualization & graphs?", "opts": ["Numpy", "Pandas", "Matplotlib", "Streamlit"], "ans": "Matplotlib"}
        ]
    }
]

# =====================================================
# 2. MAIN APPLICATION CLASS (TKINTER)
# =====================================================

class PythonLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Learning Platform - 7 Modules")
        self.root.geometry("1200x750")
        self.root.configure(bg="white")

        self.current_mod_idx = 0
        self.current_topic_idx = 0
        self.is_scorecard_view = False
        self.username = "Student"
        self.quiz_scores = {}
        self.quiz_user_answers = {}
        self.quiz_current_q = 0
        self.quiz_temp_answers = []
        self.selected_opt = tk.StringVar()
        self.show_pass = False

        self.build_login_screen()

    # ------------------ LOGIN SCREEN WITH EYE TOGGLE ------------------
    def build_login_screen(self):
        self.login_frame = tk.Frame(self.root, bg="#F0F9FF")
        self.login_frame.pack(fill="both", expand=True)

        card = tk.Frame(self.login_frame, bg="white", bd=1, relief="solid", padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="🎓 Python Learning Platform", bg="white", fg="#0D47A1", font=("Segoe UI", 22, "bold")).pack(pady=(0, 5))
        tk.Label(card, text="B.Tech Computer Science Learning Portal", bg="white", fg="gray", font=("Segoe UI", 11)).pack(pady=(0, 20))

        # USERNAME FIELD (CLEAN LABEL)
        tk.Label(card, text="Username", bg="white", fg="#1565C0", font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", pady=(10, 2))
        self.user_ent = tk.Entry(card, font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000", bd=1, relief="solid")
        self.user_ent.pack(fill="x", ipady=5, pady=(0, 15))

        # PASSWORD FIELD + EYE BUTTON TOGGLE
        tk.Label(card, text="Password", bg="white", fg="#1565C0", font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", pady=(5, 2))
        
        pass_container = tk.Frame(card, bg="white")
        pass_container.pack(fill="x", pady=(0, 20))

        self.pass_ent = tk.Entry(pass_container, font=("Segoe UI", 12), show="*", bg="#FFFFFF", fg="#000000", bd=1, relief="solid")
        self.pass_ent.pack(side="left", fill="x", expand=True, ipady=5)

        self.eye_btn = tk.Button(
            pass_container, text="👁️", bg="#E0E0E0", fg="black", font=("Segoe UI", 11),
            bd=1, relief="solid", cursor="hand2", padx=8, command=self.toggle_password
        )
        self.eye_btn.pack(side="right", padx=(5, 0), ipady=2)

        tk.Button(
            card, text="Login & Start Learning ▶", bg="#0D47A1", fg="white", font=("Segoe UI", 12, "bold"),
            activebackground="#1565C0", activeforeground="white", bd=0, padx=20, pady=10, cursor="hand2",
            command=self.validate_login
        ).pack(fill="x")

    def toggle_password(self):
        if self.show_pass:
            self.pass_ent.config(show="*")
            self.eye_btn.config(bg="#E0E0E0")
            self.show_pass = False
        else:
            self.pass_ent.config(show="")
            self.eye_btn.config(bg="#90CAF9")
            self.show_pass = True

    def validate_login(self):
        u = self.user_ent.get().strip()
        p = self.pass_ent.get().strip()
        if u != "" and p != "":
            self.username = u
            self.login_frame.destroy()
            self.build_main_dashboard()
        else:
            messagebox.showwarning("Input Error", "Please enter valid Username and Password!")

    # ------------------ MAIN DASHBOARD LAYOUT ------------------
    def build_main_dashboard(self):
        """Build the main application shell and open the Dashboard first."""
        self.header_bar = tk.Frame(self.root, bg="#123B70", height=62)
        self.header_bar.pack(side="top", fill="x")
        self.header_bar.pack_propagate(False)

        tk.Label(
            self.header_bar, text="🐍", bg="#123B70", fg="white",
            font=("Segoe UI", 21, "bold")
        ).pack(side="left", padx=(22, 5))

        tk.Label(
            self.header_bar, text="Python Learning Platform", bg="#123B70",
            fg="white", font=("Segoe UI", 16, "bold")
        ).pack(side="left")

        user_area = tk.Frame(self.header_bar, bg="#123B70")
        user_area.pack(side="right", padx=18)

        tk.Label(
            user_area, text=f"👤  Welcome, {self.username}", bg="#123B70",
            fg="white", font=("Segoe UI", 9, "bold")
        ).pack(side="left", padx=10)

        tk.Button(
            user_area, text="Logout", bg="#315A88", fg="white",
            activebackground="#426D9B", activeforeground="white",
            font=("Segoe UI", 9, "bold"), bd=0, padx=12, pady=5,
            cursor="hand2", command=self.logout
        ).pack(side="left")

        self.dashboard_body = tk.Frame(self.root, bg="#F3F7FB")
        self.dashboard_body.pack(fill="both", expand=True)

        # ---------- LEFT NAVIGATION SIDEBAR ----------
        self.sidebar = tk.Frame(self.dashboard_body, bg="#FFFFFF", width=190)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar, text="Navigation", bg="white", fg="#123B70",
            font=("Segoe UI", 12, "bold"), anchor="w"
        ).pack(fill="x", padx=20, pady=(22, 12))

        self.nav_buttons = {}
        self.create_nav_button("Dashboard", "🏠", self.show_dashboard)
        self.create_nav_button("Modules", "📚", self.show_modules)
        self.create_nav_button("Performance", "📊", self.show_performance)
        self.create_nav_button("About", "ℹ", self.show_about)
        self.create_nav_button("Logout", "🚪", self.logout)

        # Hidden controller kept for the existing next/previous logic.
        self.mod_selector = ttk.Combobox(
            self.sidebar,
            values=[m["title"] for m in modules_data] + ["🏆 Overall Final Scorecard"],
            state="readonly"
        )
        self.mod_selector.current(0)
        self.mod_selector.place(x=-500, y=-500)
        self.mod_selector.bind("<<ComboboxSelected>>", self.on_module_change)

        # ---------- RIGHT MAIN AREA ----------
        self.main = tk.Frame(self.dashboard_body, bg="#F3F7FB")
        self.main.pack(side="left", fill="both", expand=True)

        self.show_dashboard()

    def create_nav_button(self, name, icon, command):
        """Create a real clickable sidebar navigation item."""
        btn = tk.Button(
            self.sidebar,
            text=f"  {icon}   {name}",
            bg="white",
            fg="#334E68",
            activebackground="#DCEBFA",
            activeforeground="#0D47A1",
            font=("Segoe UI", 10, "bold" if name == "Dashboard" else "normal"),
            anchor="w",
            padx=10,
            pady=11,
            bd=0,
            relief="flat",
            cursor="hand2",
            command=command
        )
        btn.pack(fill="x", padx=10, pady=3)
        self.nav_buttons[name] = btn

    def set_active_nav(self, active_name):
        """Highlight the currently selected sidebar item."""
        for name, btn in self.nav_buttons.items():
            if name == active_name:
                btn.config(bg="#DCEBFA", fg="#0D47A1", font=("Segoe UI", 10, "bold"))
            else:
                btn.config(bg="white", fg="#334E68", font=("Segoe UI", 10, "normal"))

    def clear_main(self):
        """Remove the current page from the main area."""
        for widget in self.main.winfo_children():
            widget.destroy()

    def logout(self):
        """Return to the login screen instead of closing the whole program."""
        if messagebox.askyesno("Logout", "Do you want to logout?"):
            for widget in self.root.winfo_children():
                widget.destroy()
            self.current_mod_idx = 0
            self.current_topic_idx = 0
            self.is_scorecard_view = False
            self.show_pass = False
            self.build_login_screen()

    def show_dashboard(self):
        """Display the clean landing dashboard."""
        self.set_active_nav("Dashboard")
        self.clear_main()

        page = tk.Frame(self.main, bg="#F3F7FB")
        page.pack(fill="both", expand=True, padx=22, pady=20)

        welcome_card = tk.Frame(page, bg="white", bd=1, relief="solid")
        welcome_card.pack(fill="x", pady=(0, 14))

        left = tk.Frame(welcome_card, bg="white")
        left.pack(side="left", fill="both", expand=True, padx=25, pady=22)

        tk.Label(
            left, text=f"🎓  Welcome, {self.username}!", bg="white",
            fg="#123B70", font=("Segoe UI", 19, "bold"), anchor="w"
        ).pack(fill="x")

        tk.Label(
            left,
            text="Continue your Python learning journey. Choose Modules to start learning.",
            bg="white", fg="#607080", font=("Segoe UI", 10), anchor="w"
        ).pack(fill="x", pady=(7, 14))

        tk.Button(
            left, text="📚  Open Modules", bg="#0D47A1", fg="white",
            activebackground="#1565C0", activeforeground="white",
            font=("Segoe UI", 10, "bold"), bd=0, padx=18, pady=9,
            cursor="hand2", command=self.show_modules
        ).pack(anchor="w")

        progress_box = tk.Frame(welcome_card, bg="#F5F9FD", bd=1, relief="solid", width=190, height=105)
        progress_box.pack(side="right", padx=20, pady=18)
        progress_box.pack_propagate(False)

        completed = len(self.quiz_scores)
        progress_pct = (completed / len(modules_data)) * 100

        tk.Label(progress_box, text="Overall Progress", bg="#F5F9FD", fg="#334E68",
                 font=("Segoe UI", 8, "bold")).pack(pady=(12, 0))
        tk.Label(progress_box, text=f"{progress_pct:.0f}%", bg="#F5F9FD", fg="#1565C0",
                 font=("Segoe UI", 19, "bold")).pack()
        tk.Label(progress_box, text=f"{completed} / {len(modules_data)} Quizzes Completed",
                 bg="#F5F9FD", fg="#718096", font=("Segoe UI", 7)).pack()

        # Quick overview cards
        tk.Label(page, text="Learning Modules", bg="#F3F7FB", fg="#123B70",
                 font=("Segoe UI", 14, "bold"), anchor="w").pack(fill="x", pady=(2, 8))

        overview = tk.Frame(page, bg="#F3F7FB")
        overview.pack(fill="both", expand=True)
        overview.columnconfigure(0, weight=1)
        overview.columnconfigure(1, weight=1)
        overview.columnconfigure(2, weight=1)

        for i, module in enumerate(modules_data):
            row, col = divmod(i, 3)
            overview.rowconfigure(row, weight=1)
            card = tk.Frame(overview, bg="white", bd=1, relief="solid", cursor="hand2")
            card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

            tk.Label(card, text=f"MODULE {module['id']}", bg="white", fg="#1565C0",
                     font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=13, pady=(12, 3))
            tk.Label(card, text=module["title"].replace(f"Module {module['id']}: ", ""),
                     bg="white", fg="#243B53", font=("Segoe UI", 10, "bold"),
                     wraplength=210, justify="left", anchor="w").pack(fill="x", padx=13)
            tk.Label(card, text=f"{len(module['topics'])} Topics  ›", bg="white", fg="#718096",
                     font=("Segoe UI", 8)).pack(anchor="w", padx=13, pady=(5, 10))

            def open_card(event, index=i):
                self.select_module(index)

            card.bind("<Button-1>", open_card)
            for child in card.winfo_children():
                child.bind("<Button-1>", open_card)

    def select_module(self, index):
        """Open a selected module and its topics."""
        self.current_mod_idx = index
        self.current_topic_idx = 0
        self.is_scorecard_view = False
        if hasattr(self, "mod_selector"):
            self.mod_selector.current(index)
        self.show_modules()

    def show_modules(self):
        """Display all modules with a working vertical scrollbar and topics."""
        self.set_active_nav("Modules")
        self.clear_main()
        self.is_scorecard_view = False

        outer = tk.Frame(self.main, bg="#F3F7FB")
        outer.pack(fill="both", expand=True, padx=22, pady=(18, 8))

        title_row = tk.Frame(outer, bg="#F3F7FB")
        title_row.pack(fill="x", pady=(0, 8))

        self.heading = tk.Label(title_row, text="", bg="#F3F7FB", fg="#123B70",
                                font=("Segoe UI", 14, "bold"), anchor="w")
        self.heading.pack(side="left")

        self.counter = tk.Label(title_row, text="", bg="#F3F7FB", fg="#718096",
                                font=("Segoe UI", 9), anchor="e")
        self.counter.pack(side="right")

        selection_area = tk.Frame(outer, bg="#F3F7FB")
        selection_area.pack(fill="both", expand=True)

        # ---------- SCROLLABLE MODULE LIST ----------
        module_panel = tk.Frame(selection_area, bg="white", bd=1, relief="solid", width=300)
        module_panel.pack(side="left", fill="y", padx=(0, 10))
        module_panel.pack_propagate(False)

        tk.Label(module_panel, text="Select a Module", bg="white", fg="#123B70",
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", padx=15, pady=(14, 9))

        module_list_area = tk.Frame(module_panel, bg="white")
        module_list_area.pack(fill="both", expand=True, padx=8, pady=(0, 8))

        module_canvas = tk.Canvas(module_list_area, bg="white", highlightthickness=0, bd=0)
        module_scroll = tk.Scrollbar(module_list_area, orient="vertical", command=module_canvas.yview)
        module_canvas.configure(yscrollcommand=module_scroll.set)
        module_scroll.pack(side="right", fill="y")
        module_canvas.pack(side="left", fill="both", expand=True)

        module_inner = tk.Frame(module_canvas, bg="white")
        module_window = module_canvas.create_window((0, 0), window=module_inner, anchor="nw")

        def update_module_scroll(event=None):
            module_canvas.configure(scrollregion=module_canvas.bbox("all"))
            module_canvas.itemconfigure(module_window, width=module_canvas.winfo_width())

        module_inner.bind("<Configure>", update_module_scroll)
        module_canvas.bind("<Configure>", update_module_scroll)

        def module_wheel(event):
            module_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        module_canvas.bind("<MouseWheel>", module_wheel)
        module_inner.bind("<MouseWheel>", module_wheel)

        module_colors = ["#E8F2FF", "#E9F8E8", "#F1E9FF", "#FFF1DD", "#E3F7F4", "#FFEAF2", "#EAF0FF"]
        module_text_colors = ["#1565C0", "#2E7D32", "#7B1FA2", "#EF6C00", "#00897B", "#C2185B", "#3949AB"]

        for i, module in enumerate(modules_data):
            selected = (i == self.current_mod_idx)
            card_bg = "#DCEBFA" if selected else module_colors[i]
            card = tk.Frame(module_inner, bg=card_bg, bd=1, relief="solid", cursor="hand2")
            card.pack(fill="x", padx=4, pady=4)

            tk.Label(card, text=str(module["id"]), bg=card_bg, fg=module_text_colors[i],
                     font=("Segoe UI", 9, "bold"), width=2).pack(side="left", padx=(7, 2), pady=10)

            short_title = module["title"].replace(f"Module {module['id']}: ", "")
            tk.Label(card, text=short_title, bg=card_bg, fg=module_text_colors[i],
                     font=("Segoe UI", 9, "bold"), anchor="w", justify="left",
                     wraplength=185).pack(side="left", fill="x", expand=True, pady=9)

            tk.Label(card, text="›", bg=card_bg, fg=module_text_colors[i],
                     font=("Segoe UI", 16, "bold")).pack(side="right", padx=8)

            def choose(event, index=i):
                self.select_module_from_list(index)

            card.bind("<Button-1>", choose)
            for child in card.winfo_children():
                child.bind("<Button-1>", choose)

        # ---------- TOPICS + CONTENT ----------
        right = tk.Frame(selection_area, bg="#F3F7FB")
        right.pack(side="left", fill="both", expand=True)

        topics_panel = tk.Frame(right, bg="white", bd=1, relief="solid", height=150)
        topics_panel.pack(fill="x", pady=(0, 10))
        topics_panel.pack_propagate(False)

        tk.Label(topics_panel, text="Topics", bg="white", fg="#123B70",
                 font=("Segoe UI", 11, "bold"), anchor="w").pack(fill="x", padx=16, pady=(12, 6))

        topic_container = tk.Frame(topics_panel, bg="white")
        topic_container.pack(fill="both", expand=True, padx=12, pady=(0, 10))

        scrollbar = tk.Scrollbar(topic_container)
        scrollbar.pack(side="right", fill="y")

        self.topic_list = tk.Listbox(
            topic_container, font=("Segoe UI", 9), bg="white", fg="#334E68",
            selectbackground="#E2F0FF", selectforeground="#1565C0", relief="flat",
            highlightthickness=0, activestyle="none", yscrollcommand=scrollbar.set
        )
        self.topic_list.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.topic_list.yview)
        self.topic_list.bind("<<ListboxSelect>>", self.on_topic_select)

        self.content_frame = tk.Frame(right, bg="#F8FBFF", bd=1, relief="solid")
        self.content_frame.pack(fill="both", expand=True)

        self.content_body = tk.Frame(self.content_frame, bg="#F8FBFF")
        self.content_body.pack(fill="both", expand=True, padx=18, pady=18)

        # ---------- BOTTOM NAVIGATION ----------
        self.bottom = tk.Frame(outer, bg="#F3F7FB")
        self.bottom.pack(fill="x", pady=(8, 0))
        self.bottom.columnconfigure(0, weight=1)
        self.bottom.columnconfigure(1, weight=2)
        self.bottom.columnconfigure(2, weight=1)

        self.prev_btn = tk.Button(
            self.bottom, text=" ◀ Previous ", bg="#0D47A1", fg="white",
            activebackground="#1565C0", activeforeground="white",
            font=("Segoe UI", 9, "bold"), bd=0, padx=12, pady=7,
            cursor="hand2", command=self.prev_topic
        )
        self.prev_btn.grid(row=0, column=0, sticky="w")

        self.progress = ttk.Progressbar(self.bottom, orient="horizontal", mode="determinate")
        self.progress.grid(row=0, column=1, sticky="ew", padx=25)

        self.next_btn = tk.Button(
            self.bottom, text=" Next ▶ ", bg="#0D47A1", fg="white",
            activebackground="#1565C0", activeforeground="white",
            font=("Segoe UI", 9, "bold"), bd=0, padx=12, pady=7,
            cursor="hand2", command=self.next_topic
        )
        self.next_btn.grid(row=0, column=2, sticky="e")

        self.load_module_topics()

    def select_module_from_list(self, index):
        """Select a module without rebuilding the whole window."""
        self.current_mod_idx = index
        self.current_topic_idx = 0
        self.is_scorecard_view = False
        if hasattr(self, "mod_selector"):
            self.mod_selector.current(index)
        self.load_module_topics()

    def show_performance(self):
        """Open the performance/scorecard page."""
        self.set_active_nav("Performance")
        self.clear_main()
        self.heading = tk.Label(self.main, text="🏆 Performance", bg="#F3F7FB", fg="#123B70",
                                font=("Segoe UI", 15, "bold"), anchor="w")
        self.heading.pack(fill="x", padx=22, pady=(20, 8))
        self.counter = tk.Label(self.main, text=f"Student Performance Report for: {self.username}",
                                bg="#F3F7FB", fg="#718096", font=("Segoe UI", 9), anchor="w")
        self.counter.pack(fill="x", padx=22, pady=(0, 8))
        self.content_frame = tk.Frame(self.main, bg="#F8FBFF", bd=1, relief="solid")
        self.content_frame.pack(fill="both", expand=True, padx=22, pady=(0, 18))
        self.content_body = tk.Frame(self.content_frame, bg="#F8FBFF")
        self.content_body.pack(fill="both", expand=True, padx=18, pady=18)
        self.is_scorecard_view = True
        self.render_overall_scorecard()

    def show_about(self):
        """Open the project information page."""
        self.set_active_nav("About")
        self.clear_main()
        self.heading = tk.Label(self.main, text="ℹ  About the Project", bg="#F3F7FB", fg="#123B70",
                                font=("Segoe UI", 15, "bold"), anchor="w")
        self.heading.pack(fill="x", padx=22, pady=(20, 8))
        self.counter = tk.Label(self.main, text="Python Learning Platform", bg="#F3F7FB",
                                fg="#718096", font=("Segoe UI", 9), anchor="w")
        self.counter.pack(fill="x", padx=22, pady=(0, 8))
        self.content_frame = tk.Frame(self.main, bg="#F8FBFF", bd=1, relief="solid")
        self.content_frame.pack(fill="both", expand=True, padx=22, pady=(0, 18))
        self.content_body = tk.Frame(self.content_frame, bg="#F8FBFF")
        self.content_body.pack(fill="both", expand=True, padx=25, pady=25)
        self.render_about_view()

    # ------------------ CONTROLLER LOGIC ------------------
    def on_module_change(self, event):
        idx = self.mod_selector.current()
        if idx == len(modules_data):
            self.render_overall_scorecard()
        else:
            self.is_scorecard_view = False
            self.current_mod_idx = idx
            self.current_topic_idx = 0
            self.load_module_topics()

    def load_module_topics(self):
        curr_mod = modules_data[self.current_mod_idx]
        self.topic_list.delete(0, tk.END)
        for t_title, _ in curr_mod["topics"]:
            self.topic_list.insert(tk.END, f"  {t_title}")
        self.render_current_topic()

    def on_topic_select(self, event):
        if self.topic_list.curselection():
            self.is_scorecard_view = False
            self.current_topic_idx = self.topic_list.curselection()[0]
            self.render_current_topic()

    def clear_body(self):
        for w in self.content_body.winfo_children():
            w.destroy()

    def update_navigation_buttons(self):
        if not hasattr(self, "prev_btn") or not hasattr(self, "next_btn"):
            return
        if self.is_scorecard_view:
            self.prev_btn.config(state="normal", bg="#0D47A1", cursor="hand2")
            self.next_btn.config(state="disabled", bg="#90A4AE", cursor="arrow")
            return

        if self.current_mod_idx == 0 and self.current_topic_idx == 0:
            self.prev_btn.config(state="disabled", bg="#90A4AE", cursor="arrow")
        else:
            self.prev_btn.config(state="normal", bg="#0D47A1", cursor="hand2")

        self.next_btn.config(state="normal", bg="#0D47A1", cursor="hand2")

    def render_current_topic(self):
        self.is_scorecard_view = False
        curr_mod = modules_data[self.current_mod_idx]
        t_title, t_content = curr_mod["topics"][self.current_topic_idx]

        self.heading.config(text=f"{curr_mod['title']} - {t_title}")
        self.counter.config(text=f"Topic {self.current_topic_idx + 1} of {len(curr_mod['topics'])}")

        self.topic_list.selection_clear(0, tk.END)
        self.topic_list.selection_set(self.current_topic_idx)
        self.topic_list.activate(self.current_topic_idx)

        pct = ((self.current_topic_idx + 1) / len(curr_mod["topics"])) * 100
        self.progress["value"] = pct

        if t_content == "QUIZ_MODE":
            self.render_quiz_view()
        elif t_content == "ABOUT_MODE":
            self.render_about_view()
        else:
            self.render_text_view(t_content)

        self.update_navigation_buttons()

    # CONTINUOUS NAVIGATION (NEXT SWITCHES TO SCORECARD AT END)
    def next_topic(self):
        if self.is_scorecard_view:
            return

        curr_mod = modules_data[self.current_mod_idx]
        if self.current_topic_idx < len(curr_mod["topics"]) - 1:
            self.current_topic_idx += 1
            self.render_current_topic()
        elif self.current_mod_idx < len(modules_data) - 1:
            self.current_mod_idx += 1
            self.current_topic_idx = 0
            self.mod_selector.current(self.current_mod_idx)
            self.load_module_topics()
        else:
            self.render_overall_scorecard()

    def prev_topic(self):
        if self.is_scorecard_view:
            self.is_scorecard_view = False
            self.current_mod_idx = len(modules_data) - 1
            self.mod_selector.current(self.current_mod_idx)
            self.load_module_topics()
            self.current_topic_idx = len(modules_data[self.current_mod_idx]["topics"]) - 1
            self.render_current_topic()
            return

        if self.current_topic_idx > 0:
            self.current_topic_idx -= 1
            self.render_current_topic()
        elif self.current_mod_idx > 0:
            self.current_mod_idx -= 1
            self.mod_selector.current(self.current_mod_idx)
            self.load_module_topics()
            self.current_topic_idx = len(modules_data[self.current_mod_idx]["topics"]) - 1
            self.render_current_topic()

    # ------------------ TEXT & ABOUT VIEWS ------------------
    def render_text_view(self, text_data):
        self.clear_body()
        scrollbar = tk.Scrollbar(self.content_body)
        scrollbar.pack(side="right", fill="y")

        txt = tk.Text(
            self.content_body, wrap="word", font=("Segoe UI", 12), bg="#F8FBFF", fg="#222222",
            padx=15, pady=15, relief="flat", yscrollcommand=scrollbar.set
        )
        txt.pack(fill="both", expand=True)
        scrollbar.config(command=txt.yview)
        txt.insert("1.0", text_data)
        txt.config(state="disabled")

    def render_about_view(self):
        self.clear_body()
        info = """
==================================================
        DEVELOPER DETAILS & PROJECT INFO
==================================================

• Project Title   : Python Learning Platform
• Course Module   : Integrated 7-Module Comprehensive System

--------------------------------------------------
Developed By:
--------------------------------------------------
1) Name           : N. BHARGAVI
   Enrollment No  : 92500122002

2) Name           : K. RAJEE
   Enrollment No  : 92500122006

3) Name           : B.Jasmine
   Enrollment No  : 92500116021

• Branch          : CSE-AI&DS,ML (PBL)
• Section         : 3EI1,3EG1
• Semester        : 3

--------------------------------------------------
PROJECT OBJECTIVES:
--------------------------------------------------
• To provide a comprehensive, interactive Python 
  learning module covering basic syntax to advanced 
  SQLite & API concepts.

• To offer topic-wise self-assessment quizzes with 
  real-time scoring and performance tracking.
==================================================
"""
        tk.Label(self.content_body, text=info, font=("Consolas", 11), bg="#F8FBFF", fg="#1565C0", justify="left").pack(pady=10)

    # ------------------ QUIZ VIEW (SCROLLABLE) ------------------
    def _enable_canvas_mousewheel(self, canvas, inner=None):
        """Make a canvas and its inner frame scroll with both scrollbar and mouse wheel."""
        def on_wheel(event):
            if event.delta:
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind("<MouseWheel>", on_wheel)
        if inner is not None:
            def bind_children(widget):
                widget.bind("<MouseWheel>", on_wheel)
                for child in widget.winfo_children():
                    bind_children(child)
            bind_children(inner)

    def render_quiz_view(self):
        self.clear_body()
        self.quiz_current_q = 0
        self.quiz_temp_answers = []

        # The complete quiz area is scrollable. This prevents the answer
        # options / submit button from being trapped below the visible area.
        quiz_area = tk.Frame(self.content_body, bg="#F8FBFF")
        quiz_area.pack(fill="both", expand=True)

        quiz_canvas = tk.Canvas(quiz_area, bg="#F8FBFF", highlightthickness=0, bd=0)
        quiz_scroll = tk.Scrollbar(quiz_area, orient="vertical", command=quiz_canvas.yview)
        quiz_inner = tk.Frame(quiz_canvas, bg="#F8FBFF")
        quiz_window = quiz_canvas.create_window((0, 0), window=quiz_inner, anchor="nw")
        quiz_canvas.configure(yscrollcommand=quiz_scroll.set)

        quiz_canvas.pack(side="left", fill="both", expand=True)
        quiz_scroll.pack(side="right", fill="y")

        def update_quiz_scroll(event=None):
            quiz_canvas.configure(scrollregion=quiz_canvas.bbox("all"))
            quiz_canvas.itemconfigure(quiz_window, width=quiz_canvas.winfo_width())

        quiz_inner.bind("<Configure>", update_quiz_scroll)
        quiz_canvas.bind("<Configure>", update_quiz_scroll)

        self.q_card = tk.Frame(quiz_inner, bg="#F8FBFF")
        self.q_card.pack(fill="x", expand=True, padx=5, pady=5)

        self.q_lbl = tk.Label(
            self.q_card, text="", font=("Segoe UI", 14, "bold"),
            bg="#F8FBFF", fg="#1565C0", anchor="w", justify="left", wraplength=850
        )
        self.q_lbl.pack(fill="x", pady=(10, 15), padx=10)

        self.r_btns = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.q_card, text="", variable=self.selected_opt, value="",
                font=("Segoe UI", 12), bg="#F8FBFF", fg="#222222",
                anchor="w", justify="left", wraplength=800
            )
            rb.pack(fill="x", pady=7, padx=15)
            self.r_btns.append(rb)

        tk.Button(
            self.q_card, text="Submit Answer ▶", bg="#0D47A1", fg="white",
            font=("Segoe UI", 11, "bold"), bd=1, padx=15, pady=6,
            cursor="hand2", command=self.submit_quiz_q
        ).pack(anchor="e", pady=18, padx=10)

        self.load_quiz_q()
        self._enable_canvas_mousewheel(quiz_canvas, quiz_inner)
        self.root.after(50, update_quiz_scroll)

    def load_quiz_q(self):
        self.selected_opt.set("")
        q_list = modules_data[self.current_mod_idx]["quiz"]
        q_data = q_list[self.quiz_current_q]
        self.q_lbl.config(
            text=f"Question {self.quiz_current_q + 1} of {len(q_list)}: {q_data['q']}"
        )
        for idx, opt in enumerate(q_data["opts"]):
            self.r_btns[idx].config(text=opt, value=opt)

    def submit_quiz_q(self):
        choice = self.selected_opt.get()
        if not choice:
            messagebox.showwarning("Selection Required", "Please select an answer option!")
            return

        q_list = modules_data[self.current_mod_idx]["quiz"]
        correct = q_list[self.quiz_current_q]["ans"]
        is_corr = (choice == correct)

        self.quiz_temp_answers.append({
            "q": q_list[self.quiz_current_q]["q"],
            "user": choice,
            "correct": correct,
            "status": is_corr
        })

        self.quiz_current_q += 1
        if self.quiz_current_q < len(q_list):
            self.load_quiz_q()
            return

        score = sum(1 for x in self.quiz_temp_answers if x["status"])
        pct = (score / len(q_list)) * 100
        mod_id = modules_data[self.current_mod_idx]["id"]
        self.quiz_scores[mod_id] = pct
        self.quiz_user_answers[mod_id] = self.quiz_temp_answers

        # ---------------------------------------------------------
        # QUIZ RESULT: also fully scrollable, including the final
        # completion/certificate button.
        # ---------------------------------------------------------
        self.clear_body()
        result_area = tk.Frame(self.content_body, bg="#F8FBFF")
        result_area.pack(fill="both", expand=True)

        result_canvas = tk.Canvas(result_area, bg="#F8FBFF", highlightthickness=0, bd=0)
        result_scroll = tk.Scrollbar(result_area, orient="vertical", command=result_canvas.yview)
        result_inner = tk.Frame(result_canvas, bg="#F8FBFF")
        result_window = result_canvas.create_window((0, 0), window=result_inner, anchor="nw")
        result_canvas.configure(yscrollcommand=result_scroll.set)

        result_canvas.pack(side="left", fill="both", expand=True)
        result_scroll.pack(side="right", fill="y")

        def update_result_scroll(event=None):
            result_canvas.configure(scrollregion=result_canvas.bbox("all"))
            result_canvas.itemconfigure(result_window, width=result_canvas.winfo_width())

        result_inner.bind("<Configure>", update_result_scroll)
        result_canvas.bind("<Configure>", update_result_scroll)
        self._enable_canvas_mousewheel(result_canvas, result_inner)

        tk.Label(
            result_inner, text="Quiz Completed! 🎉", font=("Segoe UI", 18, "bold"),
            bg="#F8FBFF", fg="#1565C0"
        ).pack(pady=(10, 5))
        tk.Label(
            result_inner, text=f"Score: {score}/{len(q_list)} ({pct:.0f}%)",
            font=("Segoe UI", 14, "bold"), bg="#F8FBFF",
            fg="#2E7D32" if pct >= 60 else "#C62828"
        ).pack(pady=(0, 10))

        for item in self.quiz_temp_answers:
            card = tk.Frame(result_inner, bg="white", bd=1, relief="solid", padx=10, pady=8)
            card.pack(fill="x", expand=True, padx=10, pady=5)
            tk.Label(
                card, text=item["q"], font=("Segoe UI", 10, "bold"),
                bg="white", fg="#222222", anchor="w", justify="left", wraplength=800
            ).pack(fill="x")
            st_color = "#2E7D32" if item["status"] else "#C62828"
            tk.Label(
                card, text=f"Your Answer: {item['user']}", font=("Segoe UI", 10),
                bg="white", fg=st_color, anchor="w"
            ).pack(fill="x")
            if not item["status"]:
                tk.Label(
                    card, text=f"Correct Answer: {item['correct']}",
                    font=("Segoe UI", 10, "bold"), bg="white", fg="#2E7D32", anchor="w"
                ).pack(fill="x")

        tk.Button(
            result_inner, text="Retake Quiz 🔄", bg="#0D47A1", fg="white",
            font=("Segoe UI", 10, "bold"), command=self.render_quiz_view
        ).pack(pady=15)

        if len(self.quiz_scores) == len(modules_data):
            tk.Label(
                result_inner, text="🎓 All 7 Modules Completed!",
                font=("Segoe UI", 14, "bold"), bg="#F8FBFF", fg="#2E7D32"
            ).pack(pady=(5, 8))
            tk.Button(
                result_inner, text="📜 Download Completion Certificate",
                bg="#0D47A1", fg="white",
                activebackground="#1565C0", activeforeground="white",
                font=("Segoe UI", 11, "bold"), bd=0, padx=18, pady=9,
                cursor="hand2", command=self.download_certificate
            ).pack(pady=(0, 25))

        self._enable_canvas_mousewheel(result_canvas, result_inner)
        self.root.update_idletasks()
        update_result_scroll()
        result_canvas.yview_moveto(0)

    # ------------------ COMPLETION CERTIFICATE ------------------
    def download_certificate(self):
        """Create and save a personalized completion certificate."""
        if len(self.quiz_scores) < len(modules_data):
            messagebox.showinfo(
                "Certificate Not Available",
                "Complete all 7 module quizzes to unlock the Completion Certificate."
            )
            return

        safe_name = "".join(ch for ch in self.username if ch.isalnum() or ch in " _-").strip()
        if not safe_name:
            safe_name = "Student"

        save_path = filedialog.asksaveasfilename(
            title="Download Completion Certificate",
            defaultextension=".pdf",
            initialfile=f"{safe_name}_Python_Learning_Completion_Certificate.pdf",
            filetypes=[("PDF Certificate", "*.pdf")]
        )

        if not save_path:
            return

        try:
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.pdfgen import canvas
            from reportlab.lib import colors

            width, height = landscape(A4)
            c = canvas.Canvas(save_path, pagesize=(width, height))

            c.setStrokeColor(colors.HexColor("#0D47A1"))
            c.setLineWidth(3)
            c.rect(28, 28, width - 56, height - 56)
            c.setStrokeColor(colors.HexColor("#90CAF9"))
            c.setLineWidth(1)
            c.rect(40, 40, width - 80, height - 80)

            c.setFillColor(colors.HexColor("#123B70"))
            c.setFont("Helvetica-Bold", 27)
            c.drawCentredString(width / 2, height - 105, "CERTIFICATE OF COMPLETION")

            c.setFillColor(colors.HexColor("#607080"))
            c.setFont("Helvetica", 13)
            c.drawCentredString(width / 2, height - 135, "Python Learning Platform")

            c.setFillColor(colors.HexColor("#334E68"))
            c.setFont("Helvetica", 13)
            c.drawCentredString(width / 2, height - 195, "This is proudly presented to")

            c.setFillColor(colors.HexColor("#0D47A1"))
            c.setFont("Helvetica-Bold", 25)
            c.drawCentredString(width / 2, height - 235, self.username)

            c.setFillColor(colors.HexColor("#334E68"))
            c.setFont("Helvetica", 13)
            c.drawCentredString(
                width / 2, height - 280,
                "for successfully completing all 7 modules and their interactive quizzes."
            )
            c.drawCentredString(
                width / 2, height - 302,
                "Python Fundamentals • Control Flow • Data Structures • File Handling"
            )
            c.drawCentredString(
                width / 2, height - 324,
                "Object-Oriented Programming • Database Connectivity • API Integration & Reporting"
            )

            completion_date = datetime.now().strftime("%d %B %Y")
            c.setFillColor(colors.HexColor("#607080"))
            c.setFont("Helvetica", 11)
            c.drawCentredString(width / 2, height - 385, f"Date of Completion: {completion_date}")

            c.setFillColor(colors.HexColor("#1565C0"))
            c.setFont("Helvetica-Bold", 12)
            c.drawCentredString(width / 2, 92, "Python Learning Platform")
            c.setFillColor(colors.HexColor("#718096"))
            c.setFont("Helvetica", 9)
            c.drawCentredString(width / 2, 72, "Completion Certificate")

            c.save()
            messagebox.showinfo(
                "Certificate Downloaded",
                f"Completion certificate saved successfully.\n\n{save_path}"
            )

        except ImportError:
            messagebox.showerror(
                "Certificate Error",
                "The certificate feature needs ReportLab.\n\nInstall it once using:\npip install reportlab"
            )
        except Exception as e:
            messagebox.showerror("Certificate Error", f"Could not create the certificate.\n\n{e}")

    # ------------------ OVERALL FINAL SCORECARD ------------------
    def render_overall_scorecard(self):
        self.clear_body()
        self.is_scorecard_view = True
        self.mod_selector.current(len(modules_data))

        self.heading.config(text="🏆 Overall Performance Scorecard")
        self.counter.config(text=f"Student Performance Report for: {self.username}")
        self.progress["value"] = 100

        tot_mods = len(modules_data)
        completed = len(self.quiz_scores)
        self.update_navigation_buttons()

        # Full-height scrollable scorecard. Both the scrollbar and mouse
        # wheel work, so the certificate button is always reachable.
        score_area = tk.Frame(self.content_body, bg="#F8FBFF")
        score_area.pack(fill="both", expand=True)

        score_canvas = tk.Canvas(score_area, bg="#F8FBFF", highlightthickness=0, bd=0)
        score_scroll = tk.Scrollbar(score_area, orient="vertical", command=score_canvas.yview)
        score_inner = tk.Frame(score_canvas, bg="#F8FBFF")
        score_window = score_canvas.create_window((0, 0), window=score_inner, anchor="nw")
        score_canvas.configure(yscrollcommand=score_scroll.set)

        score_canvas.pack(side="left", fill="both", expand=True)
        score_scroll.pack(side="right", fill="y")

        def update_score_scroll(event=None):
            score_canvas.configure(scrollregion=score_canvas.bbox("all"))
            score_canvas.itemconfigure(score_window, width=score_canvas.winfo_width())

        score_inner.bind("<Configure>", update_score_scroll)
        score_canvas.bind("<Configure>", update_score_scroll)
        self._enable_canvas_mousewheel(score_canvas, score_inner)

        if completed == 0:
            tk.Label(
                score_inner,
                text="No module quizzes attempted yet!\nComplete module quizzes to generate overall percentage.",
                font=("Segoe UI", 14), bg="#F8FBFF", fg="#C62828",
                justify="center"
            ).pack(pady=50)
        else:
            avg_pct = sum(self.quiz_scores.values()) / tot_mods

            card = tk.Frame(
                score_inner, bg="white", bd=1, relief="solid", padx=20, pady=20
            )
            card.pack(fill="x", padx=20, pady=10)

            tk.Label(
                card, text=f"Student Name: {self.username}",
                font=("Segoe UI", 14, "bold"), bg="white", fg="#1565C0"
            ).pack(pady=(0, 5))

            tk.Label(
                card, text=f"Total Overall Percentage: {avg_pct:.2f}%",
                font=("Segoe UI", 18, "bold"), bg="white", fg="#0D47A1"
            ).pack(pady=5)

            tk.Label(
                card, text=f"Modules Completed: {completed} of {tot_mods}",
                font=("Segoe UI", 11), bg="white", fg="gray"
            ).pack(pady=(0, 15))

            for m in modules_data:
                mid = m["id"]
                score_str = (
                    f"{self.quiz_scores.get(mid, 0):.0f}%"
                    if mid in self.quiz_scores else "Not Attempted"
                )
                row = tk.Frame(
                    card, bg="#F0F0F0", bd=1, relief="solid", padx=10, pady=5
                )
                row.pack(fill="x", pady=4)
                tk.Label(
                    row, text=m["title"], font=("Segoe UI", 11, "bold"),
                    bg="#F0F0F0", fg="#1565C0", anchor="w"
                ).pack(side="left")
                tk.Label(
                    row, text=score_str, font=("Segoe UI", 11, "bold"),
                    bg="#F0F0F0",
                    fg="#2E7D32" if mid in self.quiz_scores else "#C62828"
                ).pack(side="right")

            if completed == tot_mods:
                tk.Label(
                    card, text="🎓 Congratulations! You have completed all 7 modules.",
                    font=("Segoe UI", 11, "bold"), bg="white", fg="#2E7D32"
                ).pack(pady=(16, 7))
                tk.Button(
                    card, text="📜 Download Completion Certificate",
                    bg="#0D47A1", fg="white",
                    activebackground="#1565C0", activeforeground="white",
                    font=("Segoe UI", 10, "bold"), bd=0, padx=16, pady=8,
                    cursor="hand2", command=self.download_certificate
                ).pack(pady=(0, 12))

        # Re-bind after all scorecard widgets have been created so the mouse
        # wheel works even when the pointer is directly over a label/button.
        self._enable_canvas_mousewheel(score_canvas, score_inner)

        # Force one final geometry calculation so the scrollbar knows the
        # complete content height immediately after rendering.
        self.root.update_idletasks()
        update_score_scroll()
        score_canvas.yview_moveto(0)


# =====================================================
# 3. INITIALIZE APP
# =====================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonLearningApp(root)
    root.mainloop()