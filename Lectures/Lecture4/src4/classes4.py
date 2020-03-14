class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep track of id number.
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
        self.passengers = []

        # Details about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration


    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        #print(Flight.id)

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")
        print("---------")

    def delay(self, amount):
        self.duration += amount

#allows people to add passengers + tag attributes by typing "add_passenger(name)"
    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

#creates a class, name passenger(which takes a variable), and added into a variable
class Passenger:

    def __init__(self, name):
        self.name = name



def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f2 = Flight("Singapore", "Melbourne", 100)

    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")
    toby = Passenger(name="Toby")

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)
    f2.add_passenger(toby)

    f1.print_info()
    f2.print_info()

    #print(alice.p)
    print(f"Toby's secret flight ID: {toby.flight_id}")


    #x=hasattr(alice,"flight_id")
    #print(x)

if __name__ == "__main__":
    main()
