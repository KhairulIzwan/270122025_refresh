#!/usr/bin/env python3
"""
This script demonstrates basic Python functionality with detailed explanations.
"""

# Import the necessary module
import math  # Importing the math module to perform mathematical operations

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
        radius (float): The radius of the circle.
    
    Returns:
        float: The area of the circle.
    """
    # Calculate the area using the formula: area = π * radius^2
    area = math.pi * radius ** 2  # math.pi provides the value of π (pi)
    return area  # Return the calculated area

def main():
    """
    Main function to execute the script.
    """
    # Define the radius of the circle
    radius = 5.0  # Assigning a value of 5.0 to the radius variable
    
    # Calculate the area of the circle
    area = calculate_circle_area(radius)  # Calling the function to calculate the area
    
    # Print the result
    print(f"The area of the circle with radius {radius} is {area:.2f}")  # Displaying the result with 2 decimal places

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to execute the script