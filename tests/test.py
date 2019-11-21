"""Testing for pymath."""
import pymath
import unittest


class TestGeom(unittest.TestCase):
    def test_circ(self):
        self.assertEqual(pymath.geometry.circumference(5), 15.707963267948966)


def test_log():
    """Tests pymath.algebra.log."""
    assert pymath.algebra.log(4, 16) == 2, "Should be 2"
    assert pymath.algebra.log(5, 25) == 2, "Should be 0.5"
    assert pymath.algebra.log(3, 27) == 3, "Should be 3"


def test_quad():
    """Tests pymath.algebra.quad."""
    assert pymath.algebra.quad(
        1, 3, 2) == (-1.0, -2.0), "Should be (-1.0, -2.0)"
    assert pymath.algebra.quad(
        1, 3, -4) == (1.0, -4.0), "Should be (1.0, -4.0)"
    assert pymath.algebra.quad(
        2, 4, -6) == (4.0, -12.0), "Should be (4.0, -12.0)"
    assert pymath.algebra.quad(-1, -3, -5) == ((-1.5-1.6583123951777j), (-1.5-1.6583123951777j)
                                               ), "Should be ((-1.5-1.6583123951777j), (-1.5-1.6583123951777j))"


def test_pythag():
    assert pymath.geometry.pythag_theor(
        5, 3) == 5.830951894845301, "Should be 5.830951894845301"


if __name__ == "__main__":
    test_log()
    test_quad()
    test_pythag()
    unittest.main()
    print("Everything passed!")
