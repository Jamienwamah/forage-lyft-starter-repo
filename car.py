from abc import ABC, abstractmethod
from datetime import datetime

# Serviceable interface
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

# Engine interface
class Engine(Serviceable, ABC):
    pass

# Battery interface
class Battery(Serviceable, ABC):
    pass

# Car class
class Car:
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
