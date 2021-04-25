import unittest
from polynomial import Polynomial


class MyTestCase(unittest.TestCase):
    a = Polynomial([1, 4, 3])
    b = Polynomial([-3, 0])
    c = 21

    def test_init(self):
        with self.assertRaises(ValueError):
            Polynomial([])
        with self.assertRaises(TypeError):
            Polynomial()
        with self.assertRaises(TypeError):
            Polynomial("String arguments")
        self.assertEqual(Polynomial(12).coefficients, [12])
        self.assertEqual(Polynomial((12, 21)).coefficients, [12, 21])
        self.assertEqual(Polynomial([12, 21]).coefficients, [12, 21])

    def test_add(self):
        with self.assertRaises(TypeError):
            self.a + "21"
        self.assertEqual((self.a + self.b).coefficients, [1, 1, 3])
        self.assertEqual((self.b + self.a).coefficients, [1, 1, 3])
        self.assertEqual((self.a + self.c).coefficients, [1, 4, 24])
        self.assertEqual((self.c + self.a).coefficients, [1, 4, 24])

    def test_sub(self):
        with self.assertRaises(TypeError):
            self.a - "21"
        self.assertEqual((self.a - self.b).coefficients, [1, 7, 3])
        self.assertEqual((self.b - self.a).coefficients, [-1, -7, -3])
        self.assertEqual((self.a - self.c).coefficients, [1, 4, -18])
        self.assertEqual((self.c - self.a).coefficients, [-1, -4, 18])

    def test_mul(self):
        with self.assertRaises(TypeError):
            self.a * "21"
        self.assertEqual((self.a * self.b).coefficients, [-3, -12, -9, 0])
        self.assertEqual((self.b * self.a).coefficients, [-3, -12, -9, 0])
        self.assertEqual((self.a * self.c).coefficients, [21, 84, 63])
        self.assertEqual((self.c * self.a).coefficients, [21, 84, 63])

    def test_str(self):
        self.assertEqual(str(self.a), "x^2+4x+3")
        self.assertEqual(str(self.b), "-3x")
        self.assertEqual(str(self.c), "21")

    def test_eq(self):
        self.assertTrue(self.a == self.a)
        self.assertTrue(self.c == Polynomial(21))
        self.assertTrue(self.b == Polynomial([-3, 0]))
        self.assertTrue(self.a == Polynomial((1, 4, 3)))
        self.assertFalse(self.a == self.c)
        self.assertFalse(self.a == self.b)

    def test_repr(self):
        self.assertEqual(repr(self.a), "Polynomial([1, 4, 3])")


if __name__ == '__main__':
    unittest.main()
