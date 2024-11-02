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

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours
class Electric_car(Car):
    def __init__(self, registration_num ,max_speed, battery_capacity):
        super().__init__(registration_num, max_speed)
        self.battery_capacity = battery_capacity
        

class Gas_car(Car):
    def __init__(self, registration_num , max_speed , tank_volume):
       super().__init__(registration_num ,max_speed)
       self.tank_volume = tank_volume
       


        
class Race:
    def __init__(self, name, distance_km, car_list):
        self.name = name
        self.distance_km = distance_km
        self.car_list = car_list 
    def hours_passed(self):
        for c in self.car_list:
            accel1 =r.randint(-10,15)
            c.accel(accel1)
            c.drive(1)
    def status_print(self,hour):
        print(hour)
        self.car_list.sort(key=lambda c: c.traveled_distance, reverse=True)
        print(f"{'Registration':<13} {'Max Speed (km/h)':<19} {'Current Speed (km/h)':<21} {'Traveled Distance (km)':<21}")
        for r in self.car_list:
            print(f"{r.registration_num:<13}{r.max_speed:<19}{r.current_speed:<21}{r.traveled_distance:<21.0f}")
    
    def race_finito(self):
        for c in self.car_list:
            if c.traveled_distance >= self.distance_km:
                return True
        return False


cars = []
cars.append(Electric_car("ABC-15" , 180, 52.5))  
cars.append(Gas_car("ACD-123", 165 , 32.3))

total_hours = 0
race_fini = False   
meow = Race("Grand_Demolition_Derby", 8000, cars)
while race_fini == False:
    total_hours += 1
    meow.hours_passed()
    race_fini = meow.race_finito()
    if total_hours % 3==0:
        meow.status_print(total_hours)

print(f"The race is over results:")
meow.status_print(total_hours)