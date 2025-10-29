import unittest
import sys
import os

# Добавляем корневую директорию в путь Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.calculator import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment(self):
        calculator = MortgageCalculator(1000000, 7.5, 10)
        monthly_payment = calculator.calculate_monthly_payment()
        self.assertAlmostEqual(monthly_payment, 11870.18, places=2)

    def test_total_payment(self):
        calculator = MortgageCalculator(1000000, 7.5, 10)
        total_payment = calculator.calculate_total_payment()
        self.assertAlmostEqual(total_payment, 1424421.60, places=2)

    def test_overpayment(self):
        calculator = MortgageCalculator(1000000, 7.5, 10)
        overpayment = calculator.calculate_overpayment()
        self.assertAlmostEqual(overpayment, 424421.60, places=2)

    def test_zero_interest(self):
        calculator = MortgageCalculator(120000, 0, 1)
        monthly_payment = calculator.calculate_monthly_payment()
        self.assertEqual(monthly_payment, 10000.00)

    def test_payment_schedule_length(self):
        calculator = MortgageCalculator(100000, 5, 1)
        schedule = calculator.generate_payment_schedule()
        self.assertEqual(len(schedule), 12)

    def test_payment_schedule_balance(self):
        calculator = MortgageCalculator(100000, 5, 1)
        schedule = calculator.generate_payment_schedule()
        self.assertAlmostEqual(schedule[-1]['balance'], 0, places=2)