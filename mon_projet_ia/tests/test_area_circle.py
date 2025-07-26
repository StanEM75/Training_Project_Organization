# tests/test_geometry.py
from src.utils.geometry import aire_cercle

def test_aire_cercle():
    assert round(aire_cercle(1), 2) == 3.14