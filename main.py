# The program will act as a tracker for transferable classes for WGU that need to be finished, vs classes that have already been completed.
# I want to create something that’s convenient and intuitive for use.
# I have created a template of classes that can be taken from other online schools. The user will need to supply their name and where they took the class and the class name they wish to transfer.
# Users will be able to read/write their own files, based off the template provided.Users will need to enter data or use the available options to read data.
# Users will be able to see the classes they need and update the classes they have taken.


from os.path import exists
from os import system
from classes import Classes
import class_functions
import time


#sets a global variable for the filename
#_FILENAME_ = ''

def _introduction_():
  print('Hello thank you for using this ltitle program!')
  answer = input('Do you have a file already? Please enter Yes or No \nAnswer: ').capitalize()
  if answer == 'Yes':
    file_found = 0
    find_file_count = 0
#created a loop that will break if the file is found or the count is above 2
    while not file_found and find_file_count < 3:
      filename = input('Please enter your exact file name without extension: ')
      file_exists = exists(f'Users/{filename}.csv')
      _FILENAME_ = f'{filename}.csv'
      if file_exists:
        print('We found it.')
        time.sleep(5)
        system('clear')
        file_found = 1
        _main_page_(_FILENAME_)
      else:
        print('We could not find your file')
        find_file_count += 1
        if find_file_count >= 3:
          print('Goodbye!')
  elif answer == 'No':
    #create a file for the user and send it to main page to give the user options.
    print('Lets go ahead and create you one!')
    input_filname = input('Please input a file name: ')
    _FILENAME_ = input_filname + '.csv'
    User = Classes(_FILENAME_)
    User.create_file()
    system('clear')
    _main_page_(_FILENAME_)


#the main page where users can choose what options they would like to use.
def _main_page_(_FILENAME_):
  main_page_ = 0
  main_page_counter = 0
  #loops through the main page until counter is above 2
  while not main_page_ and main_page_counter < 3:
    main_answer = input('Please let me know what would you like to do: \n1.List Classes \n2.Mark Class as completed \n3.Unmark Class as Completed \n4.Exit \n5.Clear Screen \nPlease answer with number: ')
    #will call class functions and read the file and list it
    if main_answer == '1':
      _class_list_ =class_functions.read_classes(_FILENAME_)
      class_functions.list_classes(_class_list_)
    #will read file then update the files with the users options. marks classes as complete
    elif main_answer == '2':
      _class_list_ =class_functions.read_classes(_FILENAME_)
      class_functions.update_completed_class(_class_list_,_FILENAME_)
    #will also read the file and mark a class as incomplete
    elif main_answer == '3':
      _class_list_ =class_functions.read_classes(_FILENAME_)
      class_functions.update_incomplete_class(_class_list_,_FILENAME_)
    #closes the program
    elif main_answer == '4':
      class_functions.exit_program()
    #will clear the screen
    elif main_answer == '5':
      system('clear')
    #will loop back to the main page question
    else:
      main_page_counter += 1
      if main_page_counter < 3:
        print('Please enter a valid number, 1 - 4:')
        time.sleep(5)
        system('clear')
      else:
        system('clear')
        class_functions.exit_program()

_introduction_()