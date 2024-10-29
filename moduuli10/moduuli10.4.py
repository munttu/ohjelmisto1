'''This exercise continues the previous car race exercise from the last exercise set.
Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to
the corresponding properties in the class.
The class has the following methods:

hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
print_status, which prints out the current information of each car as a clear, formatted table.
race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.'''


import random as r
class Race:
    def __init__(self, name, kilometers, car_list):

    def hours_passed(self,):


class Car:
    def __init__(self, registration_num , max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0
    def accel(self, km_h):
        if self.current_speed + km_h > 0:
            self.current_speed= min(self.max_speed, self.current_speed + km_h)
        else:
            self.current_speed = 0

    def kulje(self, hours):
        self.traveled_distance += self.current_speed * hours

        wheee