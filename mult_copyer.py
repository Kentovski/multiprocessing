# /usr/bin/python3

# MELNIKOV ILYA


from multiprocessing import Pool
from os import listdir
from functools import partial
from shutil import copy
import json


def copy_files(dst, file):
    copy(file, dst)


def main():
    if input("Do you want to change max number of processes? Y / N") == "Y":
        max_processes = int(input("Enter max number of processes"))
    else:
        with open(config.json) as f:
            max_processes = json.load(f)['max_processes']

    src = input("Enter the source path: ")
    dst = input("Enter the destination path: ")

    pool = Pool(max_processes)
    pool.map(partial(copy_files, dst), listdir(path=src))
    pool.close()
    pool.join()
    print("Copied")


if __name__ == "__main__":
    main()
