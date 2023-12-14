#task 1
my_list = [1, 2, 3, 5, 6, 7, 8, 9]
def apply_and_sum(numbers, func):
    transformed_list = [func(num) for num in numbers]
    return sum(transformed_list)
def outer(some_list):
    def inner(num):
        return num + 1  
    return apply_and_sum(some_list, inner)
res = outer(my_list)
print(res)  

#task 2
import pickle

def save_result_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'wb') as file:
                pickle.dump(result, file)
            return result
        return wrapper
    return decorator

@save_result_to_file('result.pickle')
def add_numbers(a, b):
    return a + b
result = add_numbers(3, 4)
print(result)  

#task 3
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалась за {execution_time} сек.")
        return result
    return wrapper

@measure_time
def some_function():
    time.sleep(2)
some_function()

#task 4
def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls < max_calls:
                calls += 1
                return func(*args, **kwargs)
            else:
                print("Перевищує ліміт викликів")
                return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")
some_function()
some_function()
some_function()
some_function()

#task 5
def cache_results(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
            return result
    return wrapper

@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))  # Обчислюється
print(fibonacci(10))  # Використання кешу