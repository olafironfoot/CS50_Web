class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):   #gives the object, "Flight" a new functionality
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print("\n")


def main():

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()

    f2 = Flight(origin="Tokyo", destination="Shanghai", duration=185)
    f2.print_info()

    f3 = Flight(origin="Singapore", destination="Australia", duration = 1000000)
    f3.print_info()

    f1.print_info()


if __name__ == "__main__":
    main()
