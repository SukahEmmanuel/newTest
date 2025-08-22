class Flight:
    def __init__(self, number):
        self.capacity = number
        self.passengers = []

    def add_passenger(self, passenger_name):
        if not self.open_seats():
            return False
        self.passengers.append(passenger_name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


boeing235 = Flight(3)

people = ["Alice", "Bob", "Charlie", "David"]
for person in people:
    if boeing235.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")
        