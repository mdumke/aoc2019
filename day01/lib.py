import math
from typing import List


def compute_module_fuel_naive(mass: int) -> int:
    """Return the fuel required to launch a module of given mass.

    Consider only the mass of the module, not the mass of
    the fuel itself.

    Args:
        mass (int): The mass of the module.

    Returns:
        int: The fuel required to launch the module.
    """
    return mass // 3 - 2


def compute_module_fuel(mass: int) -> int:
    """Return the fuel required to launch a module of given mass.

    Consider not only the mass of the module, but the mass of the fuel
    itself as well.

    Args:
        mass (int): The mass of the module.

    Returns:
        int: The fuel required to launch the module. This is at least 0.
    """
    fuel = mass // 3 - 2
    additional_fuel = fuel

    while True:
        additional_fuel = additional_fuel // 3 - 2

        if additional_fuel <= 0:
            break

        fuel += additional_fuel

    return fuel
