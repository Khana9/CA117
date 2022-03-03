#!/usr/bin/env python3

class BankAccount():
    def __init__(bank, bal=0.00):
        bank.balance = 0.00 + bal

    def deposit(self, new_bal):
        self.balance = self.balance + new_bal

    def withdraw(self, new_bal):
        if new_bal <= self.balance:
            self.balance = self.balance - new_bal

    def __str__(self):
        return 'Your current balance is {:.02f} euro'.format(self.balance)

    pass
