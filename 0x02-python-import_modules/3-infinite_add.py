#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    for arg in range (1, len(argv)):
        total += int(argv[arg])
    print("{}".format(total))
