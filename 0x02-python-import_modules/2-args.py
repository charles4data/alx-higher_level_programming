#!/usr/bin/python3

if __name__ == "__main__":
    # import module
    import sys

    # define function
    def cmd_args(argv):
        num_args = len(argv)

        if num_args > 0:
            print("{} arguments".format(num_args))
            for i in range(num_args):
                print("{}: {}".format(i, argv[i]), end="\n")
        else:
            print("No Arguments provided")

    if __name__ == "__main__":
        cmd_args(sys.argv[1:])