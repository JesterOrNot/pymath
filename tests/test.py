"""Testing for pymath."""
from pymath.algebra import log as log


def test_log():
    """Tests pymath.algebra.log."""
    assert log(4, 16) == 2, "Should be 2"
    assert log(5, 25) == 2, "Should be 0.5"
    assert log(3, 27) == 3, "Should be 3"


if __name__ == "__main__":
    test_log()
    print("Everything passed!")
