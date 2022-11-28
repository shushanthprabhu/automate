"""
    Code Snipet to clean up simulation files from Simulation folder

"""

# list_of_file.txt = ["log", "inf", "dat", "plot"]

# pyinstaller --hidden-import=pkg_resources.py2_warn --onefile SW_FileClean.py
import shutil
from os import remove, walk, chdir, listdir, rmdir

filename_to_delete = ["hard_coded_files.txt",
                      "hard_coded_files2.txt"]

try:
    f = open("list_of_files.txt", "r")
    list_of_file_ext = f.read()
    for item in list_of_file_ext:
        item.strip()
    # print(list_of_file_ext)

    print("SW File Clean Version 2. Last Updated on 28-11-2022")
    path = input("Enter Simulation folder to clean-")
    chdir(path)
    files_deleted = []
    files_deleted_counter = 0
    folders_deleted = []
    folders_deleted_counter = 0

    for root, dirs, files in walk(".", topdown=True):
        for file in files:
            # print("FILE is-", file)
            filename_split = file.split(".")
            try:
                if filename_split[1] in list_of_file_ext:
                    if root == ".":
                        file_location = path + "\\" + file
                    else:
                        file_location = path + "\\" + root + "\\" + file
                        # print(file_location)
                    try:
                        files_deleted_counter += 1
                        files_deleted.append(file_location)
                        remove(file_location)
                    except:
                        print("Could not delete the file", file_location)

                if file in filename_to_delete:
                    if root == ".":
                        file_location = path + "\\" + file
                    else:
                        file_location = path + "\\" + root + "\\" + file
                        # print(file_location)
                    try:
                        files_deleted_counter += 1
                        files_deleted.append(file_location)
                        remove(file_location)
                    except:
                        print("Could not delete the file", file_location)

            except:
                print("TOTAL FILES DELETED-", files_deleted_counter)
                print("LIST OF FILES DELETED-")
                for item in files_deleted:
                    print(item)
                # pass

    delete_folder = True
    while delete_folder:
        delete_folder = False
        for root, dirs, files in walk(".", topdown=True):
            for folder in dirs:
                if root == ".":
                    folder_location = path
                    # print(folder_location)
                else:
                    folder_location = path + "\\" + root + "\\" + folder
                    try:
                        folder_location = folder_location.replace("\\.\\", "\\")
                    except:
                        pass

                if len(listdir(folder_location)) == 0:
                    folders_deleted_counter += 1
                    folders_deleted.append(folder_location)
                    rmdir(folder_location)
                    delete_folder = True

                if folder[0] == '$':
                    # Deletes folder with $ in the first letter
                    if folder_location == path:
                        # base folder does not have the folder in it the path updated.
                        folder_2_delete = folder_location + folder
                    else:
                        folder_2_delete = folder_location
                    folders_deleted_counter += 1
                    folders_deleted.append(folder_2_delete)
                    try:
                        shutil.rmtree(folder_2_delete)
                    except:
                        pass
                        # STUPID IDEA BUT WORKS :)

    print("TOTAL FOLDERS DELETED-", folders_deleted_counter)
    print("LIST OF FOLDERS DELETED-")
    for item in folders_deleted:
        print(item)
    print("Done Cleaning")
    exit_character = input("press close to exit")

except FileNotFoundError:
    print("list_of_files.txt not found")
    exit_character = input("press close to exit")
