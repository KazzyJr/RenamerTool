"""
Python 3.x code to rename all the files inside all the subsequent directories as the parent directory name
Version 1.0
"""

import os


def main():
    test = True
    while test:
        input_opt = input("One folder (1) or the entire tree of one folder (2)? ")
        if input_opt == "1":
            input_dir = input("Base folder: ")
            if_single(input_dir)
            print("Job is done! Enjoy!")
            test = False
        elif input_opt == "2":
            input_dir = input("Base folder: ")
            if_dir(input_dir)
            print("Job is done! Enjoy!")
            test = False
        else:
            print("Please insert a valid option!\n", )
            test = True


def if_dir(input_dir):
    source = input_dir
    for filename in enumerate(os.listdir(source)):
        if os.path.isdir(os.path.join(source, filename[1])):  # This tests if we have a file or a folder
            path = os.path.join(source, filename[1])
            if_dir(path)
        else:
            if_file(filename, source)


def if_single(input_dir):
    source = input_dir
    for filename in enumerate(os.listdir(source)):
        if_file(filename, source)


def if_file(filename, source):
    counter = 0
    ext = filename[1].split(".")[-1]  # File extension
    a = 0
    while a == 0:  # We try to rename until we find an open slot
        try:
            dst = str(source.split("\\")[-1]) + "_" + str(counter) + "." + ext.lower()
            src = os.path.join(source, filename[1])
            dst = os.path.join(source, dst)
            os.rename(src, dst)
            counter += 1
            a = 1
        except FileExistsError:
            a = 0
            counter += 1


if __name__ == '__main__':
    prompt = "y"
    while prompt == "y":
        main()
        prompt = input("Do you want to rename another base directory? y/n ")
