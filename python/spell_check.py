# 
# Spell Check
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def spell_check(s, w):
    """This function takes a string s and a set of words w, and counts how many words in the
    string are not present in the words set. The string and set of words are all lower case
    and do not contain symbols or numbers.

    Example 1: "hello world", [... "hello", "world" ...] -> 0  there are no words in the string that
        are not present in the set.
    Example 2: "helol wrodl", [... "hello", "world" ...] -> 2  There are two words ('helol' and 'wrodl')
        that are not present in the set.
    Example 3: "this is a bunch of words", [...] -> 0  There are no words in the string that are not
        present in the set.

    Parameters
    ----------
    s : str
        The string to be checked.
    w : set
        This set of all correctly spelled words.
    
    Returns
    -------
    int
        The number of words that were not present in the set.
    """
    pass


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python spell_check.test.py")