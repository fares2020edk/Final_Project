import tkinter  as tk
from tkinter import messagebox
import math
class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg="lightgreen")


        self.fnLabel = tk.Label(master, text="Enter first number: ")
        self.fnLabel.grid(row=0, column=0, padx=5, pady=10)
        self.entry_first_number = tk.Entry(master, width=10,font=(14))
        self.entry_first_number.grid(row=0, column=1, padx=10, pady=15)
        self.entry_first_number.config(bg="green")
        self.snLabel = tk.Label(master, text="Enter second number: ")
        self.snLabel.grid(row=1, column=0, padx=5, pady=10)
        self.entry_second_number = tk.Entry(master, width=10,font=(14))
        self.entry_second_number.grid(row=1, column=1, padx=10, pady=15)
        self.entry_second_number.config(bg="green")

        self.operation_var = tk.IntVar()
        self.operation_var.set(1)


        operations = [("+", 1), ("-", 2), ("/", 3), ("*", 4), ("Square Root", 5), ("Power", 6)]
        for operation_text, operation_value in operations:
            radio_button = tk.Radiobutton(master, text=operation_text, variable=self.operation_var, value=operation_value)
            radio_button.grid(column=2, row=operations.index((operation_text, operation_value)))


        self.result_label = tk.Label(master, text="The result is: ",font=(14))
        self.result_label.grid(row=3, column=1, padx=25, pady=25)


        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_result,font=(14))
        self.calculate_button.grid(row=2, column=1, pady=10)

    def calculate_result(self):
        try:
            first_number = float(self.entry_first_number.get())
            operation = self.operation_var.get()

            if operation != 5:
                second_number = float(self.entry_second_number.get())

            if operation == 1:
                result = first_number + second_number
            elif operation == 2:
                result = first_number - second_number
            elif operation == 3:
                result = first_number / second_number
            elif operation == 4:
                result = first_number * second_number
            elif operation == 5:
                result = math.sqrt(first_number)
            elif operation == 6:
                result = math.pow(first_number, second_number)
            else:
                raise ValueError("Invalid operation")

            self.result_label.config(text=f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

