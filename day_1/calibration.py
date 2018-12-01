from itertools import cycle


def calculate_frequency(input):
    parameters = parse_file(input)
    frequency = 0
    for parameter in parameters:
        frequency += parameter
    return frequency


def parse_file(input):
    parameters = list(input)
    parameters = [int(parameter[:-1]) for parameter in parameters]
    return parameters


def find_loop(input):
    parameters = parse_file(input)
    parameters = cycle(parameters)
    frequencies = dict()
    frequency = 0
    for parameter in parameters:
        if frequency in frequencies:
            return frequency
        else:
            frequencies[frequency] = 1
        frequency += parameter
