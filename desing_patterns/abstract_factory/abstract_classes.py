from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFaction(ABC):
    """Abstract class to be used as superclass."""

    @abstractmethod
    def create_caracter(self, name) -> AbstractCaracter:
        pass
    
    @abstractmethod
    def create_weapon(self) -> AbstractWeapon:
        pass


class AbstractCaracter(ABC):
    """Abstract class to be used as superclass."""

    @abstractmethod
    def presentation(self) -> str:
        pass

    @abstractmethod
    def attack(self, weapon : AbstractWeapon) -> None:
        pass


class AbstractWeapon(ABC):
    """Abstract class to be used as superclass."""

    @abstractmethod
    def invoke(self) -> str:
        pass