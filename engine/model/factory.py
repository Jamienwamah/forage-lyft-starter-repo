from calliope import Calliope
from glissade import Glissade
from palindrome import Palindrome
from rorschach import Rorschach
from thovex import Thovex


class CarFactory:
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_is_on: bool) -> Car:
        return Palindrome(current_date, last_service_date, warning_light_is_on)

    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
