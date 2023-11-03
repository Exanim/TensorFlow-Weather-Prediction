import random


def chaotic_random():
    if random.random() > 0.5:
        return 0.0
    exp = random.expovariate(0.45) * 2
    if exp < 25:
        return round(exp, 1)
    else:
        return 0.0


def main():
    for i in range(100):
        print(chaotic_random())


if __name__ == '__main__':
    main()
