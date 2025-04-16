def GreetUser(name):
    Greeting = f'Good to see you mr.{name}'

    return Greeting

name = input('Enter your name: ')
print(GreetUser(name))    