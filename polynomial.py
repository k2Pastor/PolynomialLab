class Polynomial:

    def __init__(self, coefficients=None):
        self.coefficients = []
        if coefficients is None:
            raise TypeError("Coefficients cannot be 'None'!")
        elif isinstance(coefficients, (list, tuple)):
            if len(coefficients) == 0:
                raise ValueError("Coefficients cannot be empty!")
            else:
                if not all(map(lambda c: isinstance(c, int), coefficients)):
                    raise ValueError("Incorrect input: coefficients must be integers!")
                self.coefficients = list(map(lambda c: c, coefficients))
        elif isinstance(coefficients, int):
            self.coefficients.append(coefficients)
        elif isinstance(coefficients, Polynomial):
            self.coefficients = coefficients.coefficients.copy()
        else:
            raise \
                TypeError("Unacceptable type of the coefficients: it should be integer, list, tuple or Polynomial!")

    def __repr__(self):
        return "Polynomial({})".format(self.coefficients)

    def __str__(self):
        result = []
        reversed_coefficients = self.coefficients[::-1]
        for i, c in enumerate(reversed_coefficients):
            if c != 0:
                if i == 0:
                    result.append((str("{:+d}").format(c)))
                elif i == 1:
                    result.append(("-" if c < 0 else "+") + (str(abs(c)) if (abs(c) != 1) else "") + "x")
                else:
                    result.append(("-" if c < 0 else "+") + (str(abs(c)) if (abs(c) != 1) else "") + "x^" + str(i))
        if reversed_coefficients != [0]:
            if result[-1][0] == "+":
                result[-1] = result[-1].replace("+", "")
        else:
            return "0"
        return "".join(reversed(result))

    def __add__(self, other):
        addition_coefficients = []
        if isinstance(other, int):
            addition_coefficients = self.coefficients[:]
            addition_coefficients[-1] += other
        elif isinstance(other, Polynomial):
            long_polynomial, short_polynomial = (self, other) if len(self.coefficients) > len(other.coefficients) \
                else (other, self)
            addition_coefficients = long_polynomial.coefficients[:]
            for i in range(1, len(short_polynomial.coefficients) + 1):
                addition_coefficients[-i] += short_polynomial.coefficients[-i]
        else:
            raise TypeError("Unacceptable type of the operand!")
        return Polynomial(self.__remove_zeros(addition_coefficients))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            return self.__add__(-other)
        elif isinstance(other, Polynomial):
            negative_coefficients = list(map(lambda c: -c, other.coefficients))
            return self.__add__(Polynomial(negative_coefficients))
        else:
            raise TypeError("Unacceptable type of the operand!")

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Polynomial(other)
            return other.__sub__(self)
        elif isinstance(other, Polynomial):
            return other.__sub__(self)
        else:
            raise TypeError("Unacceptable type of the operand!")

    def __mul__(self, other):
        result_coefficients = []
        if isinstance(other, int):
            result_coefficients = list(map(lambda c: c * other, self.coefficients))
            return Polynomial(result_coefficients)
        elif isinstance(other, Polynomial):
            result_coefficients = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i, c1 in enumerate(self.coefficients):
                for j, c2 in enumerate(other.coefficients):
                    result_coefficients[i + j] += c1 * c2
            return Polynomial(result_coefficients)
        else:
            raise TypeError("Unacceptable type of the operand!")

    __rmul__ = __mul__

    def __eq__(self, other):
        if isinstance(other, int):
            other = Polynomial(other)
            return self.coefficients == other.coefficients
        elif isinstance(other, Polynomial):
            return self.__remove_zeros(self.coefficients) == other.__remove_zeros(other.coefficients)
        else:
            raise TypeError("Unacceptable type of the operand!")

    @staticmethod
    def __remove_zeros(coefficients):
        while coefficients[0] == 0 and len(coefficients) > 1:
            del coefficients[0]
        return coefficients
