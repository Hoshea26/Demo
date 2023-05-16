import time

def genesis():
    print(f'Hello, world!')
    for i in range(10):
        print(i)
        time.sleep(1)

def print_f():
    print("knock knock")
    for i in range(3):
        print("knock")
        time.sleep(1)
    time.sleep(1)
    print("who's there?")
    var = input()
    print(f"FUCK YOU {var}")

def imporatnt_changes():
    print(f'how many changes would you like to make?')
    var = input()
    time.sleep(3)
    print(f"{var} important changes were made")

if __name__ == '__main__':
    genesis()
    print_f()
    imporatnt_changes()

