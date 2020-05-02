import sys


def two_fer(name="you"):
    return "One for {}, one for me.".format(name)


if __name__ == "__main__":
    two_fer(sys.argv[1])
