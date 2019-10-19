"""Testing for pymath."""
from pymath.algebra import log as log


def test_log():
    """Tests pymath.algebra.log."""
    assert log(3, 77) == 0.25291471002384025, "Should be 0.25291471002384025"


if __name__ == "__main__":
    test_log()
    print("Everything passed!")
