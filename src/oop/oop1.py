# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # Vehicle base class
    pass


class GroundVehicle(Vehicle):  # Ground Vehicle parent
    pass


class Car(GroundVehicle):  # Ground Vehicle
    pass


class Motorcycle(GroundVehicle):  # Ground Vehicle
    pass


class FlightVehicle(Vehicle):  # Flight Vehicle Parent
    pass


class Starship(FlightVehicle):  # Flight Vehicle
    pass


class Airplane(FlightVehicle):  # Flight Vehicle
    pass
