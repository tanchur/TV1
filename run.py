import sys
import os
import tkinter as tk

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import MortgageApp

if __name__ == "__main__":
    root = tk.Tk()
    app = MortgageApp(root)
    root.mainloop()

