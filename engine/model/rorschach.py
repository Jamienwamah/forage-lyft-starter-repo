from datetime import datetime
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        super().__init__(engine, battery)