# Напишіть простий декоратор, який буде прінтити повідомлення “Function 
# is been called” до та після виклику функції. Будьте уважні, деворатор повинен працювати 
# з усіма функціями, які приймають різні параметри, та не забувайте повертати результат роботи функції.



def called_decorator(func):
    
    def wrapper(*args, **kwargs):
        print("Functions is been called")
        print(func(*args, **kwargs))
        print("Functions is been called")

    return wrapper


@called_decorator
def some_func(a, b, c="x"):
    return f"Hi!"
    
some_func(3,4, "x")
