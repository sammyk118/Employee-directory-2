import os
import csv

path = "data/users.csv"
def append_csv(entry):
    file_write = open(path, "a")
    file_write.write(entry)
    file_write.close()


def read_csv():
    if os.stat(path).st_size == 0:
        print("file is empty!")
        init_csv()
    with open(path) as file:
        csv_file = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_file:
            if line_count == 0:
                print(f'column names: {", ".join(row)}')
                line_count += 1
            else:
                print(f'{row[0]} works in the {row[1]} department, and is {row[2]} years old')
                line_count += 1



def init_csv():
    file_overwrite = open(path, "w")
    file_overwrite.write("Name, Age, Department\n")