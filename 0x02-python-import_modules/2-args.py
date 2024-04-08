#!/usr/bin/python3

if __name__ == "__main__":
    # import module
    import sys

    # define function
    arguments = sys.argv[1:]
    argc = len(arguments)

    if argc > 1:
        print("{} arguments:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, arguments[i]), end="\n")
    elif argc == 1:
        print("{} argument:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, arguments[i]))
    else:
        print("0 arguments.")
