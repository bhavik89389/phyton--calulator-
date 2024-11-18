import tkinter as tk
from tkinter import messagebox

# below code creates  the main application window
root = tk.Tk()
root.title("Calculator")

#used for setting size of display window
root.geometry("650x650")

# A variable to store the expression
expression = ""

# Function to update the expression on the screen
def update_expression(value):
    global expression
    expression += str(value)
    entry_var.set(expression)

# Function to evaluate the expression and show the result
def evaluate_expression():
    try:
        global expression
        result = str(eval(expression)) 
        entry_var.set(result)
        expression = result  
    except Exception as e:
        entry_var.set("Error")
        expression = ""  # Clear expression if there's an error

# Function to clear the input(we can type another operation after clearing the function )
def clear_input():
    global expression
    expression = ""
    entry_var.set(expression)

# function can be used as a backspace command 
def backspace():
    global expression
    expression = expression[:-1]
    entry_var.set(expression)

# Create the input display for the calculator
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 24), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Createing  the buttons on the calculator window
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('<', 5, 1), ('√', 5, 2), ('^', 5, 3)
]

#  adding buttons to the grid 
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), command=evaluate_expression, width=10, height=3)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear_input, width=10, height=3)
    elif text == "<":
        button = tk.Button(root, text=text, font=("Arial", 18), command=backspace, width=10, height=3)
    elif text == "√":
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda: update_expression("**(1/2)"), width=10, height=3)
    elif text == "^":
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda: update_expression("**"), width=10, height=3)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda value=text: update_expression(value), width=10, height=3)

    button.grid(row=row, column=col, padx=7, pady=7)

# Run the application
root.mainloop()
