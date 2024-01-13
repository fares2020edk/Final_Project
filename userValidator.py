import re
import tkinter as tk
from tkinter import messagebox
class UserValidator:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_email(self):

        email_regex = r'^\w+@\w+\.\w+$'
        return re.match(email_regex, self.email)

    def validate_password(self):

        password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
        return re.match(password_regex, self.password)

    def validate_user(self):
        if self.validate_email() and self.validate_password():
            return True
        else:
            return False

class UserValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Validation App")
        self.root.config(bg="lightgreen")


        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()


        tk.Label(root, text="Email:",font=14).pack()
        tk.Entry(root, textvariable=self.email_var,font=14).pack()
        tk.Label(root, text="Password:",font=14).pack()
        tk.Entry(root, textvariable=self.password_var, show="*",font=14).pack()


        tk.Button(root, text="Validate", command=self.validate_user,font=14).pack()

    def validate_user(self):

        email = self.email_var.get()
        password = self.password_var.get()


        user_validator = UserValidator(email, password)


        if user_validator.validate_user():
            messagebox.showinfo("Validation Result", "Email and password are valid!",font=14)
        else:
            messagebox.showerror("Validation Result", "Invalid email or password. Please check the format.",font=14)

