# tests/test_geometry.py
from src.utils.geometry import calculate_area

def test_aire_cercle():
    assert round(calculate_area(1), 2) == 3.14