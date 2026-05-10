import os 
cwd = os.getcwd()
print("Current Directory:",cwd)
files = os.listdir()
print("Files and Folders:",files)
folder="demo_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory Created:",folder)
else:
    print("Directory already existing",folder)