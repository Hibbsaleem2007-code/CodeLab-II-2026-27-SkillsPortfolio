from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ---------------- SAGE PERIDOT MORNING THEME ----------------

SAGE = "#A8B89A"
DARK_SAGE = "#657D62"
DEEP_SAGE = "#405B49"
PERIDOT = "#B5C878"
LIGHT_PERIDOT = "#DCE8B5"
CREAM = "#F8F6E9"
WHITE = "#FFFFFF"
DARK = "#26382D"
MUTED = "#647565"
RED = "#B85C50"
LIGHT_GREEN = "#D8E8C6"

# ---------------- WINDOW ----------------

root = Tk()
root.title("Math Quiz | Challenge Your Mind")
root.geometry("980x720")
root.minsize(850, 650)
root.configure(bg=SAGE)

# ---------------- VARIABLES ----------------

total_questions = 10
question_number = 0
score = 0
attempt_number = 1
correct_answer = 0
selected_level = ""
minimum = 1
maximum = 9
current_operation = "+"
question_active = False

# ---------------- HELPER FUNCTIONS ----------------

def clear_screen():
    for widget in content_frame.winfo_children():
        if widget != background_label:
            widget.destroy()


def make_button(parent, text, command, bg=DEEP_SAGE,
                fg=WHITE, width=18):

    return Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        activebackground=PERIDOT,
        activeforeground=DARK,
        font=("Segoe UI", 11, "bold"),
        relief=FLAT,
        bd=0,
        cursor="hand2",
        width=width,
        pady=11
    )


# ---------------- HEADER ----------------

def show_header():

    header = Frame(root, bg=SAGE, height=140)
    header.pack(fill=X, padx=35, pady=(18, 5))
    header.pack_propagate(False)

    title_area = Frame(header, bg=SAGE)
    title_area.pack(side=LEFT, fill=BOTH, expand=True)

    Label(
        title_area,
        text="THE DAILY BRAIN CHALLENGE",
        bg=SAGE,
        fg=DEEP_SAGE,
        font=("Segoe UI", 9, "bold")
    ).pack(anchor=W, pady=(20, 5))

    Label(
        title_area,
        text="MATH QUIZ",
        bg=SAGE,
        fg=DARK,
        font=("Georgia", 34, "bold")
    ).pack(anchor=W)

    Label(
        title_area,
        text="Think fast. Solve smart. Reach 100 points.",
        bg=SAGE,
        fg=MUTED,
        font=("Segoe UI", 11)
    ).pack(anchor=W, pady=(5, 0))


# ---------------- MAIN CONTENT ----------------

content_frame = Frame(
    root,
    bg=CREAM,
    highlightthickness=1,
    highlightbackground=PERIDOT
)

content_frame.pack(
    fill=BOTH,
    expand=True,
    padx=35,
    pady=(8, 20)
)


# ---------------- FULL BACKGROUND IMAGE ----------------

# Keep math_quiz.webp in the same folder as this Python file.

background_image = Image.open("resources\math _ quiz _ image.webp")
background_photo = None

background_label = Label(
    content_frame,
    bd=0
)

background_label.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)

background_label.lower()


def resize_background(event):

    global background_photo

    if event.width < 2 or event.height < 2:
        return

    resized = background_image.resize(
        (event.width, event.height),
        Image.Resampling.LANCZOS
    )

    background_photo = ImageTk.PhotoImage(resized)

    background_label.config(image=background_photo)


content_frame.bind(
    "<Configure>",
    resize_background
)


# ---------------- BACK TO HOME FUNCTION ----------------

def confirmQuit():

    answer = messagebox.askyesno(
        "Back to Home",
        "Are you sure you want to leave the current quiz and go back home?"
    )

    if answer:
        global question_active
        question_active = False
        displayMenu()


# ---------------- FUNCTION 1: DISPLAY MENU ----------------

def displayMenu():

    clear_screen()

    Label(
        content_frame,
        text="CHOOSE YOUR DIFFICULTY",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 10, "bold")
    ).pack(pady=(28, 5))

    Label(
        content_frame,
        text="How challenging should it be?",
        bg=CREAM,
        fg=DARK,
        font=("Georgia", 22, "bold")
    ).pack(pady=(0, 8))

    Label(
        content_frame,
        text="Choose a level to start your 10-question quiz.",
        bg=CREAM,
        fg=MUTED,
        font=("Segoe UI", 11)
    ).pack(pady=(0, 20))

    levels = [
        ("1", "EASY", "Single-digit numbers | 1 to 9"),
        ("2", "MODERATE", "Double-digit numbers | 10 to 99"),
        ("3", "ADVANCED", "Four-digit numbers | 1000 to 9999")
    ]

    for number, level, description in levels:

        card = Frame(
            content_frame,
            bg=LIGHT_PERIDOT,
            padx=18,
            pady=10
        )

        card.pack(fill=X, padx=100, pady=6)

        Label(
            card,
            text=number,
            bg=DEEP_SAGE,
            fg=WHITE,
            font=("Segoe UI", 15, "bold"),
            width=3,
            pady=8
        ).pack(side=LEFT, padx=(0, 15))

        text_box = Frame(
            card,
            bg=LIGHT_PERIDOT
        )

        text_box.pack(side=LEFT, fill=X, expand=True)

        Label(
            text_box,
            text=level,
            bg=LIGHT_PERIDOT,
            fg=DARK,
            font=("Segoe UI", 12, "bold")
        ).pack(anchor=W)

        Label(
            text_box,
            text=description,
            bg=LIGHT_PERIDOT,
            fg=MUTED,
            font=("Segoe UI", 9)
        ).pack(anchor=W)

        make_button(
            card,
            "SELECT",
            lambda value=level: startQuiz(value),
            bg=DEEP_SAGE,
            fg=WHITE,
            width=10
        ).pack(side=RIGHT, padx=5)

    Label(
        content_frame,
        text="10 Questions | 100 Points | 2 Attempts Per Question",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 9, "bold")
    ).pack(pady=20)


# ---------------- FUNCTION 2: RANDOM INTEGER ----------------

def randomInt(min_value, max_value):
    return random.randint(min_value, max_value)


# ---------------- FUNCTION 3: DECIDE OPERATION ----------------

def decideOperation():
    return random.choice(["+", "-"])


# ---------------- START QUIZ ----------------

def startQuiz(level):

    global selected_level, minimum, maximum
    global question_number, score, attempt_number

    selected_level = level

    if level == "EASY":
        minimum, maximum = 1, 9

    elif level == "MODERATE":
        minimum, maximum = 10, 99

    else:
        minimum, maximum = 1000, 9999

    question_number = 0
    score = 0
    attempt_number = 1

    displayProblem()


# ---------------- FUNCTION 4: DISPLAY PROBLEM ----------------

def displayProblem():

    global question_number, attempt_number
    global correct_answer, current_operation
    global question_active
    global answer_entry, feedback_label, attempt_label

    clear_screen()

    question_number += 1
    attempt_number = 1
    question_active = True

    first_number = randomInt(minimum, maximum)
    second_number = randomInt(minimum, maximum)

    current_operation = decideOperation()

    if current_operation == "+":
        correct_answer = first_number + second_number

    else:
        correct_answer = first_number - second_number

    top_row = Frame(
        content_frame,
        bg=CREAM
    )

    top_row.pack(
        fill=X,
        padx=35,
        pady=(25, 12)
    )

    Label(
        top_row,
        text=f"QUESTION {question_number:02d} / {total_questions}",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 10, "bold")
    ).pack(side=LEFT)

    Label(
        top_row,
        text=f"{selected_level} LEVEL",
        bg=CREAM,
        fg=DEEP_SAGE,
        font=("Segoe UI", 10, "bold")
    ).pack(side=RIGHT)

    progress_bg = Frame(
        content_frame,
        bg=SAGE,
        height=7
    )

    progress_bg.pack(fill=X, padx=35)
    progress_bg.pack_propagate(False)

    progress_fill = Frame(
        progress_bg,
        bg=PERIDOT,
        width=int((question_number / total_questions) * 800),
        height=7
    )

    progress_fill.pack(side=LEFT)

    Label(
        content_frame,
        text="Solve this problem",
        bg=CREAM,
        fg=DARK,
        font=("Georgia", 21, "bold")
    ).pack(pady=(28, 10))

    Label(
        content_frame,
        text=f"{first_number:,}   {current_operation}   {second_number:,}   =",
        bg=DEEP_SAGE,
        fg=WHITE,
        font=("Georgia", 31, "bold"),
        padx=35,
        pady=24
    ).pack(pady=8)

    Label(
        content_frame,
        text="TYPE YOUR ANSWER",
        bg=CREAM,
        fg=MUTED,
        font=("Segoe UI", 9, "bold")
    ).pack(pady=(22, 7))

    answer_entry = Entry(
        content_frame,
        font=("Segoe UI", 20, "bold"),
        justify=CENTER,
        width=15,
        bg=WHITE,
        fg=DARK,
        relief=FLAT,
        bd=0
    )

    answer_entry.pack(ipady=10)
    answer_entry.focus_set()

    attempt_label = Label(
        content_frame,
        text="Attempt 1 of 2",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 10, "bold")
    )

    attempt_label.pack(pady=(12, 2))

    feedback_label = Label(
        content_frame,
        text="You have two chances to answer.",
        bg=CREAM,
        fg=MUTED,
        font=("Segoe UI", 10)
    )

    feedback_label.pack(pady=5)

    # SUBMIT ANSWER BUTTON

    make_button(
        content_frame,
        "SUBMIT ANSWER",
        checkAnswer,
        bg=DEEP_SAGE,
        fg=WHITE,
        width=22
    ).pack(pady=(12, 5))

    # BACK TO HOME BUTTON

    make_button(
        content_frame,
        "BACK TO HOME",
        confirmQuit,
        bg=RED,
        fg=WHITE,
        width=22
    ).pack(pady=(5, 10))

    answer_entry.bind(
        "<Return>",
        lambda event: checkAnswer()
    )


# ---------------- FUNCTION 5: IS CORRECT ----------------

def isCorrect(user_answer, correct_value):
    return user_answer == correct_value


# ---------------- CHECK ANSWER ----------------

def checkAnswer():

    global score, attempt_number, question_active

    if not question_active:
        return

    answer_text = answer_entry.get().strip()

    if answer_text == "":

        feedback_label.config(
            text="Please enter an answer first.",
            fg=RED
        )

        return

    try:

        user_answer = int(answer_text.replace(",", ""))

    except ValueError:

        feedback_label.config(
            text="Please enter a whole number.",
            fg=RED
        )

        answer_entry.delete(0, END)
        return

    if isCorrect(user_answer, correct_answer):

        if attempt_number == 1:

            score += 10

            feedback_label.config(
                text="Correct! Excellent work. +10 points",
                fg=DARK_SAGE
            )

        else:

            score += 5

            feedback_label.config(
                text="Correct on your second attempt. +5 points",
                fg=DARK_SAGE
            )

        question_active = False

        root.after(850, nextQuestion)

    else:

        if attempt_number == 1:

            attempt_number = 2

            attempt_label.config(
                text="Attempt 2 of 2"
            )

            feedback_label.config(
                text="Not quite! Try one more time.",
                fg=RED
            )

            answer_entry.delete(0, END)
            answer_entry.focus_set()

        else:

            question_active = False

            feedback_label.config(
                text=f"Good try! The correct answer was {correct_answer:,}.",
                fg=RED
            )

            root.after(1300, nextQuestion)


# ---------------- NEXT QUESTION ----------------

def nextQuestion():

    if question_number < total_questions:
        displayProblem()

    else:
        displayResults()


# ---------------- FUNCTION 6: DISPLAY RESULTS ----------------

def displayResults():

    clear_screen()

    if score > 90:
        rank = "A+"
        message = "Outstanding! You are a maths star."

    elif score >= 80:
        rank = "A"
        message = "Excellent work. Keep it up!"

    elif score >= 70:
        rank = "B"
        message = "Great effort. You are doing well."

    elif score >= 60:
        rank = "C"
        message = "Good try. A little more practice will help."

    elif score >= 50:
        rank = "D"
        message = "Keep practising. You can improve!"

    else:
        rank = "Needs Practice"
        message = "Do not give up. Try another round!"

    Label(
        content_frame,
        text="QUIZ COMPLETED",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 10, "bold")
    ).pack(pady=(38, 8))

    Label(
        content_frame,
        text="Your final result",
        bg=CREAM,
        fg=DARK,
        font=("Georgia", 25, "bold")
    ).pack(pady=5)

    Label(
        content_frame,
        text=f"{score} / 100",
        bg=DEEP_SAGE,
        fg=WHITE,
        font=("Georgia", 38, "bold"),
        padx=35,
        pady=18
    ).pack(pady=15)

    Label(
        content_frame,
        text=f"RANK: {rank}",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 18, "bold")
    ).pack(pady=5)

    Label(
        content_frame,
        text=message,
        bg=CREAM,
        fg=MUTED,
        font=("Segoe UI", 11)
    ).pack(pady=5)

    Label(
        content_frame,
        text="You answered 10 questions. Maximum score: 100 points.",
        bg=CREAM,
        fg=DARK_SAGE,
        font=("Segoe UI", 9)
    ).pack(pady=10)

    make_button(
        content_frame,
        "PLAY AGAIN",
        replayQuiz,
        bg=DEEP_SAGE,
        fg=WHITE,
        width=20
    ).pack(pady=(18, 8))

    make_button(
        content_frame,
        "EXIT QUIZ",
        root.destroy,
        bg=DARK_SAGE,
        fg=WHITE,
        width=20
    ).pack(pady=5)


# ---------------- REPLAY QUIZ ----------------

def replayQuiz():

    answer = messagebox.askyesno(
        "Play Again?",
        "Would you like to play another 10-question quiz?"
    )

    if answer:
        displayMenu()

    else:
        root.destroy()


# ---------------- RUN APPLICATION ----------------

show_header()
displayMenu()
root.mainloop()