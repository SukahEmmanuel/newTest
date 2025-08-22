def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Function has finished running.")
    return wrapper

@announce
def greet():
    print("Hello, world!")

greet()