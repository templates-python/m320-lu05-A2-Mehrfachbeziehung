class Reservation:

    def __init__(self, number, name):
        self._event  = name
        self._number = number
        self._the_customer = None

    @property
    def event(self):
        return self._event

    @property
    def number(self):
        return self._number

    @property
    def customer(self):
        return self._the_customer

    @customer.setter
    def customer(self, customer):
        self._the_customer = customer


    def to_string(self):

        print(self.customer)

        if self.customer != None:
          return f'Reservation {self.number} {self.event} für Kunde {customer.name}'
        else:
          return f'{self.event} ist kein Kunde zugeordnet'

class Customer:

    def __init__(self, name, reservation):
        self._name          = name
        self._reservation   = reservation
        reservation.customer = self

    @property
    def name(self):
        return self._name

    @property
    def reservation(self):
        return self._reservation

    def to_string(self) -> str:
          return f'{self.name} hat eine Reservation für den Anlass {self._reservation.event}'




if __name__ == "__main__":
    reservation = Reservation('123', 'ESAF')
    customer    = Customer ('Julian', reservation)
    print("\n")
    print(customer.to_string())
    print(reservation.to_string())