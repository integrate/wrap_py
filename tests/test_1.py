from wrap_engine import math_utils

def test_circle_calcs():
    dx, dy = math_utils.get_point_on_circle([100, 100], [100, 50], 90)
    assert (-50, 50) == (round(dx), round(dy))