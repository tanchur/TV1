import tkinter as tk
import tkinter as tk
from tkinter import ttk, messagebox
from .calculator import MortgageCalculator


class MortgageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор ипотеки")
        self.root.geometry("500x600")

        self.create_widgets()

    def create_widgets(self):
        # Основная рамка
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Поля ввода
        label1 = ttk.Label(main_frame, text="Сумма кредита (руб):")
        label1.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.principal_entry = ttk.Entry(main_frame)
        self.principal_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

        label2 = ttk.Label(main_frame, text="Процентная ставка (% год):")
        label2.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.rate_entry = ttk.Entry(main_frame)
        self.rate_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        label3 = ttk.Label(main_frame, text="Срок кредита (лет):")
        label3.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.years_entry = ttk.Entry(main_frame)
        self.years_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Кнопка расчета
        self.calculate_btn = ttk.Button(
            main_frame, text="Рассчитать", command=self.calculate
        )
        self.calculate_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Поле для результатов
        self.results_text = tk.Text(main_frame, height=15, width=50)
        self.results_text.grid(row=4, column=0, columnspan=2, pady=10)

        # Полосы прокрутки
        scrollbar = ttk.Scrollbar(
            main_frame, orient="vertical", command=self.results_text.yview
        )
        scrollbar.grid(row=4, column=2, sticky=(tk.N, tk.S))
        self.results_text.configure(yscrollcommand=scrollbar.set)

        # Настройка растягивания
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def calculate(self):
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            years = int(self.years_entry.get())

            calculator = MortgageCalculator(principal, rate, years)

            monthly_payment = calculator.calculate_monthly_payment()
            total_payment = calculator.calculate_total_payment()
            overpayment = calculator.calculate_overpayment()

            results = "РЕЗУЛЬТАТЫ РАСЧЕТА:\n"
            results += "=" * 50 + "\n"
            results += f"Ежемесячный платеж: {monthly_payment:,.2f} руб.\n"
            results += f"Общая сумма выплат: {total_payment:,.2f} руб.\n"
            results += f"Переплата: {overpayment:,.2f} руб.\n\n"

            results += "ГРАФИК ПЛАТЕЖЕЙ (первые 12 месяцев):\n"
            header = f"{'Месяц':<6} {'Платеж':<12} {'Основной':<12} "
            header += f"{'Проценты':<12} {'Остаток':<12}\n"
            results += header
            results += "-" * 60 + "\n"

            schedule = calculator.generate_payment_schedule()
            for payment in schedule[:12]:
                row = f"{payment['month']:<6} {payment['payment']:<12,.2f} "
                row += f"{payment['principal']:<12,.2f} {payment['interest']:<12,.2f} "
                row += f"{payment['balance']:<12,.2f}\n"
                results += row

            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, results)

        except ValueError:
            messagebox.showerror(
                "Ошибка", "Пожалуйста, введите корректные числовые значения"
            )
        except Exception:
            messagebox.showerror("Ошибка", "Произошла ошибка при расчете")