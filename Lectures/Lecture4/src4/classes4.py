class Flight:

    counter = 1

    #(Olaf:"this is a function")
    def __init__(self, origin, destination, duration):

        # Keep track of id number.
            #(Olaf:"equating id to a counter that +1 when a new object is created") - not required as argument within this class of objects
        self.id = Flight.counter
        Flight.counter += 1

        # Keep track of passengers.
            #(Olaf "equating a empty list when a new object is created) - not required as argument within this class of objects
        self.passengers = []



        # Details about flight.
            #(Olaf:"attributes of this class of objects require)
        self.origin = origin
        self.destination = destination
        self.duration = duration

    #(Olaf:"this is a function, that prints attributes stored in an object when called")
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        #print(Flight.id)

        print()
        print("Passengers:")
        #(Olaf:"also part of the function, this line just prints more infomation and loops over the list, remember self.passengers = [], per the line 13 - 18)
        for passenger in self.passengers:
            print(f"{passenger.name}, Flight ID: {passenger.flight_id}") #<- QUESTION: why doesn't passenger.name.flight_id work, assuming p = to name that we will append, shouldn't passenger.name.flight_id work?
        print("---------")

    def delay(self, amount):
        self.duration += amount


    #(Olaf:"this is a function, that appends passengers to the list when used/called, remember self.passengers = [], per the line 13 - 18")
    def add_passenger(self, p):
        self.passengers.append(p)
        #setting passangers, represented by "p"'s flight_id. *Remember that "self" is the flight object. The attribute of each p(passenger).
        #(Olaf:"this line creates an additional attribute "flight_id" on the appended passenger(p).
        p.flight_id = self.id #<- self.id is actually referencing the self.id above between lines 8 - 13, remember, which is = flight counter when a new object under the flight class is created.
                                #Example: p.flight_id = self.id = Flight.counter += 1
                            # p is then appended into a list [], name along with the new attribute it picked up.
                                #Example(python documentation): string_list.append(1) adds 1 to the list string_list.
                                #Thus self.passengers.append(p), adds p to the self.passenger list


#creates a class, name passenger(which takes a variable), and added into a variable
class Passenger:

    def __init__(self, name):
        self.name = name



def main():

    # Create flight.
    #(Olaf"these are essentially "objects"")
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



    #print list
    list2=[1,2,3,4, "this is list2"]
    print(list2)
    print (list())
    #print(alice.p)
    print(f"Toby's secret flight ID: {toby.flight_id}")
    print(f"Toby's secret flight ID: {toby.name}")


    #x=hasattr(alice,"flight_id")
    #print(x)

if __name__ == "__main__":
    main()
