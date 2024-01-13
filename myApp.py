#Eman and Faris python project(EF_Students_kit)
import time
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import math
from calculatorApp import CalculatorApp
from noteApp import NoteApp
from countdownTimerApp import CountdownTimerApp
from userValidator import UserValidator
from userValidator import UserValidatorApp




class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Log in")
        self.root.config(bg="lightgreen")






        self.email_label = tk.Label(root,text="Enter your Email",width=60,font=(14))
        self.email_label.pack()
        self.email_entry = tk.Entry(root, width=30,font=(14))
        self.email_entry.pack(pady=10)

        self.password_label = tk.Label(root,text="Enter your password", font=(14))
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*", width=30, font=(14))
        self.password_entry.pack(pady=10)

        # Button for user validation
        self.login_button = tk.Button(root, text="Login",font=(14), command=self.validate_user)
        self.login_button.pack(pady=10)

    def validate_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        user_validator = UserValidator(email, password)

        if user_validator.validate_user():
            messagebox.showinfo("Login Successful", "Logged in successfully!")
            self.show_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password. Please check the format.")

    def show_main_menu(self):

        main_menu = tk.Toplevel(self.root)
        main_menu.title("Main Menu")
        main_menu_label = tk.Label(main_menu,text="EF_Students_Kit",bg="green",font=(25))
        main_menu_label.pack(pady=20,padx=400)


        calculator_button = tk.Button(main_menu, text="Calculator",font=(20) ,bg="green", command=self.open_calculator)
        calculator_button.pack(pady=20,padx=40)

        notes_button = tk.Button(main_menu, text="Notes",font=(20),bg="green", command=self.open_notes)
        notes_button.pack(pady=20,padx=40)

        timer_button = tk.Button(main_menu, text="Study Timer",font=(20),bg="green" ,command=self.open_study_timer)
        timer_button.pack(pady=20,padx=40)

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.root)
        calculator_app = CalculatorApp(calculator_window)

    def open_notes(self):
        notes_window = tk.Toplevel(self.root)
        notes_app = NoteApp(notes_window)

    def open_study_timer(self):
        timer_window = tk.Toplevel(self.root)
        timer_app = CountdownTimerApp(timer_window)


root = tk.Tk()
app = MainApplication(root)
root.mainloop()
