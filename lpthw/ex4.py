# Quantity of cars
cars = 100
# Space size in cars
space_in_a_car = 4.0
# Quantity of drivers
drivers = 30
# Quantity of passengers
passengers = 90
# Quantity of cars left without drivers
cars_not_driven = cars - drivers
# Quantity of cars with drivers
cars_driven = drivers
# Space available from all cars
carpool_capacity = cars_driven * space_in_a_car
# Divides all passangers by amount of cars driven
# and gives you average amount of passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
