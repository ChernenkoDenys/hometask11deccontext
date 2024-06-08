# Створіть простий контекстний менеджер file_opener за допомогою декоратора з contextlib, 
# який буде відкривати файл, повертати його та закривати при виході з контексту

from contextlib import contextmanager


@contextmanager
def file_opener(filename: str, mode: str):
    try:
        file = open(filename, mode)
        yield file
    finally:
        if file is not None:
            file.close()



with file_opener("file.txt", "r") as f:
    print(f.read())