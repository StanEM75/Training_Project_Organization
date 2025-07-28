from src.utils.production import cars_by_day, production_cost, is_target_reached

def test_cars_by_day():
    assert cars_by_day(100, 10) == 10
    assert cars_by_day(200, 2) == 100

def test_production_cost():
    assert production_cost(100, 10) == 1000
    assert production_cost(200, 2) == 400

def test_is_target_reached():
    assert is_target_reached(100, 10) == "The target has been overcome."
    assert is_target_reached(100, 1000) == "The target has not been reached."

def test_divide_by_zero():
    try:
        cars_by_day(100,0)
    except ValueError as e:
        assert str(e) == "Division by 0"
