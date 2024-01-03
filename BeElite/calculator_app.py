import tkinter as tk
from math import sqrt, log10


def log_function_call(func):
    def wrapper(self, *args, **kwargs):
        print(
            f"Operation: Calling function {func.__name__} clicked on: {args}")
        result = func(self, *args, **kwargs)
        return result
    return wrapper


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.configure(bg="#f0f0f0")

        self.entry_font = ("Helvetica", 36)
        self.button_font = ("Helvetica", 20, "bold")
        self.button_bg = "#e0e0e0"
        self.button_fg = "#333333"

        self.result_var = tk.StringVar()
        self.result_var.set("")
        
        self.memory = 0

        self.create_ui()

    @log_function_call
    def create_ui(self):
        entry = tk.Entry(self.root, textvariable=self.result_var,
                         font=self.entry_font, bd=10, relief="ridge")
        entry.grid(row=0, column=0, columnspan=4,
                   padx=10, pady=10, ipady=10, ipadx=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '%', '√', 'x²', 'log',
            'M+', 'M-', 'MR', 'MC',
            'C'
        ]

        row_position = 1
        column_position = 0
        for label in buttons:
            button = tk.Button(self.root, text=label, width=4, height=2,
                               font=self.button_font, bg=self.button_bg, fg=self.button_fg,
                               command=lambda lbl=label: self.on_button_click(lbl))
            button.grid(row=row_position,
                        column=column_position, padx=5, pady=5, ipadx=5, ipady=5)
            column_position += 1
            if column_position > 3:
                column_position = 0
                row_position += 1

    @log_function_call
    def on_button_click(self, label):
        if label == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif label == "√":
            try:
                result = sqrt(float(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif label == "x²":
            try:
                result = float(self.result_var.get()) ** 2
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif label == "log":
            try:
                result = log10(float(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif label == "C":
            try:
                self.result_var.set(" ")
            except Exception:
                self.result_var.set("Error")
        elif label == "M+":
            try:
                self.memory += float(self.result_var.get())
                self.result_var.set(self.memory)
            except Exception:
                pass
        elif label == "M-":
            try:
                self.memory -= float(self.result_var.get())
                self.result_var.set(self.memory)
            except Exception:
                pass
        elif label == "MR":
            self.result_var.set(str(self.memory))
        elif label == "MC":
            self.memory = 0
        else:
            self.result_var.set(self.result_var.get() + label)



if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
