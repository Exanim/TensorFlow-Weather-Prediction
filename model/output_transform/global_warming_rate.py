import math


def logarithmic_warming_rate(year, temperature):
    if year > 1981:
        log_warming_rate_per_decade = 0.18 - (0.18 / math.log(year, 1000))
        current_decade = (year-1981) / 10
        return round(temperature + (current_decade * log_warming_rate_per_decade), 1)
    else:
        return round(temperature, 1)


def main():
    for year in range(1990, 10000):
        print(year, ":", logarithmic_warming_rate(year, 10))
        print(10 - logarithmic_warming_rate(year, 10))


if __name__ == '__main__':
    main()