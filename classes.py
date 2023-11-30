class Rectangle():
    _counter = 0

    def __init__(self, length=5.5, width=3.25):
        self._length = length
        self._width = width
        Rectangle._counter += 1

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_counter(self):
        return Rectangle._counter

    def set_length(self, length):
        self._length = length

    def set_width(self, width):
        self._width = width

    def perimeter(self):
        return 2 * (self._length + self._width)

    def area(self):
        return self._length * self._width

    def equals(self, other):
        return self._length == other._length and self._width == other._width

    def to_string(self):
        return f"Length = {self._length} and Width = {self._width}"


class Parallelepiped(Rectangle):
    def __init__(self, length=2, width=1.75, height=3):
        super().__init__(length, width)
        self._height = height
        Rectangle._counter += 1

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def perimeter(self):
        return 2 * (self.get_length() + self.get_width()) * self._height

    def surface_area(self):
        return 2 * (self.get_length() * self.get_width() +
                    self.get_length() * self._height +
                    self.get_width() * self._height)

    def volume(self):
        return self.get_length() * self.get_width() * self._height

    def to_string(self):
        return f"Length = {self.get_length()}, Width = {self.get_width()}, Height = {self._height}"

    def equals(self, other):
        return (self.get_length() == other.get_length() and
                self.get_width() == other.get_width() and
                self._height == other._height)
