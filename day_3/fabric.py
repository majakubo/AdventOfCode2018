class Rectangle:
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
        for i in range(self.height):
            for j in range(self.width):
                if fabric[self.top + i][self.left + j] != self.id:
                    return False

        return True

    def draw_yourself(self, fabric):
        for i in range(self.height):
            for j in range(self.width):
                if fabric[self.top + i][self.left + j] == 0:
                    fabric[self.top + i][self.left + j] = self.id
                else:
                    fabric[self.top + i][self.left + j] = 'x'


def get_input(file):
    parameters = list(file)
    parameters = [parameter[:-1] for parameter in parameters]
    return parameters


def create_rectangles(claims):
    rectangles = []
    for claim in claims:
        rectangle = Rectangle(claim)
        rectangles.append(rectangle)

    return rectangles


def draw_rectangles(rectangles):
    size = 1000
    fabric = [[0 for i in range(size)] for j in range(size)]

    for rectangle in rectangles:
        rectangle.draw_yourself(fabric)

    return fabric


def count_collisions(fabric):
    counter = 0
    for i in range(len(fabric)):
        for j in range(len(fabric)):
            if fabric[i][j] == 'x':
                counter += 1

    return counter


def find_valid_rectangle(rectangles, fabric):
    ids = []
    for rectangle in rectangles:
        if rectangle.check_interruption(fabric):
            ids.append(rectangle.id)

    return ids


if __name__ == '__main__':
    claims = get_input(open('1input.txt'))
    rectangles = create_rectangles(claims)
    fabric = draw_rectangles(rectangles)
    print(count_collisions(fabric))

    value_rectangles = find_valid_rectangle(rectangles, fabric)
    for rectangle in value_rectangles:
        print(rectangle)

