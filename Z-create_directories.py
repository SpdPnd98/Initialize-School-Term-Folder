import sys
import os
import json

def create_directory(parent,child):
  try:
    print("Creating folder " + child + " at " + parent)
    os.mkdir(parent + "/" + child)
  except OSError:
    print("Directory already exist!")
  else:
    print("-------- Successfully Created---------------")

def child_directory(parent_path, parent_json, index):
  create_directory(parent_path, parent_json["name"])
  if "generate_weeks" in parent_json:
    for week_number in range (0, parent_json["generate_weeks"] + 1):
        create_directory(parent_path + "/" + parent_json["name"], "Week " + str(week_number))
  if "child" not in parent_json:
    return # no children in child
  else:
    child_directory(parent_path + "/" + parent_json["name"], parent_json["child"][index], 0)
  if index < (len(parent_json["child"]) - 1):
    print("Number of childrens at" + parent_path + parent_json["name"] + ":" + str(len(parent_json["child"])))
    child_directory(parent_path + "/" + parent_json["name"], parent_json["child"][index + 1], 0)
  else:
    return

if len(sys.argv)==1:
  print("Please create a directory config file")
  sys.exit()
for config in range(1,len(sys.argv)):
  with open(sys.argv[config]) as file:
    file_directory = json.load(file)

  print("The following is the file structure:")
  print(file_directory)
  usr_input = input("Do you wish to proceed? [Y/n]")

  if usr_input != "Y" and usr_input != "y":
    print("operation aborted")
  else:
    path = os.getcwd()
    exit_flag = False
    if "name" not in file_directory:
      print("No file name specified, aborting...")
      exit_flag = True
    if "generate_weeks" not in file_directory:
      print("You are defeating the purpose of this script!")
      exit_flag = True
    if "child" not in file_directory:
      print("Checks for now only go one direcotry deep, please be responsible for creating your json files")
      for child in file_directory["child"]:
        if child["name"] == None:
          print("The child folder has no name! Plase name your children in the config file...")
          exit_flag = True
    if exit_flag == False:
      child_directory(path, file_directory, 0)
