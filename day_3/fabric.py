def get_input(file):
    parameters = list(file)
    parameters = [parameter[:-1] for parameter in parameters]
    return parameters


class Square():
    def __init__(self, _id):
        self.id = _id
        # parse id to parameters
        claim = _id.split(' @ ')
        claim = claim[1:]
        claim = claim[0].split(': ')
        left, top = claim[0].split(',')
        width, height = claim[1].split('x')
        parameters = (left, top, width, height)

        # convert every element to int
        parameters = tuple(map(lambda x: int(x), parameters))

        self.left, self.top, self.width, self.height = parameters

    def check_interruption(self, fabric):
        for i in range(len(fabric)):
            for j in range(len(fabric)):
                if fabric[i][j] != 1:
                    return True
        return False


def parse_input(claims):
    parsed = []
    for claim in claims:
        claim = claim.split(' @ ')
        claim = claim[1:]
        claim = claim[0].split(': ')
        left, top = claim[0].split(',')
        width, height = claim[1].split('x')
        parameters = (left, top, width, height)
        parameters = tuple(map(lambda x: int(x), parameters))
        parsed.append(parameters)
    return parsed


def fill_squares(claims):
    size = 1000
    fabric = [[0 for i in range(size)] for j in range(size)]

    for claim in claims:
        left, top, width, height = claim
        for i in range(height):
            for j in range(width):
                fabric[top + i][left + j] += 1
    for row in fabric:
        print(row)
    return fabric


def count_collisions(fabric):
    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric)):
            if fabric[i][j] > 1:
                counter += 1

    return counter


def find_valid_square(fabric):
    fields = []
    for i in range(len(fabric)):
        for j in range(len(fabric)):
            if fabric[i][j] == 1:
                fields.append((i, j))
    # print_valid_square(fields)
    return fields


def print_valid_square(fields):
    size = 1000
    fabric = [[0 for i in range(size)] for j in range(size)]
    for field in fields:
        fabric[field[0]][field[1]] = '#'

    for row in fabric:
        print(row)


def find_corners_of_valid_square(fields):
    left_upper_corner = [1000000, 1000000]
    right_lower_corner = [0, 0]
    for cord in fields:
        x, y = cord
        if x < left_upper_corner[1]:
            left_upper_corner[1] = x
        if y < left_upper_corner[0]:
            left_upper_corner[0] = y

        if x > right_lower_corner[1]:
            right_lower_corner[1] = x
        if y > right_lower_corner[0]:
            right_lower_corner[0] = y

    return left_upper_corner, right_lower_corner


def find_id_of_square(ids, left_upper_corner, right_lower_corner):
    left = left_upper_corner[1]
    top = left_upper_corner[0]
    width = right_lower_corner[1] - left_upper_corner[1]
    height = right_lower_corner[0] - left_upper_corner[0]
    valid_id = " @ {},{}: {}x{}".format(left, top, width, height)
    for id_ in ids:
        if valid_id in id_:
            return id_


if __name__ == '__main__':
    print(count_collisions(fill_squares(parse_input(get_input(open('1input.txt'))))))
    inp = get_input(open('1input.txt'))
    parsed = parse_input(inp)
    fabric = fill_squares(parsed)
    valid_square = find_valid_square(fabric)
    left_upper_corner, right_lower_corner = find_corners_of_valid_square(valid_square)
    print(find_id_of_square(inp, left_upper_corner, right_lower_corner))
