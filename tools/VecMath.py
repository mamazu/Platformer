class Vec2D:
    def __init__(self, x=0, y=0, vec=None):
        """
        Constructor of the vector
        :param x: x value
        :type x: float
        :param y: y value
        :type y: float
        """
        self.x = x
        self.y = y
        if vec is None:
            return
        self.set(vec)

    def __add__(self, other):
        """
        Adds two vectors component-wise and adds a scale and a vector
        :param other: Second part of the sum
        :type other: int, float, Vec2D
        :return: Returns the sum
        :rtype: Vec2D
        """
        if isinstance(other, Vec2D):
            return Vec2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vec2D(self.x + other, self.y + other)

    def __sub__(self, other):
        """
        Subtracts a vector by.
        :param other: Other must have specified a __neg__ method
        :type other: int, float, Vec2D
        :rtype: Vec2D
        """
        return self + (-other)

    def __neg__(self):
        """
        Returns the negative value of the vector
        :rtype: Vec2D
        """
        return Vec2D(-self.x, -self.y)

    def __mul__(self, other):
        """
        Multiplies an int with a vector with a number or a vector.
        If the parameter other is a number it, scalar multiplication will be applied.
        If the parameter is a vector the components will be multiplied one by one.
        :type other: int, float, Vec2D
        :rtype: Vec2D
        """
        if Vec2D.is_vec(other):
            return Vec2D(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vec2D(self.x * other, self.y * other)

    def __div__(self, other):
        """
        Returns the division
        :type other: float
        :return: Vector
        :rtype: Vec2D
        """
        if other == 0:
            return None
        if isinstance(other, int) or isinstance(other, float):
            return Vec2D(self.x / other, self.y / other)

    def __eq__(self, other):
        """
        Checks if two vectors are equal
        :param other:
        :type other: Vec2D
        :return:
            True if equal, false otherwise
        :rtype: bool
        """
        if not Vec2D.is_vec(other):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Checks if two vectors are unequal
        :param other:
        :type other: Vec2D
        :return:
            False if equal, true otherwise
        :rtype: bool
        """
        return not (self == other)

    def __lt__(self, other):
        if Vec2D.is_vec(other):
            return self.x < other.x and self.y < other.y
        if isinstance(other, int) or isinstance(other, float):
            return self.x < other and self.y < other

    def __gt__(self, other):
        if Vec2D.is_vec(other):
            return self.x > other.x and self.y > other.y
        if isinstance(other, int) or isinstance(other, float):
            return self.x > other and self.y > other

    def __len__(self):
        return 2

    def get_tuple(self):
        """
        Returns the tuple of the vector
        :rtype: tuple
        """
        int_version = self.get_int()
        return int_version.x, int_version.y

    def get_int(self):
        """
        Returns the integer version of the vector.
        :rtype: Vec2D
        """
        return Vec2D(int(self.x), int(self.y))

    def get_length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def set(self, value):
        """
        Sets the value of the vector based on a tuple
        :param value:
        :type value: tuple or Vec2D
        :return: The new vector
        :rtype: Vec2D
        """
        if Vec2D.is_vec(value):
            self.x = value.x
            self.y = value.y
        elif len(value) == 2:
            print(value)
            self.x, self.y = value
        else:
            self.x, self.y = (0, 0)
        return self

    @staticmethod
    def is_vec(vec):
        """
        Checks if the parameter is a vector
        :param vec:
        :type vec: Vec2D
        :return: True if it is a vector, false otherwise
        :rtype: bool
        """
        return isinstance(vec, Vec2D) and vec is not None

    def __str__(self):
        """
        Returns the string representation of the vector
        :rtype: str
        """
        return "Vec2(%f|%f)" % (self.x, self.y)

    def __repr__(self):
        """
        Returns the string representation of the vector
        :rtype: str
        """
        return str(self)


class Pane:
    def __init__(self, pos=None, size=None):
        """
        Constructor of the pane object
        :param pos: Position of the pane
        :type pos: Vec2D
        :param size: Size of the pane
        :type size: Vec2D
        """
        self.pos = pos if Vec2D.is_vec(pos) else Vec2D(0, 0)
        self.size = size if Vec2D.is_vec(size) else Vec2D(0, 0)

    def set(self, value):
        """
        Sets the values of a pane based on a rectangle
        :param value:
        :type value: pygame.Rect
        :return: Returns the pane
        :rtype: Pane
        """
        from pygame.rect import Rect
        if isinstance(value, Rect):
            self.pos = Vec2D(value.left, value.top)
            self.size = Vec2D(value.width, value.height)
        return self

    def get_rect(self):
        """
        Gets the rectangle object based on the pane
        :return:
        :rtype: pygame.Rect
        """
        from pygame import Rect
        pos = self.pos.get_int()
        size = self.size.get_int()
        return Rect(pos.x, pos.y, size.x, size.y)

    def __add__(self, other):
        """
        Adds two panes together if the other one is not a pane or a tuple the
        :param other: Pane to be added
        :type other: tuple or Pane
        :return: The new pane
        :
        """
        result = Pane()
        if len(other) == 4:
            result.pos = self.pos + Vec2D(other[0], other[1])
            result.size = self.size + Vec2D(other[2], other[3])
        elif isinstance(other, Pane):
            result.pos = self.pos + other.pos
            result.size = self.size + other.size
        return result

    def __mul__(self, other):
        """
        Multiplies the size of the pane by a factor
        :param other: factor
        :type other: int or float
        :return: The new pane
        :rtype: Pane
        """
        if isinstance(other, int) or isinstance(other, float):
            return self.size * other

    def __str__(self):
        """
        Returns the string version of the pane
        :return:
        :rtype: str
        """
        return "Pos: %s; Size: %s" % (self.pos, self.size)

    def __iadd__(self, other):
        return other
