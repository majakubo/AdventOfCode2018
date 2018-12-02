from collections import Counter


def checksum(id_list):
    doubles, triples = 0, 0

    for id in id_list:
        letter_frequency = Counter(id)
        contains_double, contains_triple = False, False

        for letter in letter_frequency:
            if letter_frequency[letter] == 2 and not contains_double:
                doubles += 1
                contains_double = True
            elif letter_frequency[letter] == 3 and not contains_triple:
                triples += 1
                contains_triple = True

    return doubles * triples


def parse_file(id_list):
    parameters = list(id_list)
    parameters = [parameter[:-1] for parameter in parameters]
    return parameters

def differs(seq_one, seq_two):
    sequences = list(zip(seq_one, seq_two))
    diff = 0
    for l1, l2 in sequences:
        if l1 != l2:
            diff += 1

    return diff

def get_correct_id(id_list):
    for word_one in id_list:
        for word_two in id_list:
            if differs(word_one, word_two) == 1:
                words = list(zip(word_one, word_two))
                id = [letter_one for letter_one, letter_two in words if letter_one == letter_two] #
                return ''.join(id)


if __name__ == '__main__':
    print(checksum(parse_file(open('1input.txt', 'r'))))
    print(get_correct_id(parse_file(open('1input.txt', 'r'))))
