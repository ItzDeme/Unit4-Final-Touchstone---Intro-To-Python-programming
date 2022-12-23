#this is the classes class haha. It will create a file for the user using the classes template.
import csv
import sys


class Classes(object):
  def __init__(self, filename):
    self.filename = filename
    self.classes_template = 'classestemplate.csv'

    #this function will copy the contents of the classes template and place them into another file
  def create_file(self):
    classes = []
    template= open(self.classes_template, 'r')
    reader = csv.reader(template)
    for row in reader:
      classes.append(row)
    template.close()
    user_classes=open(f'Users/{self.filename}', "w", newline="")
    writer = csv.writer(user_classes)
    writer.writerows(classes)
    print(f'Successfully created {self.filename} within the Users directory')