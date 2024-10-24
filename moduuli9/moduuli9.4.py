import random as r


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

car = []
total_hours = 0
for i in range(10):
    car.append(Car("ABC-"+str(i+1), r.randint(100,200)))
game = 1
total_hours = 0
while game != 2:
    total_hours += 1
    for c in car:
        c.accel(r.randint(-10, 15))
        c.kulje(1)
        if c.traveled_distance > 10000:
            game = 2
            break

print(f"{'Registration':<13} {'Max Speed (km/h)':<19} {'Current Speed (km/h)':<21} {'Traveled Distance (km)':<21}")
for r in car:
    print(f"{r.registration_num:<13}{r.max_speed:<19}{r.current_speed:<21}{r.traveled_distance:<21.0f}")
