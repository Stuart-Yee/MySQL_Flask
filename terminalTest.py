import sys
def term_test(*args):
    for x in args:
        print(x)

if __name__ == "__main__":
    term_test(sys.argv)