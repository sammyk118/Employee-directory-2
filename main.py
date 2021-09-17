from tabulate import tabulate
from methods.JSON import *
from methods.CSV import *
from methods.API import load_rand

def main():
    print("welcome to the employee directory!")
    start()


def start():
    print("\nWelcome! choose one of the following commands: \n1: read CSV \n2: write to CSV \n3: read JSON\n4: write to JSON\n5: exit")
    input1 = int(input("write command here: "))

    if input1 == 1:
        data = read_csv()
        print(data)
        start()

    elif input1 == 2:
        entry: str= ""
        name=input("write employee name: ")
        age=input("write employee's age: ")
        dept=input("write employee's department: ")
        entry = name + ", " + age + ", " + dept + "\n"
        append_csv(entry)

        start()

    elif input1 == 3:
        read_json()

        start()

    elif input1 == 4:
        response = load_rand()
        print(response)
        write_json(response)

        start()

    elif input1 == 5:
        exit()

    else:
        print("please enter a valid command")

        start()


main()