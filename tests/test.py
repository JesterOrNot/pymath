"""Testing for pymath."""
from pymath.algebra import log as log


def test_log():
    """Tests pymath.algebra.log."""
    assert log(4, 16) == 2, "Should be 2"


if __name__ == "__main__":
    test_log()
    print("Everything passed!")
