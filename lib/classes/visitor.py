import ipdb

class Visitor:

    def __init__(self, name="Visitor"):
        self.name = name
        print(name)

    def get_name(self): 
        return self._name

    def set_name(self, name):
        if name is str:
            self._name = name
        else: 
            raise Exception("name does not fit criteria")

    name = property(get_name , set_name)

    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass

visitor_one = Visitor("Bob")
