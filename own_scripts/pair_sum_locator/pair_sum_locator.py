import numpy as np
from typing import List, Tuple

def find_two_sum(numbers: List[int], target_sum: int) -> Tuple[int, int]:
    """
    Find two elements in the list of numbers whose sum is equal to the target sum.

    Args:
        numbers (List[int]): The list of numbers.
        target_sum (int): The required target sum.

    Returns:
        Tuple[int, int] or None: A tuple containing the indices of the two elements whose sum is equal to target_sum,
            or None if no such elements are found.

    Raises:
        ValueError: If 'numbers' is not a list of integers, if 'target_sum' is not an integer,
            or if 'numbers' has fewer than two elements.
    """
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input 'numbers' must be a list of integers.")
    
    if not isinstance(target_sum, int):
        raise ValueError("Input 'target_sum' must be an integer.")
    
    if len(numbers) < 2:
        raise ValueError("Input 'numbers' must contain at least two elements.")

    numbers = np.array(numbers)
    scroll_vector = numbers[1:]
    sum_index = 1
    index_result = None
    while len(numbers) > 0:
        vector_sum = (numbers[0:-1]+scroll_vector)
        if target_sum in vector_sum:
            index_result = np.where(vector_sum ==target_sum)[0][0]
            return index_result, index_result+sum_index
        else:
            sum_index += 1
            numbers = numbers[0:-2]
            scroll_vector = scroll_vector[1:-1]
    return None

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
    print(find_two_sum([3, 1], 10))
