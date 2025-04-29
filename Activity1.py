class Vehical:
    def __init__(self,name,max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class bus(Vehical):
    pass
school_bus= bus("Volvo" , 180 , 12)
print("Bus name:" , school_bus.name , "Maximum speed " , school_bus.max_speed , "Mileage:" , school_bus.mileage)