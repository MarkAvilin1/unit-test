from unittest import TestCase, main

from calculator.main import calc


class CalcTest(TestCase):
    def test_sum(self):
        self.assertEqual(calc('2 + 2'), 4)

    def test_minus(self):
        self.assertEqual(calc('3 - 1'), 2)

    def test_mult(self):
        self.assertEqual(calc('2 * 5'), 10)

    def test_div(self):
        self.assertEqual(calc('10 / 5'), 2)

    def test_div_type(self):
        self.assertEqual(type(calc('2 / 1')), float)

    def test_mult_type(self):
        self.assertEqual(type(calc('5 * 2')), int)

    def test_raiseError_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('1+2+3')
        self.assertEqual('The expiration should has tow numbers and one sign', e.exception.args[0])

    def test_raiseError(self):
        with self.assertRaises(ValueError) as e:
            calc('hi there')
        self.assertEqual('The expiration should has one of (+-*/)', e.exception.args[0])


if __name__ == '__main__':
    main()
