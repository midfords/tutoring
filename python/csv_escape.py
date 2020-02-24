# 
# Csv Escape
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def csv_escape(l):
    """This function takes a list of strings l, and formats the items into escaped csv format.
    Each item is seperated by a comma "," character. If a string contains a comma in it, it 
    must be escaped by putting a "\\" character infront of it.

    Example 1: ["one", "two", "three"] -> "one,two,three"  a single string is prepared with 
        each item seperated by commas
    Example 2: ["one,two", "three,four"] -> "one\\,two,three\\,four"  These strings contain
        a comma, so they are escaped with a "\\" character before being joined with commas.
    Example 3: ["one"] -> "one"  a list with a single item will not have a comma.
    Example 4: ["", "", ""] -> ",,"  each empty string is seperated by a comma.
    Example 5: [] -> ""  an empty list produces an empty string

    Parameters
    ----------
    s : str
        The string to be formatted.
    
    Returns
    -------
    str
        The formatted string.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python csv_escape.test.py")