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
        self.discount = discount

    def get_total_price(self, order):
        total_price = sum(item.price for item in order)
        discounted_price = total_price * (1 - self.discount.discount())
        return discounted_price


class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price


order = [Dish("Вареники", 100), Dish("Картопля", 50), Dish("Тістечко", 80)]
client_regular = Client("Юлія", RegularDiscount())
total_price_regular = client_regular.get_total_price(order)
print(f"Вартість замовлення для клієнта {client_regular.name}: {total_price_regular}")
client_silver = Client("Лев", SilverDiscount())
total_price_silver = client_silver.get_total_price(order)
print(f"Вартість замовлення для клієнта {client_silver.name}: {total_price_silver}")
client_gold = Client("Ельза", GoldDiscount())
total_price_gold = client_gold.get_total_price(order)
print(f"Вартість замовлення для клієнта {client_gold.name}: {total_price_gold}")
