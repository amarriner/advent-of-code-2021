import sys


def main():

    with open("../input.txt") as f:
        input = f.read().split("\n")

    gamma = []
    epsilon = []
    for i in range(0, 12):

        ones = 0
        zeroes = 0
        for line in input:

            if line == "":
                continue

            if int(line[i]) == 0:
                zeroes += 1
            if int(line[i]) == 1:
                ones += 1

        if ones > zeroes:
            gamma.append("1")
            epsilon.append("0")
        else:
            gamma.append("0")
            epsilon.append("1")

    binary_gamma = "".join(gamma)
    decimal_gamma = int(binary_gamma, 2)
    print(f"Binary Gamma   : {binary_gamma}")
    print(f"Decimal Gamma  : {decimal_gamma}")

    binary_epsilon = "".join(epsilon)
    decimal_epsilon = int(binary_epsilon, 2)
    print(f"Binary Epsilon : {binary_epsilon}")
    print(f"Decimal Epsilon: {decimal_epsilon}")

    print(f"Consumption    : {decimal_gamma * decimal_epsilon}")


if __name__ == "__main__":
    sys.exit(main())
