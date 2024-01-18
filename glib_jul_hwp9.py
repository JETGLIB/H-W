# task 1
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def area(self):
        return format(math.pi * self.r ** 2, ".2f")
    def perimeter(self):
        return format(2 * math.pi * self.r, ".2f")

class Rectangle(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return format(self.w * self.h, ".2f")
    def perimeter(self):
        return format(2 * (self.w + self.h), ".2f")

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return format(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)), ".2f")
    def perimeter(self):
        return format(self.a + self.b + self.c, ".2f")

class Square(Figure):
    def __init__(self, side):
        self.side = side
    def area(self):
        return format(self.side ** 2, ".2f")
    def perimeter(self):
        return format(4 * self.side, ".2f")

class RegularPolygon(Figure):
    def __init__(self, n, side):
        self.n = n
        self.side = side
    def area(self):
        return format((self.n * self.side ** 2) / (4 * math.tan(math.pi / self.n)), ".2f")
    def perimeter(self):
        return format(self.n * self.side, ".2f")

if __name__ == "__main__":
    circle = Circle(10)
    print("Circle:")
    print("Area:", circle.area())
    print("Perimeter:", circle.perimeter(), "\n")

    rectangle = Rectangle(4, 8)
    print("Rectangle:")
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter(), "\n")

    triangle = Triangle(3, 4, 5)
    print("Triangle:")
    print("Area:", triangle.area())
    print("Perimeter:", triangle.perimeter(), "\n")

    square = Square(7)
    print("Square:")
    print("Area:", square.area())
    print("Perimeter:", square.perimeter(), "\n")

    heptagon = RegularPolygon(7, 5)
    print("Heptagon:")
    print("Area:", heptagon.area())
    print("Perimeter:", heptagon.perimeter(), "\n")

# task 2
class PaymentOption:
    def pay(self, amount):
        raise NotImplementedError("The 'pay' method must be implemented.")

class CreditCard(PaymentOption):
    def pay(self, amount):
        print(f"Making payment: {amount} with a credit card.")

class BankTransfer(PaymentOption):
    def pay(self, amount):
        print(f"Making bank transfer: {amount}.")

class MobileWallet(PaymentOption):
    def pay(self, amount):
        print(f"Making payment: {amount} with a mobile wallet.")

class PaymentProcessor:
    def __init__(self):
        self.options = []
    def add_option(self, option):
        self.options.append(option)
    def make_payment(self, amount, option_index):
        if 0 <= option_index < len(self.options):
            self.options[option_index].pay(amount)
        else:
            print("Invalid option index.")

if __name__ == "__main__":
    credit_card = CreditCard()
    bank_transfer = BankTransfer()
    mobile_wallet = MobileWallet()

    payment_processor = PaymentProcessor()
    payment_processor.add_option(credit_card)
    payment_processor.add_option(bank_transfer)
    payment_processor.add_option(mobile_wallet)

    payment_processor.make_payment(2500, 0)  
    payment_processor.make_payment(2000, 1)  
    payment_processor.make_payment(1000, 2)   
    payment_processor.make_payment(15000, 3)  