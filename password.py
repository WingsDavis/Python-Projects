from customtkinter import *
from tkinter import *
from CTkMessagebox import CTkMessagebox
import random
import string
import time
import customtkinter
from PIL import ImageTk, Image
import os

customtkinter.set_appearance_mode("dark-blue")
customtkinter.set_default_color_theme("dark-blue")


def passer(password):
    chars = string.printable
    chars_list = list(chars)

    guess_password = ""
    
    start_time = time.time()

    while(guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))
        
        # message_label.configure(text="Searching: " + "".join(str(guess_password)))
        print("<-Cracking" + str(guess_password) + "->")

        if (guess_password == list(password)):
            end_time = time.time()
            time_taken = end_time - start_time
            hours, remainder = divmod(time_taken, 3600)
            minutes, seconds = divmod(remainder, 60)
            if hours > 0:
                formatted_time = "{:02} hours".format(int(hours))
            elif minutes > 0:
                formatted_time = "{:02} minutes".format(int(minutes))
            else:
                formatted_time = "{:02} seconds".format(int(seconds))
            message_label.configure(text="Your password is : " + "".join(guess_password) + "\nTime taken: " + formatted_time)
            break

def check_password(password):
    # Check password length
    if len(password) < 8:
        message_label.configure(text="Your password is short. It is recommended to use a password with at least 8 characters.")
    else:
        message_label.configure(text="Your password is long.")
    # Check password strength
    has_symbol = False
    has_uppercase = False
    has_number = False
    for char in password:
        if char in string.punctuation:
            has_symbol = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_number = True
    if has_symbol and has_uppercase and has_number:
        message_label.configure(text="Your password contains a symbol, an uppercase letter, and a number.")
    else:
        message_label.configure(text="Your password does not contain all of the following: a symbol, an uppercase letter, and a number. It is recommended to use a password that contains all of these.")

def generate_password():
    password_length = 9
    password = ""
    while len(password) < password_length:
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
    password = ''.join(random.sample(password, len(password)))
    message_label.configure(text="Your generated password is: " + password)

def ask_question():
    response = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes").get()
    if response == "Yes":
        root.destroy()
    else:
        print("Click 'Yes' to exit!")

def show_frame(frame):
    frame.tkraise()


root = CTk()
root.title('Password Test')
root.rowconfigure((0, 1), weight=1)
root.columnconfigure(0, weight=1)
root.minsize(300, 400)

# Open the image file
# bg_image = Image.open('C:/Users/kofi1/OneDrive/Documents/wp.png')
# bg_photo = ImageTk.PhotoImage(bg_image)

# # Create a label with the image as the background
# bg_label = Label(root, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = CTkLabel(master=root, text="Password System", font=CTkFont(family='SEGOE UI', size=24))
label.grid(padx=20, pady=10, sticky="news")

# Create container frame to hold all other frames
container = CTkFrame(root)
container.grid(padx=140, pady=110, sticky="news")

# Create frames for each tab
frame1 = CTkFrame(container)
frame2 = CTkFrame(container)
frame3 = CTkFrame(container)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='news')

# Tab 1: Check Password
password_label1 = CTkLabel(frame1, text="Password:")
password_label1.grid(padx=80, pady=30, sticky="news")
password_entry1 = CTkEntry(frame1, show="*")
password_entry1.grid(padx=80, pady=30, sticky="news")

check_password_button1 = CTkButton(frame1, text="Check Password", command=lambda: check_password(password_entry1.get()))
check_password_button1.grid(padx=20, pady=10, sticky="news")

# Tab 2: Generate Password
generate_password_button2 = CTkButton(frame2, text="Generate Password", command=generate_password)
generate_password_button2.grid(padx=80, pady=90, sticky="news")

# Tab 3: Test Bruteforce
password_label3 = CTkLabel(frame3, text="Password:")
password_label3.grid(padx=80, pady=30, sticky="news")
password_entry3 = CTkEntry(frame3, show="*")
password_entry3.grid(padx=80, pady=30, sticky="news")

test_bruteforce_button3 = CTkButton(frame3, text="Test Bruteforce", command=lambda: passer(password_entry3.get()))
test_bruteforce_button3.grid(padx=20, pady=10, sticky="news")

# Create buttons to switch between tabs
button_frame = CTkFrame(root)
button_frame.grid(padx=20, pady=10, sticky="news")

check_password_button = CTkButton(button_frame, text="Check Password", command=lambda: show_frame(frame1))
check_password_button.grid(row=0, column=0, padx=20, pady=10, sticky="news")

generate_password_button = CTkButton(button_frame, text="Generate Password", command=lambda: show_frame(frame2))
generate_password_button.grid(row=0, column=1, padx=20, pady=10, sticky="news")

test_bruteforce_button = CTkButton(button_frame, text="Test Bruteforce", command=lambda: show_frame(frame3))
test_bruteforce_button.grid(row=0, column=2, padx=20, pady=10, sticky="news")

# Get the width of the window in pixels
window_width = root.winfo_width()

# Create the message label with a large width and set the wraplength option
message_label = CTkLabel(root, width=50, wraplength=window_width)
message_label.grid(padx=20, pady=10, sticky="news")

quits = CTkButton(root, text="Exit", command=ask_question)
quits.grid(padx=20, pady=10, sticky="news")

# Show first frame
show_frame(frame1)

root.mainloop()
