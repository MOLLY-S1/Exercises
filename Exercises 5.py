def say_hello():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    return f"hello {first_name.title()} {last_name.title()} from a function"

def calculate_doubles(number):
    double = number *2
    return double

def calculate_half(amount):
    half = amount/2
    return half

def calculate_10m(amount):
    ten = amount+10
    return ten

#Main Routine
print(say_hello())

question = int(input("how Much?"))

print(f"double {question} is {calculate_doubles(question)}")

print(f"half {question} is {calculate_half(question)}")

print(f"10 more than {question} is {calculate_10m(question)}")


