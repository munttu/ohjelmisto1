class Talo:
    def __init__(self, top_floor, bottom_floor, elev_amount):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elev_amount = [Hissi(bottom_floor, top_floor ) for _ in range(elev_amount + 1)]


    def elev_drive(self, elev_num, target_floor ):
        if 0 <= elev_num <  len(self.elev_amount):
            print(f"hissiä {elev_num} ajetaan kerrokseen {target_floor}")
            self.elev_amount[elev_num].move(target_floor)
        else:
            print("virheellinen hissi numero")
    def fire_alarm(self):
        print("koska palohälytin soi kaikki hissit menee 1")
        for a , hissi in  enumerate(self.elev_amount):
            print(f"ajetaan hissi {a} ensimmäiseen kerrokseen ")
            hissi.move(1)

class Hissi:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.default_floor = self.bottom

    def move(self, wanted_floor):
        if wanted_floor > self.top or wanted_floor < self.bottom:
            print("kerrosta ei ole")
            return

        while self.default_floor != wanted_floor:
            if self.default_floor < wanted_floor:
                print(f"Tän hetkinen kerros on : {self.default_floor}")
                Hissi.elev_up(self, 1)
            elif self.default_floor > wanted_floor:
                print(f"Tän hetkinen kerros on : {self.default_floor}")
                Hissi.elev_down(self, 1)

        else:
            print(f"Pääsit kerrokseen : {self.default_floor}")

    def elev_down(self, wanted_floor):
        self.default_floor -= wanted_floor

    def elev_up(self, wanted_floor):
        self.default_floor += wanted_floor

talo = Talo(10, 1, 3)
talo.elev_drive(1, 5)
talo.elev_drive(2, 8)
talo.fire_alarm()
talo.elev_drive(2,6)
talo.elev_drive(4,11)

talo.elev_drive(3,11)



