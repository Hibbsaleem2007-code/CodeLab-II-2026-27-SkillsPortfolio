import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ---------------- COLOUR THEME: DRIFTWOOD PEARL ----------------

DRIFTWOOD = "#8B7765"
TAUPE = "#A99582"
PEARL = "#F5F0E8"
CREAM = "#E8DED0"
BROWN = "#5C493B"
DARK_BROWN = "#403329"
GOLD = "#C5A77D"
WHITE = "#FFFFFF"

# ---------------- JOKES AND PUNCHLINES ----------------

jokes = [
    ("Why did the computer go to the doctor?", "Because it had a virus!"),
    ("Why was the maths book sad?", "Because it had too many problems."),
    ("What do you call a bear with no teeth?", "A gummy bear!"),
    ("Why did the student eat his homework?", "Because the teacher said it was a piece of cake."),
    ("What do you call fake spaghetti?", "An impasta!"),
    ("Why can't your nose be 12 inches long?", "Because then it would be a foot."),
    ("What did one wall say to the other wall?", "I'll meet you at the corner."),
    ("Why did the bicycle fall over?", "Because it was two-tired."),
    ("What do you call cheese that isn't yours?", "Nacho cheese!"),
    ("Why did the scarecrow win an award?", "Because he was outstanding in his field."),
    ("What do you call a sleeping bull?", "A bulldozer!"),
    ("Why are frogs so happy?", "Because they eat whatever bugs them."),
    ("What did the ocean say to the beach?", "Nothing, it just waved."),
    ("Why did the tomato turn red?", "Because it saw the salad dressing."),
    ("What do you call a fish wearing a bowtie?", "Sofishticated!"),
    ("Why did the cookie go to the hospital?", "Because it felt crummy."),
    ("What do you call a dinosaur with a big vocabulary?", "A thesaurus!"),
    ("Why don't eggs tell jokes?", "Because they might crack up."),
    ("What is a computer's favourite snack?", "Microchips!"),
    ("Why did the banana go to the doctor?", "Because it wasn't peeling well."),
    ("What do you call a dog magician?", "A Labracadabrador!"),
    ("Why was the broom late?", "It swept in!"),
    ("What did the zero say to the eight?", "Nice belt!"),
    ("Why did the orange stop rolling?", "Because it ran out of juice."),
    ("What do you call an alligator in a vest?", "An investigator!"),
    ("Why did the coffee call the police?", "Because it got mugged."),
    ("What do you call a funny mountain?", "Hill-arious!"),
    ("Why did the phone wear glasses?", "Because it lost its contacts."),
    ("What do you call a lazy kangaroo?", "A pouch potato!"),
    ("Why was the computer cold?", "Because it left its Windows open.")
]

# ---------------- VARIABLES ----------------

current_joke = None
used_jokes = []
meme_photo = None

# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("Alexa, Tell Me a Joke!")
root.geometry("650x620")
root.resizable(False, False)
root.configure(bg=PEARL)

# ---------------- LOAD IMAGE ----------------

meme_image = Image.open("resources/funny_image.jpg")
meme_image = meme_image.resize((105, 105), Image.Resampling.LANCZOS)
meme_photo = ImageTk.PhotoImage(meme_image)

# ---------------- FUNCTIONS ----------------

def getJoke():
    global current_joke

    if len(used_jokes) == len(jokes):
        used_jokes.clear()

    available_jokes = [
        joke for joke in jokes if joke not in used_jokes
    ]

    current_joke = random.choice(available_jokes)
    used_jokes.append(current_joke)

    joke_label.config(text=current_joke[0])

    punchline_label.config(
        text="Press SHOW PUNCHLINE to reveal the answer."
    )


def showPunchline():
    if current_joke is None:
        messagebox.showinfo(
            "No Joke",
            "Please select a joke first!"
        )
    else:
        punchline_label.config(text=current_joke[1])


def nextJoke():
    getJoke()


def quitApp():
    root.destroy()


# ---------------- HEADER ----------------

header = tk.Frame(root, bg=DRIFTWOOD, height=115)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="ALEXA, TELL ME A JOKE!",
    font=("Georgia", 23, "bold"),
    bg=DRIFTWOOD,
    fg=WHITE
).pack(pady=(23, 5))

tk.Label(
    header,
    text="A little laughter makes every day better",
    font=("Arial", 11, "italic"),
    bg=DRIFTWOOD,
    fg=CREAM
).pack()


# ---------------- MAIN CONTENT ----------------

main_frame = tk.Frame(root, bg=PEARL)
main_frame.pack(fill="both", expand=True, padx=35, pady=12)

tk.Label(
    main_frame,
    text="YOUR DAILY DOSE OF HUMOUR",
    font=("Arial", 12, "bold"),
    bg=PEARL,
    fg=TAUPE
).pack(pady=5)


# ---------------- JOKE BOX ----------------

joke_box = tk.Frame(
    main_frame,
    bg=CREAM,
    height=125,
    highlightbackground=TAUPE,
    highlightthickness=2
)

joke_box.pack(fill="x", pady=10)
joke_box.pack_propagate(False)

# JOKE TEXT

joke_label = tk.Label(
    joke_box,
    text="Click 'Tell Me a Joke' to start!",
    font=("Georgia", 16, "bold"),
    bg=CREAM,
    fg=BROWN,
    wraplength=350,
    justify="center"
)

joke_label.pack(
    side="left",
    expand=True,
    fill="both",
    padx=10
)

# ---------------- ADDED IMAGE ----------------

image_label = tk.Label(
    joke_box,
    image=meme_photo,
    bg=CREAM
)

image_label.pack(
    side="right",
    padx=8,
    pady=5
)


# ---------------- PUNCHLINE ----------------

tk.Label(
    main_frame,
    text="THE PUNCHLINE",
    font=("Arial", 11, "bold"),
    bg=PEARL,
    fg=TAUPE
).pack(pady=(8, 3))

punchline_box = tk.Frame(
    main_frame,
    bg=PEARL,
    height=65,
    highlightbackground=GOLD,
    highlightthickness=1
)

punchline_box.pack(fill="x", pady=5)
punchline_box.pack_propagate(False)

punchline_label = tk.Label(
    punchline_box,
    text="Your answer will appear here.",
    font=("Arial", 13, "italic"),
    bg=PEARL,
    fg=DARK_BROWN,
    wraplength=500
)

punchline_label.pack(expand=True, padx=10)


# ---------------- BUTTONS: 2 x 2 GRID ----------------

button_frame = tk.Frame(main_frame, bg=PEARL)
button_frame.pack(pady=15)

# Button 1

joke_button = tk.Button(
    button_frame,
    text="TELL ME A JOKE",
    font=("Arial", 11, "bold"),
    bg=DRIFTWOOD,
    fg=WHITE,
    activebackground=BROWN,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=getJoke
)

joke_button.grid(row=0, column=0, padx=8, pady=7)


# Button 2

punchline_button = tk.Button(
    button_frame,
    text="SHOW PUNCHLINE",
    font=("Arial", 11, "bold"),
    bg=TAUPE,
    fg=WHITE,
    activebackground=DRIFTWOOD,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=showPunchline
)

punchline_button.grid(row=0, column=1, padx=8, pady=7)


# Button 3

next_button = tk.Button(
    button_frame,
    text="NEXT JOKE",
    font=("Arial", 11, "bold"),
    bg=GOLD,
    fg=DARK_BROWN,
    activebackground=TAUPE,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=nextJoke
)

next_button.grid(row=1, column=0, padx=8, pady=7)


# Button 4

quit_button = tk.Button(
    button_frame,
    text="QUIT",
    font=("Arial", 11, "bold"),
    bg=CREAM,
    fg=BROWN,
    activebackground=DRIFTWOOD,
    activeforeground=WHITE,
    width=22,
    height=2,
    relief="flat",
    cursor="hand2",
    command=quitApp
)

quit_button.grid(row=1, column=1, padx=8, pady=7)


# ---------------- FOOTER ----------------

tk.Label(
    main_frame,
    text="Made for a little moment of happiness",
    font=("Arial", 9, "italic"),
    bg=PEARL,
    fg=TAUPE
).pack(pady=3)


# ---------------- START APPLICATION ----------------

root.mainloop()