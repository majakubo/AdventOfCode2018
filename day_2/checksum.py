from collections import Counter
import nltk


def checksum(id_list):
    doubles, triples = 0, 0

    for id in id_list:
        id = list(id)
        letter_frequency = dict(Counter(id))

        contains_double, contains_triple = False, False

        for letter in letter_frequency:
            if letter_frequency[letter] == 2 and not contains_double:
                doubles += 1
                contains_double = True
            elif letter_frequency[letter] == 3 and not contains_triple:
                triples += 1
                contains_triple = True

    return doubles * triples


def parse_file(input):
    parameters = list(input)
    parameters = [parameter[:-1] for parameter in parameters]
    return parameters


def get_correct_id(input):
    for word_one in input:
        for word_two in input:
            if nltk.edit_distance(word_one, word_two) == 1:
                words = list(zip(word_one, word_two))
                id = [letter_one for letter_one, letter_two in words if letter_one == letter_two] #
                print(''.join(id))


if __name__ == '__main__':
    print(checksum(parse_file(open('1input.txt', 'r'))))
    get_correct_id(parse_file(open('1input.txt', 'r')))
