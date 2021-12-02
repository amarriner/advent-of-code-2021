import sys


def main():

    with open("../input.txt") as f:
        input = f.read().split("\n")

    horizontal = 0
    depth = 0
    aim = 0
    for line in input:

        if len(line.split(" ")) < 2:
            print(f"Error processing line {line}")
            continue

        command = line.split(" ")[0]
        x = int(line.split(" ")[1])

        if command == "forward":
            horizontal += x
            depth += (aim * x)
        elif command == "down":
            aim += x
        elif command == "up":
            aim -= x

    print(f"Final horizontal: {horizontal}")
    print(f"Final depth     : {depth}")
    print(f"Final aim       : {aim}")
    print(f"Product         : {horizontal * depth}")


if __name__ == "__main__":
    sys.exit(main())
