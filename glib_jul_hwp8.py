# task 1
class Account:
    def __init__(self, balance):
        self._balance = balance
    @property
    def balance(self):
        return self._balance
    def __setattr__(self, name, value):
        if name == "balance":
            raise AttributeError("Directly changing the balance is not allowed.")
        super().__setattr__(name, value)
    def __getattr__(self, name):
        return f"The property '{name}' does not exist."

if __name__ == "__main__":
    account = Account(30000)
    print(account.balance)
    account._balance = 35000
    print(account.balance)
    print(account.none)

# task 2
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    def __setattr__(self, name, value):
        if name in ["first_name", "last_name"]:
            raise AttributeError
        super().__setattr__(name, value)
    def __getattr__(self, name):
        return f"The property '{name}' does not exist."

if __name__ == "__main__":
    user = User("Юлька", "Глібіщук")
    print(user.first_name)  
    user._first_name = "Ельза" 
    print(user.last_name) 
    print(user.none)  

# task 3
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        raise AttributeError()

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        raise AttributeError()
    
    def area(self):
        return self._width * self._height
    def __getattr__(self, name):
        return f"The property '{name}' does not exist."

if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    print(rectangle.width)  
    print(rectangle.height)  
    print(rectangle.area())  
    rectangle.width = 11  
    print(rectangle.none)  

