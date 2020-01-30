# 
# Postal Code
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def is_valid_postal_code(p):
    """This function takes a string p, and checks if it is a valid postal code. 
    A postal code is exactly 6 characters long, alternating letters and numbers.
    All postal codes are of the format LNLNLN ,where N is a number and L is a letter.

    Example 1: "A1B2C3" -> True  because the string contains exactly 6 characters matching LNLNLN.
    Example 2: "1A2B3C" -> False  because a postal code must start with a letter.
    Example 3: "A11B2C" -> False  because the postal code does not match LNLNLN.
    Example 4: "" -> False  because there are not exactly 6 characters.

    Parameters
    ----------
    p : str
        The string to be checked.
    
    Returns
    -------
    bool
        True if the string is a valid postal code, otherwise False.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python postal.test.py")