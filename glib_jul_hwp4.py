#task 1
class InvalidPriceException(Exception):
    pass
class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.set_price(price)
    def set_price(self, price):
        if price <= 0:
            raise InvalidPriceException("Недійсна ціна страви")
        self.price = price
    def __str__(self):
        return f"{self.name} - {self.description} - Ціна: {self.price}"

class MenuCategory:
    def __init__(self, name, dishes):
        self.name = name
        self.dishes = dishes
    def add_dish(self, dish):
        self.dishes.append(dish)
    def remove_dish(self, dish):
        self.dishes.remove(dish)
    def __str__(self):
        category_menu = f"{self.name}:\n"
        for dish in self.dishes:
            category_menu += f"- {dish}\n"
        return category_menu

try:
    dish1 = Dish("Броколі", "Дієтичний овочевий салат", 100)
    dish2 = Dish("Креветки темпура", "Ніжна японська закуска з хрусткою скоринкою", 250)
    dish3 = Dish("Вареники з вишнями", "Традиційна українська кухня", 300)
    dish4 = Dish("Шоколадний фондан", "Класичний французький десерт", 90)
    category1 = MenuCategory("Закуски", [dish1])
    category2 = MenuCategory("Основні страви", [dish2])
    category3 = MenuCategory("Десерти", [dish3, dish4])
    invalid_dish = Dish("Страва з недійсною ціною", "Опис страви", -50)
except InvalidPriceException as e:
    print(f"Помилка: {str(e)}")

print("Меню:")
print(category1)
print(category2)
print(category3)

#task 2
class InvalidDiscountException(Exception):
    pass
class Discount:
    def discount(self):
        pass
class RegularDiscount(Discount):
    def discount(self):
        return 0
class SilverDiscount(Discount):
    def discount(self):
        return 0.05
class GoldDiscount(Discount):
    def discount(self):
        return 0.15
class Client:
    def __init__(self, name, discount):
        self.name = name
        self.set_discount(discount)
    def set_discount(self, discount):
        if not isinstance(discount, Discount):
            raise InvalidDiscountException("Недійсна знижка для клієнта")
        self.discount = discount
    def get_total_price(self, order):
        total_price = sum(item.price for item in order)
        discounted_price = total_price * (1 - self.discount.discount())
        return discounted_price

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.set_price(price)
    def set_price(self, price):
        if price <= 0:
            raise InvalidPriceException("Недійсна ціна страви")
        self.price = price

order = [Dish("Вареники", 100), Dish("Картопля", 50), Dish("Тістечко", 80)]

try:
    client_regular = Client("Юлія", RegularDiscount())
    total_price_regular = client_regular.get_total_price(order)
    print(f"Вартість замовлення для клієнта {client_regular.name}: {total_price_regular}")

    client_silver = Client("Лев", SilverDiscount())
    total_price_silver = client_silver.get_total_price(order)
    print(f"Вартість замовлення для клієнта {client_silver.name}: {total_price_silver}")

    client_gold = Client("Ельза", GoldDiscount())
    total_price_gold = client_gold.get_total_price(order)
    print(f"Вартість замовлення для клієнта {client_gold.name}: {total_price_gold}")

    invalid_client = Client("Іван", "InvalidDiscount")
except InvalidDiscountException as e:
    print(f"Помилка: {str(e)}")
except InvalidPriceException as e:
    print(f"Помилка: {str(e)}")
