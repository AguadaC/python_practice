import random

from abstract_classes import (AbstractFaction,
                              AbstractCaracter,
                              AbstractWeapon)


class ConcreteFactionWarrior(AbstractFaction):
    """Concrete Faction Warrior"""

    Faction = "Warrior"

    def create_caracter(self, name) -> AbstractCaracter:
        return ConcreteWarriorCaracter(name)

    def create_weapon(self) -> AbstractWeapon:
        return ConcreteWarriorWeapon()


class ConcreteFactionWizard(AbstractFaction):
    """Concrete Faction Wizard"""

    def create_caracter(self, name) -> AbstractCaracter:
        return ConcreteWizardCaracter(name)

    def create_weapon(self) -> AbstractWeapon:
        return ConcreteWizardWeapon()


class ConcreteWarriorCaracter(AbstractCaracter):
    """Concrete Warrior Caracter Class"""

    Faction = "Warrior"
    Max_Damage = 100

    def __init__(self, name) -> None:
        self.name = name

    def presentation(self) -> str:
        return f"My name is {self.name}, the greatest {self.Faction}"

    def attack(self, weapon: AbstractWeapon) -> None:
        weapon_type = weapon.invoke()
        return f"{weapon_type} did {random.randint(1, self.Max_Damage)}"


class ConcreteWizardCaracter(AbstractCaracter):
    """Concrete Wizard Caracter Class"""

    Faction = "Wizard"
    Max_Damage = 70

    def __init__(self, name) -> None:
        self.name = name

    def presentation(self) -> str:
        return f"My name is {self.name}, the greatest {self.Faction}"

    def attack(self, weapon: AbstractWeapon) -> None:
        weapon_type = weapon.invoke()
        return f"{weapon_type} did {random.randint(1, self.Max_Damage)}"



class ConcreteWarriorWeapon(AbstractWeapon):
    """Concrete Warrior Weapon Class"""

    Weapon = "Sword"

    def invoke(self) -> str:
        return self.Weapon


class ConcreteWizardWeapon(AbstractWeapon):
    """Concrete Wizard Weapon Class"""

    Weapon = "Crosier"

    def invoke(self) -> str:
        return self.Weapon