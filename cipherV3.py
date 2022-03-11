#!/usr/bin/env python3
import string
import os
import sys


def picker():
    num = 1
    files = []
    for file in os.listdir():
        if file.endswith(".txt"):
            if not "encoded" in file and not "decoded" in file:
                files.append(file)
            else:
                if files == [""]:
                    sys.exit(2)
    for name in files:
        print(f"{num}: {name}")
        num += 1
    selection = input("Select a File to Encode: ")
    return str(files[int(selection) - 1])


def cipher():
    txt = picker()
    with open(txt, "r", encoding="utf8") as filename:
        text = filename.read()
        key = input("Enter Key For " + txt + " :")
        for num in key:
            letters = string.printable
            mask = letters[int(num):] + letters[:int(num)]
            code = str.maketrans(letters, mask)
            text = text.translate(code)
        with open("encoded_" + txt, "w+") as file:
            file.write(text)
        # print(text)
    input("Press Enter to Finish: ")


cipher()
