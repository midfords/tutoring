# 
# Name
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def is_valid_name(n):
    """This function takes a string p, and checks if it is a valid first and last name. 
    A valid first and last name contains only letters and a single space, and must be at least
    5 characters long in total.

    Example 1: "marry modern" -> True  because the string contains a single space, letters and is 12 characters long.
    Example 2: "a b" -> False  because this name is not at least 5 characters long.
    Example 3: "a114n sh3pp4rd" -> False  because a name can not contain numbers.
    Example 4: "james" -> False  because there is no space character
    Example 5: "james jimmy john" -> False  because a first and last name can only contain a single space.

    Parameters
    ----------
    n : str
        The string to be checked.
    
    Returns
    -------
    bool
        True if the string is a valid first and last name, otherwise False.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python name.test.py")