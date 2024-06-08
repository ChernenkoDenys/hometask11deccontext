#Напишіть декоратор, який буде прінтити 
# “{імʼя функції яку викликали} is been called with parameters: 
# {список параметрів з якими функцію викликали}”, 
# а після виклику функції “Function {function_name} 
# return this value: {значення яке функція повернула}”


def function_info(func):
    
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} is been called with this position paramaters: {args}")
        print(f"{func.__name__} is been called with this key paramaters: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} return this value: {result}")
        
    return wrapper


@function_info
def some_func(a, b, c):
    print("Hi guys!")
    return b


some_func('x', 'z', 5)
