def rectangle_area(length,width):
    """This function calculates area of rectangle.
    parameters: length, width
    Returns: area"""
    
    return length * width 
    
print(rectangle_area.__doc__)
print("area:",rectangle_area(5,3))