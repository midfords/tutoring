# 
# Csv Escape 2
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def csv_escape(l):
    """This function takes a list of strings l, and formats the items into escaped csv format.
    Each item is seperated by a comma "," character. If a string contains a comma in it, it 
    must be escaped by wrapping the value in "quotation marks". If a value contains the quotation
    mark character already, it must be escaped by placing a second quotation mark character infront
    of it.

    Example 1: ["one", "two", "three"] -> one,two,three  a single string is prepared with 
        each item seperated by commas
    Example 2: ["one,two", "three", "four"] -> "one,two",three,four  One of these strings contains
        a comma, so it is escaped by wrapping the value in quotation marks before joining them with
        comma characters ','.
    Example 3: [" "hello," ", " world"] -> " ""hello,"" ", world  This example contains a string with both
        a comma and a quotation mark. First the quotation mark is escaped, then the value is wrapped
        in strings.
    Example 4: ["one"] -> "one"  a list with a single item will not have any commas.
    Example 5: ["", "", ""] -> ",,"  each empty string is seperated by a comma.
    Example 6: [] -> ""  an empty list produces an empty string

    Parameters
    ----------
    l : list
        The list of strings to be formatted.
    
    Returns
    -------
    str
        The formatted string.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python csv_escape_2.test.py")