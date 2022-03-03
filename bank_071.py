#!/usr/bin/env python3

class BankAccount():

    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def deposit(self, new_bal):
        self.balance = self.balance + new_bal

    def print_attributes(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.number}")
        print(f"Balance: {self.balance:.2f}")
