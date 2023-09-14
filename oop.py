#!/usr/bin/env python3

class Rocket:
    def __init__(self, length, speed, brand) -> None:
        self.length = length
        self.speed = speed
        self.brand = brand
        
    def brand_name(self):
        return self.brand
    
## using a function inside another
    
def print_message(message):
    def message_sender():
        print(message)
    message_sender()
    
print_message("A random message\n")

## using a decorator for uppercasing strings

def uppercase_decorator(function): ##say_hi return enters here as 'this is a test\n'
    def wrapper():
        func = function() #'this is a test\n'
        make_uppercase = func.upper() #'THIS IS A TEST\n'
        return make_uppercase
    
    return wrapper #returns make_uppercase


@uppercase_decorator    
def say_hi():
    return 'this is a test\n'
    
print(say_hi())
        
#this decorator extract arguments of cities functions and also runs it

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"My arguments are: {arg1}, {arg2}")
        function(arg1, arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print(f"Cities I love are {city_one} and {city_two}\n")
    
cities("Nairobi", "Accra")

def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper function"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}\n".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")


