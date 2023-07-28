from concrete_classes import (AbstractFaction,
                              ConcreteFactionWarrior,
                              ConcreteFactionWizard)

def checking_faction(faction : AbstractFaction, name) -> None:
    """Code to try each faction.

    Args:
        faction (AbstractFaction): Any faction can be called.
    """

    caracter = faction.create_caracter(name)
    weapon = faction.create_weapon()

    print(caracter.presentation())
    print(caracter.attack(weapon))

if __name__ == "__main__":
    """Main function."""

    checking_faction(ConcreteFactionWarrior(), "Juan")
    print()
    checking_faction(ConcreteFactionWizard(), "Pedro")