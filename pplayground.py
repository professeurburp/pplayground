# all python files are considered as modules
# they always start with other modules import, if needed
import time

# we can define functions in a module
def hello_world():
    print('hello world!')

def play():
    my_name = input("what's your name, friend?\n")
    my_number = input(f'ok, {my_name}, now enter a number between 1 and 100:\n')
    print(f'nice. your number is {my_number}')

if __name__ == '__main__':
    # when a python module is used as an entry point for a script, we need this check
    # https://www.freecodecamp.org/news/if-name-main-python-example/

    hello_world()
    play()

    exit = 5
    print(f'program will exit in {exit} seconds.')
    time.sleep(exit)