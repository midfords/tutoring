# 
# Sentence
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def sentence_formatter(s):
    """This function takes a string s, and formats the phrase into a proper sentence.
    The first letter of each word following a period must be capitalized, all other letters
    are lower case. If there is no period at the end of the sentence, one must be added.

    Example 1: "this is a sentence" -> "This is a sentence."  the first letter of the 
        sentence is capitalized and a period has been added to the end.
    Example 2: "this is a sentence. this is another sentence" -> "This is a sentence. 
        This is another sentence."  the first letter of each sentence is capitalized 
        and a period has been added to the end.
    Example 3: "This is a sentence..." -> "This is a sentence."  the first letter of 
        the sentence is capitalized and a single period is put at the end.
    Example 4: "" -> "."  since there are no words, the same empty string is returned 
        with a single period added to the end.

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
    print("Do not run this file directly. \nRun the test file instead: python sentence.test.py")