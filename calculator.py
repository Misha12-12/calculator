import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор на Python")
        self.root.geometry("300x400")
        
        # Поле ввода
        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Кнопки
        buttons = [
            ('C', 1, 0, 2, 'red'), ('/', 1, 2, 1, 'orange'), ('*', 1, 3, 1, 'orange'),
            ('7', 2, 0, 1, 'lightgray'), ('8', 2, 1, 1, 'lightgray'), ('9', 2, 2, 1, 'lightgray'), ('-', 2, 3, 1, 'orange'),
            ('4', 3, 0, 1, 'lightgray'), ('5', 3, 1, 1, 'lightgray'), ('6', 3, 2, 1, 'lightgray'), ('+', 3, 3, 1, 'orange'),
            ('1', 4, 0, 1, 'lightgray'), ('2', 4, 1, 1, 'lightgray'), ('3', 4, 2, 1, 'lightgray'), 
            ('0', 5, 0, 2, 'lightgray'), ('.', 5, 2, 1, 'lightgray'), ('=', 5, 3, 1, 'blue')
        ]
        
        for text, row, col, span, color in buttons:
            if text == '=':
                btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="white",
                                command=self.calculate)
            elif text == 'C':
                btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="white",
                                command=self.clear)
            else:
                btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="black",
                                command=lambda t=text: self.append_to_display(t))
            
            btn.grid(row=row, column=col, columnspan=span, sticky="nsew", padx=2, pady=2)
        
        # Настройка сетки (чтобы кнопки растягивались)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def append_to_display(self, char):
        current = self.display.get()
        if current == "0" and char != ".":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, char)
        else:
            self.display.insert(tk.END, char)

    def clear(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, "0")

    def calculate(self):
        try:
            expression = self.display.get().replace('×', '*').replace('÷', '/')
            result = eval(expression)
            # Проверка на бесконечность
            if not isinstance(result, complex) and (not str(result).replace('.', '', 1).isdigit()):
                 self.display.delete(0, tk.END)
                 self.display.insert(0, str(result))
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Ошибка")
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Ошибка")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
