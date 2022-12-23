#This program is to help keep track of the classes that I will be taking for WGU.

import csv
import sys

#FILENAME = "classes.csv"

#exiting the program
def exit_program():
    print("Terminating program.")
    sys.exit()

#read the classes from the file
def read_classes(FILENAME):
    print(FILENAME)
    try:
        classes = []
        with open(f'Users/{FILENAME}', newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                classes.append(row)
        return classes
    except FileNotFoundError as error:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

#write classes to files
def update_classes(classes,FILENAME):
    try:
        with open(f'Users/{FILENAME}', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(classes)
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_classes(classes):
  for x in classes:
    print(x[0],x[1],x[2])      

#add class to the list
def add_classes(classes):
    class_id_ = input("Enter WGU Class ID:")
    class_ = input("Enter the class: ")
    class__ = [class_id_,class_,'Not Completed']
    classes.append(class__)
    update_classes(classes)
    print(f"Class {class_} was added.\n")


#update the classes, by asking for the school and the class taken at that school
def update_completed_class(classes,FILENAME):
    list_classes(classes)
    class_id = input('Please choose the class you would like to update(Class ID): ')
    school = input('Where was this class taken: ')
    school_class = input('What was the class name you wish to transfer: ')
    found = False
    for i in classes:
      if (i[0] == class_id):
        i[2]= 'Completed'
        i[3]= school
        i[4]= school_class
        found = True

    if (found == False):
      print("Class was not found.\n Please add the class, or correct the class ID.")
    else:
      print(f'{class_id} has been updated!')
      update_classes(classes,FILENAME)

def update_incomplete_class(classes,FILENAME):
    list_classes(classes)
    class_id = input('Please choose the class you would like to update(Class ID): ')
    found = False
    for i in classes:
      if (i[0] == class_id):
        i[2]= 'Not Completed'
        i[3]= ''
        i[4]= ''
        found = True
    print(f'{class_id} has been updated')
    if (found == False):
      print("Class was not found.\n Please add the class, or correct the class ID.")
    else:
      update_classes(classes,FILENAME)
    


#classes = read_classes()

#update_incomplete_class(classes)
#list_classes(classes)
#update_completed_class(classes)
#add_classes(classes)