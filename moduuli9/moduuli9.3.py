class Car:
    def __init__(self, registration_num , max_speed):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.traveled_distance = 0
    def accel(self, km_h):
        if self.current_speed + km_h > 0:
            if self.current_speed + km_h < self.max_speed:
                self.current_speed += km_h
            else:
                self.current_speed = self.max_speed
        else:
            self.current_speed = 0

    def kulje(self, hours):
        self.traveled_distance += self.current_speed * hours




car1 = Car ("ABC-123",142)
car1.accel(30)
car1.kulje(1.5)
print(f" Auton rekisteri numero on :{car1.registration_num},"
      f"\n Maksimi nopeus on :{car1.max_speed},\n Tän hetkinnen nopeus :{car1.current_speed},"
      f"\n kuljettu matka : {car1.traveled_distance:.0f}km/h")
