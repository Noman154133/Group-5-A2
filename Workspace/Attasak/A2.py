import random

def generate_random_numbers(count, lower_bound, upper_bound):
    """Generate a list of random numbers.

    Args:
        count (int): The number of random numbers to generate.
        lower_bound (int): The lower bound for the random numbers.
        upper_bound (int): The upper bound for the random numbers.

    Returns:
        list: A list containing the generated random numbers.
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(count)]