#! /usr/bin/env python
# coding: utf-8


import os


def walk_dir(file_path):
    count = 0
    for root, dirs, files in os.walk(file_path):
        # print(root)
        for d in dirs:
            if os.path.isdir(d):
                walk_dir(d)
        for file in files:
            count = count + 1
            print("FileName: " + file)
    if count == 0:
        print(file_path)


if __name__ == '__main__':
    dir_path = 'd:/book'
    walk_dir(dir_path)