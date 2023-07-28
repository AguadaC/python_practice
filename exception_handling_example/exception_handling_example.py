from typing import Union

# Exception block.
class ErrorException(Exception):
    """Custom Exception to be used as example."""
    pass


# Intermediate functions.
def generator_of_exceptions(number_str: str) -> None:
    """Converts a string into an integer and raises a ValueError or ErrorException if necessary.

    Args:
        number_str (str): The string to convert into an integer.

    Raises:
        ValueError: If the conversion from string to integer fails.
        ErrorException: If the resulting integer is less than 10.
    """

    try:
        number_int = int(number_str)

    except ValueError:
        print("Value Error happend.")
        raise

    if number_int < 10:
        print("ErrorException happend.")
        raise ErrorException("Our exception is raised.")


def function_with_raise(number: Union[str, int]) -> None:
    """Calls generator_of_exceptions with the given number, catching and re-raising any exception.
    If it catches ErrorException, re-raises ErrorException.

    Args:
        number (Union[str, int]): The number to pass to generator_of_exceptions.

    Raises:
        Exception: If any exception is raised in generator_of_exceptions.
    """

    try:
        generator_of_exceptions(str(number))

    except Exception:
        print("Catched exception. The same Exeption will be raised.")
        raise


def function_raise_exception(number: Union[str, int]) -> None:
    """Calls generator_of_exceptions with the given number, catching and raising a new Exception.
    If it catches ErrorException, re-raises Exception.

    Args:
        number (Union[str, int]): The number to pass to generator_of_exceptions.

    Raises:
        Exception: Always raises a new Exception, regardless of the exception in generator_of_exceptions.
    """

    try:
        generator_of_exceptions(str(number))

    except Exception:
        print("Catched exception. A based Exeption will be raised.")
        raise Exception("From function_raise_exception()")


def function_without_try_except(number):
    """Calls generator_of_exceptions with the given number without using try-except.

    Args:
        number (Union[str, int]): The number to pass to generator_of_exceptions.
    """

    generator_of_exceptions(str(number))


# Main function.
def main() -> None:
    """This is the main function where we call function_with_raise, function_raise_exception,
    and function_without_try_except. These functions handle exceptions from generator_of_exceptions
    in different ways. Observe the behavior between them."""

    # Input: "Hi"
    print("function_with_raise block - Input: 'Hi'")
    try:
        function_with_raise("Hi")
    except ValueError:
        print("ValueError caught.")

    print()
    print("function_raise_exception block - Input: 'Hi'")
    try:
        function_raise_exception("Hi")
    except Exception as e:
        print(f"Exception caught, with following message: {e}")

    print()
    print("function_without_try_except block - Input: 'Hi'")
    try:
        function_without_try_except("Hi")
    except ValueError:
        print("ValueError caught.")

    # Input: 2
    print()
    print("function_with_raise block - Input: 2")
    try:
        function_with_raise(2)
    except ErrorException as e:
        print(f"ErrorException caught, with following message: {e}")

    print()
    print("function_raise_exception block - Input: 2")
    try:
        function_raise_exception(2)
    except Exception as e:
        print(f"Exception caught, with following message: {e}")

    print()
    print("function_without_try_except block - Input: 2")
    try:
        function_without_try_except(2)
    except ErrorException as e:
        print(f"ErrorException caught, with following message: {e}")

if __name__ == "__main__":
    main()
