class Hissi:
    def __init__(self,bottom , top):
        self.bottom = bottom
        self.top = top
        self.default_floor = self.bottom

    def move(self, wanted_floor):
        if wanted_floor > self.top or wanted_floor < self.default_floor:
            print ("kerrosta ei ole")
            return

        while self.default_floor != wanted_floor:
            if self.default_floor < wanted_floor:
                print(f"Tän hetkinen kerros on : {self.default_floor}")
                Hissi.elev_up(self,1)
            elif self.default_floor > wanted_floor:
                print(f"Tän hetkinen kerros on : {self.default_floor}")
                Hissi.elev_down(self,1)

        else:
             print(f"Pääsit kerrokseen : {self.default_floor}")
    def elev_down(self, wanted_floor):
        self.default_floor -= wanted_floor
    def elev_up(self, wanted_floor):
        self.default_floor += wanted_floor

kerrostalo = Hissi(1,15)
kerrostalo.move(4)
kerrostalo.move(14)