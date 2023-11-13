import math


def logarithmic_warming_rate(year, temperature):
    if year > 1981:
        log_warming_rate_per_decade = 0.18 - (0.18 / math.log(year, 1000))
        current_decade = (year-1981) / 10
        calculated_temperature = temperature + (current_decade * log_warming_rate_per_decade)
        return math.trunc(calculated_temperature * 10)/10  # Round the result
    else:
        return math.trunc(temperature * 10)/10


def main():
    for year in range(1990, 3000):
        print(year, ":", logarithmic_warming_rate(year, 10.0))
        print(round(10 - logarithmic_warming_rate(year, 10.0), 1))


if __name__ == '__main__':
    main()