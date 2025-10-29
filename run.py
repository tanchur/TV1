import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import MortgageApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = MortgageApp(root)
    root.mainloop()