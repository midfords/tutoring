# 
# Red Green
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def is_red_green_even(l):
    """This function takes a list of strings l, and checks if it contains the same number of 
    "red" and "green" elements. The list of strings can be anything, but only the number of 
    "red" and "green" strings are compared.

    Example 1: ["red", "green"] -> True  because there is an equal number of "red" and "green".
    Example 2: ["red", "green", "Blue"] -> True  because there is an equal number of "red" and "green".
      The "Blue" string doesn't count.
    Example 3: ["red", "green", "green"] -> False  because there is not an equal number of "red" and "green".
    Example 4: ["Blue", "Yellow"] -> True  because there is still an even number of "red" and "green" (0 of each).
    Example 5: [] -> True  because there is still an even number of "red" and "green" (0 of each).

    Parameters
    ----------
    l : list
        The list of strings to be checked.
    
    Returns
    -------
    bool
        True if there are an equal number of "red" and "green", otherwise False.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python red_green.test.py")