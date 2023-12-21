#task 1
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Description: {self.description}"

class Cart:
    def __init__(self):
        self.products = []
    def add_product(self, product, quantity):
        self.products.append((product, quantity))
    def calculate_total(self):
        total = 0
        for product, quantity in self.products:
            total += product.price * quantity
        return total

    def __str__(self):
        cart_contents = ""
        for product, quantity in self.products:
            cart_contents += f"{product.name} - Quantity: {quantity}\n"
        return cart_contents

product1 = Product("Телевізор", 3000, "Гаджет нового покоління")
product2 = Product("Кондиціонер", 6000, "Двоінжекторний пристрій терморегуляції")
product3 = Product("Настінний годинник", 500, "Аксесуар для дому")
product4 = Product("Телефон", 5000, "Смартфон нового покоління")

cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 1)
cart.add_product(product3, 3)
cart.add_product(product4, 4)

print("Кошик:")
print(cart)
print("Загальна вартість:", cart.calculate_total())

#task 2
class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.description} - Ціна: {self.price}"

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes
    def __str__(self):
        category_menu = f"{self.name}:\n"
        for dish in self.dishes:
            category_menu += f"- {dish}\n"
        return category_menu

dish1 = Dish("Броколі", "Дієтичний овочевий салат", 100)
dish2 = Dish("Креветки темпура", "Ніжна японська закуска з хрусткою скоринкою", 250)
dish3 = Dish("Вареники з вишнями", "Традиційна українська кухня", 300)
dish4 = Dish("Шоколадний фондан", "Класичний французький десерт", 90)

category1 = MenuCategory("Закуски", [dish1])
category2 = MenuCategory("Основні страви", [dish2])
category3 = MenuCategory("Десерти", [dish3, dish4])

print("Меню:")
print(category1)
print(category2)
print(category3)