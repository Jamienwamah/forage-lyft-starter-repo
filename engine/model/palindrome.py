from datetime import datetime
from .car import Car
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery


class Palindrome(Car):
    def __init__(self, current_date: datetime, last_service_date: datetime, warning_light_is_on: bool):
        engine = SternmanEngine(warning_light_is_on)
        battery = NubbinBattery(last_service_date, current_date)
        super().__init__(engine, battery)