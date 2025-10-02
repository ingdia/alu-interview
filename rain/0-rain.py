#!/usr/bin/python3
"""
Module to calculate the total amount of rainwater retained between walls.
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained between walls.

    Args:
        walls (list): List of non-negative integers representing wall heights.

    Returns:
        int: Total units of rainwater retained.
    """
    if not walls:  # Handle empty list
        return 0

    total_water = 0
    left, right = 0, len(walls) - 1
    left_max = right_max = 0

    while left < right:
        # Update maximum heights from left and right
        left_max = max(left_max, walls[left])
        right_max = max(right_max, walls[right])

        # Process the smaller wall
        if left_max <= right_max:
            # Water at left: min of left_max, right_max minus current height
            total_water += left_max - walls[left]
            left += 1
        else:
            # Water at right: min of left_max, right_max minus current height
            total_water += right_max - walls[right]
            right -= 1

    return total_water