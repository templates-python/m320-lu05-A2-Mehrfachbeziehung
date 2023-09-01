import pytest
from customer_reservation import Customer, Reservation

class TestCustomerReservation:

    @pytest.fixture
    def reservation(self):
        return Reservation('123', 'ESAF')


    @pytest.fixture
    def customer(self, reservation):
       return Customer('Julian', reservation)

    # Test für Reservation-Objekt. Noch ohne Zuweisung eines Customer-Objekts
    def test_reservation_number(self, reservation):
        assert reservation.number == '123'

    def test_reservation_event(self, reservation):
        assert reservation.event == 'ESAF'

    def test_reservation_without_customer(self, reservation):
        assert reservation.customer == None

    # Test Customer-Objekt und Customer-Referenz in Reservation-Objekt
    def test_customer_name(self, customer):
        assert customer.name == 'Julian'

    def test_customers_reservation(self, customer, reservation):
        assert customer.reservation is reservation

    def test_reservation_from_customer(self, customer, reservation):
        assert reservation.customer is customer




