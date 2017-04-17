#!/bin/bash

import requests
import re

charset = "abcdefghiklmnopqrstuwxyz"

def bacon(char):
    baconian = str(char.replace("a", "0")).replace("b", "1")
    index = int(baconian, 2)
    translate = charset[index:index+1]
    #print("{0} turns {1} [{2}]".format(char, baconian, translate))
    return translate

def main():
    link = "http://www.try2hack.nl/levels/level6.data"
    r = requests.get(link)
    data = r.content.decode()
    lines = data.split("\n")
    print(data)
    print("Received {0} lines of data.".format(len(lines)))

    pattern = "[ab]+"
    for line in lines:
        buffer = str()
        for each in re.findall(pattern, line):
            #print(each)
            buffer += bacon(each)
        if len(buffer) > 0:
            print("Decoded: {0}".format(buffer))

    return 0


if __name__ == "__main__":
    main()
