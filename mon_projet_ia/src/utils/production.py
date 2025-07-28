# Now we practice by creating functions and tests for a car manufacturer 

# Create a function to calculate the number of cars produced everyday
def cars_by_day(number_of_cars : float, number_of_days : float) -> float:
    if number_of_days == 0:
        raise ValueError("Division by 0")
    return number_of_cars / number_of_days

# Create a function to calculate the total production cost of cars
def production_cost(number_of_cars : float, cost_of_a_car : float) -> float:
    if cost_of_a_car == 0:
        raise ValueError("Division by 0")
    return number_of_cars * cost_of_a_car

# Create a function to check if the target has been reached for the past month
def is_target_reached(number_of_cars : float, target_number_of_cars : float) -> str:
    if number_of_cars < target_number_of_cars:
        return "The target has not been reached."
    elif number_of_cars == target_number_of_cars:
        return "The target has been reached."
    elif number_of_cars > target_number_of_cars:
        return "The target has been overcome."
    else: 
        return "We can't handle this situation, sorry."


