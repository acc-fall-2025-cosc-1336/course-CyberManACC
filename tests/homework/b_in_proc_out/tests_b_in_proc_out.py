import pathlib
import sys

# Make the "src" layout importable for tests
ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from homework.b_in_proc_out.output import multiply_numbers


def test_multiply_numbers():
    assert multiply_numbers(7, 7) == 49
    assert multiply_numbers(5, 5) == 25


