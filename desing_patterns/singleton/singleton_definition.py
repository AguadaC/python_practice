class SingletonDefinition:
    """
    SingletonDefinition class represents a Singleton pattern implementation.
    It ensures that only one instance of the class exists throughout the program.
    """

    _instance = None

    def __new__(cls):
        """
        Creates and returns a new instance of the class if it doesn't exist.
        If an instance already exists, returns the existing instance.

        Returns:
            SingletonDefinition: The single instance of the class.
        """
        if cls._instance is None:
            cls._instance = super(SingletonDefinition, cls).__new__(cls)
            cls._instance.message = "Singleton Pattern"

        return cls._instance


def main():
    """
    Demonstrates the Singleton pattern by creating two instances of SingletonDefinition.
    Since it's a Singleton, both instances should be the same, sharing the same data.

    Prints:
        - The ID of the first singleton instance.
        - The ID of the second singleton instance.
        - The message attribute of the first singleton instance.
        - A boolean indicating if both instances are the same (True).
    """
    singleton1 = SingletonDefinition()
    singleton2 = SingletonDefinition()

    print("Singleton 1 ID:", id(singleton1))
    print("Singleton 2 ID:", id(singleton2))

    print("Message from Singleton 1:", singleton1.message)
    print("Are Singleton 1 and Singleton 2 the same instance?", singleton1 is singleton2)


if __name__ == "__main__":
    main()
