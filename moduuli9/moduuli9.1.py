class Car:
    def __init__(self, registration_num , max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0

car1 = Car ("ABC-123",142)
print(f" Auton rekisteri numero on :{car1.registration_num},\n Maksimi nopeus on :{car1.max_speed},\n Tän hetkinnen nopeus :{car1.current_speed},\n kuljettu matka : {car1.traveled_distance}")







