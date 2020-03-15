class Flight:

    counter = 1 #Olaf: "get a counter going"

    def __init__(self, origin, destination, duration):  #Olaf: "declare a function, init to ensure users put in these arguments when using the class"

        # Keep track of id number.
        self.id = Flight.counter    #Olaf: "create an object agnostic id, so that every object under the flight class will include a ".id" which is = to the Flight.counter"
        Flight.counter += 1     #Olaf: "Flight counter adds 1 to every object under the flight class creates"

        # Keep track of passengers.
        self.passengers = []    #Olaf: "creates a ".passenger" attribute to every object under the flight class"

        # Details about flight.     #Olaf: "every object under the flight class will have the following attributes"
        self.origin = origin    #Olaf: "this stores the origin from the init argument, line 5, into the attribute of the object"
        self.destination = destination
        self.duration = duration


#Olaf: "below this line are mostly functions that we'll need for our main code to work. (!)Most of them works under the class, flight and items defined within the class(!)"

    def print_info(self):   #Olaf: "creates a function that prints the argument passed in"
        print(f"Flight origin: {self.origin}")      ##Olaf: "prints the origin of the argument(object) passed in"
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:       #Olaf: "loops over the list, self.passengers and prints the values of each items within the list."
            print(passenger)

    def delay(self, amount):        #Olaf: "creates a function that takes in an argument(amount) which allows us to add delay to flight, by alterning the duration attribute of the said object(flight)"
        self.duration += amount

    def add_passenger(self, p):     #Olaf: "creates a function that takes the argument p and append it to the list self.passengers"
        self.passengers.append(p)
        p.flight_id = self.id       #Olaf: "it also adds a subtle flight_id attribute which is derived from self.id, which is in turn, from the value of Flight.counter"

#Olaf: "below this line is class again"
class Passenger:    #Olaf: "this is a new class which is used to catagorise objects under"

    def __init__(self, name):       #Olaf: "a function that states, when an object is created under this class it would require name as an input/argument"
        self.name = name        #it then passes the input as the attribute in the objects under this class.

    def __repr__(self):
        return self.name

#Olaf: "Below this line is the main(haha) code"
def main():

    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)   #Olaf: "creates an object under the Flight class, passing values into it's attributes"

    # Create passengers.
    alice = Passenger(name="Alice") #Olaf: "creates an object under the Passenger class, passing values into it's attribute"
    bob = Passenger(name="Bob")

    # Add passengers.
    f1.add_passenger(alice) #Olaf: "calls on the function add_passenger on the object f1(under the Flight class), adding the argument into the list in f1(aka self).passengers and giving an additional attribute named flight_id to each f1.passengers"
    f1.add_passenger(bob)

    f1.print_info() #Olaf: "calls on the function print_info which prints out a bunch of attributes of the object under the Flight class"
                    #Olaf: "followed by looping over the list within the object(under the class Flight)'s passenger attribute. (f1.passenger) which prints out the names of each passenger within that list."

if __name__ == "__main__":
    main()
