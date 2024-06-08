# Напишіть декоратор, який буде приймати необмежену кількість типів даних 
# (str, int і так далі) 
# та перевіряти аргументи які передали в 
# декоровану функцію на те чи вони є типами, які передали в декоратор, 
# та повертати помилку якщо ні. Наприклад ми передали @my_decorator(int, str) 
# а декоровану функцію викликали з аргументами func(2, “hello”, True) 
# повинна повернутись помилка бо ми не очікуємо bool тип.

def type_checker(*possible_types):
    
    def decorator_some_func(func):
    
        def wrapper(*args, **kwargs):
            for arguments in args:
                if type(arguments) not in possible_types:
                    raise TypeError("Not correct types in arguments")
            
            for arguments in kwargs.values():
                 if type(arguments) not in possible_types:
                        raise TypeError("Not correct types in arguments")
                
            print("Started function with correct arguments")
            result = func(*args, **kwargs)
            print("Finish function with correct arguments")
            return result
            
        return wrapper
    
    return decorator_some_func


@type_checker(int, str)
def some_func(a, b, c="rofl"):
    print("Hi!")


try:    
    some_func(2, "Hello")
except TypeError as e:
    print(e)