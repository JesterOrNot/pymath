"""Testing for pymath."""
from pymath.algebra import log as log
from pymath.algebra import quad as quad
from pymath.geometry import circumference as circumference
from pymath.geometry import pythag_theor
import unittest


class TestGeom(unittest.TestCase):
    def test_circ(self):
        self.assertEqual(circumference(5), 15.707963267948966)


def test_log():
    """Tests pymath.algebra.log."""
    assert log(4, 16) == 2, "Should be 2"
    assert log(5, 25) == 2, "Should be 0.5"
    assert log(3, 27) == 3, "Should be 3"


def test_quad():
    """Tests pymath.algebra.quad."""
    assert quad(1, 3, 2) == (-1.0, -2.0), "Should be (-1.0, -2.0)"
    assert quad(1, 3, -4) == (1.0, -4.0), "Should be (1.0, -4.0)"
    assert quad(2, 4, -6) == (4.0, -12.0), "Should be (4.0, -12.0)"
    assert quad(-1, -3, -5) == ((-1.5-1.6583123951777j), (-1.5-1.6583123951777j)
                                ), "Should be ((-1.5-1.6583123951777j), (-1.5-1.6583123951777j))"


def test_pythag():
    assert pythag_theor(
        5, 3) == 5.830951894845301, "Should be 5.830951894845301"


if __name__ == "__main__":
    test_log()
    test_quad()
    test_pythag()
    unittest.main()
    print("Everything passed!")
