class MortgageCalculator:
    """
    Калькулятор для расчета ипотечных платежей
    """

    def __init__(self, principal: float, annual_rate: float, years: int):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.months = years * 12
        self.monthly_rate = annual_rate / 100 / 12

    def calculate_monthly_payment(self) -> float:
        """Рассчитать ежемесячный платеж по аннуитетной схеме"""
        if self.monthly_rate == 0:
            return self.principal / self.months

        rate_factor = (1 + self.monthly_rate) ** self.months
        monthly_payment = (self.principal * self.monthly_rate * rate_factor) / (rate_factor - 1)
        return round(monthly_payment, 2)

    def calculate_total_payment(self) -> float:
        """Рассчитать общую сумму выплат"""
        monthly_payment = self.calculate_monthly_payment()
        return round(monthly_payment * self.months, 2)

    def calculate_overpayment(self) -> float:
        """Рассчитать переплату по кредиту"""
        total_payment = self.calculate_total_payment()
        return round(total_payment - self.principal, 2)

    def generate_payment_schedule(self) -> list:
        """Сгенерировать график платежей"""
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()

        for month in range(1, self.months + 1):
            interest_payment = balance * self.monthly_rate
            principal_payment = monthly_payment - interest_payment

            if principal_payment > balance:
                principal_payment = balance
                monthly_payment = principal_payment + interest_payment

            balance -= principal_payment

            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),
                'principal': round(principal_payment, 2),
                'interest': round(interest_payment, 2),
                'balance': round(max(balance, 0), 2)
            })

            if balance <= 0:
                break

        return schedule
