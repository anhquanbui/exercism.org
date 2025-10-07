def is_armstrong_number(number: int) -> bool:
    """Determine if a number is an Armstrong number.

    An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.

    :param number: int - input number.
    :return: bool - True if number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(number)]
    num_digits = len(digits)
    armstrong_sum = sum(d ** num_digits for d in digits)
    return armstrong_sum == number
