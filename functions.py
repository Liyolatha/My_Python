#functions
'''
def greet(name):
    print(f"Hello, {name}")
    
greet("Emihle")

def add(a, b): #return function
    return a + b

result = add(5, 9)
print(result)
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def greet(name, greeting= "Hello"):
    print(f"{greeting}, {name}")
    
greet("Onele")

greet("Liyolatha", "Good morning")

greet("Olona")