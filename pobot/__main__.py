import pobot
import sys


def main():
    if len(sys.argv) < 3:
        print("You need to provide at least two words!")
    else:
        words = sys.argv[1:]
    print(pobot.run(words))


if __name__ == "__main__":
    main()
