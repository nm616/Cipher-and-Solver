#!/usr/bin/env python3

import string
import os
import sys

def picker():
    num = 1
    files = []
    for file in os.listdir():
        if "encoded" in file:
            files.append(file)
        else:
            if files == [""]:
                sys.exit(2)
    for name in files:
        print(f"{num}: {name}")
        num += 1
    selection = input("Select a File to Decode: ")
    return str(files[int(selection) - 1])


def solver():
    file = picker()
    ext = file[7:]
    with open(file, "r") as t:
        text = t.read()
        key = input("Enter Key (num): ")
        key = key[::-1]
        for num in key:
            num = int(num) * -1
            letters = string.printable
            mask = letters[int(num):] + letters[:int(num)]
            code = str.maketrans(letters, mask)
            text = text.translate(code)
            with open("decoded_" + ext, "w+") as file:
                file.write(text)
    print(text)
    input("Press Enter to Finish: ")
solver()