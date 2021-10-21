from dataclasses import dataclass
import math
from app.utils.compute import sum


@dataclass
class SumItem():
    x: int
    y: int
    result: int

def test_sum():
    tests = [
        SumItem(0, 0, 0),
        SumItem(-1, 1, 0),
        SumItem(1, 1, 2),
        SumItem(-1, -1, -2),
        SumItem(-1, -1, -2)
    ]
    for test in tests:
        assert sum(test.x, test.y) == test.result
