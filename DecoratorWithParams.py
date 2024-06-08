# Напишіть декоратор, який приймає як параметр число, 
# та робить time.sleep перед викликом декорованої функції на це число.
from time import sleep

def sleeper(num):
    
    def decorator(func):
        
        def wrapper(*args, **kwargs):
            sleep(num)
            print("Function started")
            func(*args, **kwargs)
            print("Function finished")
        
        return wrapper
    
    return decorator


# @sleeper(3)
def some_func(a,b,c):
    print("Hi!")
    

# Sleeper function takes a 3 and returns decorator 
# -> decorator takes some_func
# -> return wrapper, which is extend logic of function
# -> in the end wrapper is called 
some_func = sleeper(3)(some_func)
some_func(1,2,3)