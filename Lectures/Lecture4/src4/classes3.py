class Flight:

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print("\n")

    def delay(self, amount):
        self.duration += amount

    #self created, print hellow world if used this
    def print_hello(self):
        print("hello world only lah, relax")


def main():

    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.delay(50)
    f1.print_info()
    f1.print_hello()


if __name__ == "__main__":
    main()
