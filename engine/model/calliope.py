from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from battery .sprindler_battery import SpindlerBattery


class Calliope(Car):
    def __init__(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(engine, battery)
