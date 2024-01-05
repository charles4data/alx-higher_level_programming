#!/usr/bin/python3

if __name__ == "__main__":
    # import module
    import sys

    # define function
    arguments = sys.argv[1:]
    argc = len(arguments)

    if argc > 0:
        print("{} arguments".format(argc))
        for i in range(argc):
            print("{}: {}".format(i, arguments[i]), end="\n")
    else:
        print("No Arguments provided")
