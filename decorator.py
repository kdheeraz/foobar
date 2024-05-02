
def deco(fn):
    def wrapper(a,b,c):
        return fn(a,b)+c
    return wrapper
    

@deco
def add(a,b):
    return a+b
    

print(add(4,5,6))