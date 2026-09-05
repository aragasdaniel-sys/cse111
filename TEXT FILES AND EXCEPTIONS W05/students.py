import csv
KEY_INDEX = 0
NAME_INDEX = 1
    
def read_dictionary(filename, key_column_index):
    s_dictionary = {}
    with open(filename,"rt") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            s_dictionary[key_value] = row
    return s_dictionary

def get_student_info(id_number, dictionary):
    name = None
    id_number = id_number.replace("-","")
    if not id_number.isdigit():
        print("Invalid input")
    elif len(id_number) < 9:
        print("Invalid ID Number: too few digits")
    elif len(id_number) > 9:
        print("Invalid ID Number: too many digits")
    else:
        if id_number in dictionary:
            student = dictionary[id_number]
            name = student[NAME_INDEX]
        else:
            print("No such student.")
    return name


def main():
    students = read_dictionary("students.csv", KEY_INDEX)
    inumber = input("Please enter an ID Number (xxxxxxxxx): ")
    student_info = get_student_info(inumber, students)
    if student_info is not None:
        print(student_info)
    
if __name__ == "__main__":
    main()