
""" This module contains usefull functions related to string data types """


### Compares string_1 and string_2 and prints the first line and word in which they are different.
def string_compare_differences(string_1, string_2):
    if string_1 == string_2:
        print("Both strings are equal")
    else:
        for index_line, line in enumerate(string_1.split("\n")):
            if not line == string_2.split("\n")[index_line]:
                print("The line of index", index_line, "is different")
                for index_word, word in enumerate(line.split()):
                    if not word == string_2.split("\n")[index_line].split()[index_word]:
                        print("Found word '" + string_2.split("\n")[index_line].split()[index_word] + "' but was expecting '" + word + "'")


if __name__ == "__main__":
    print("I prefer to be a module :)")
    print("But I can do some tests for you.")

    string_1 = """
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.
    """

    string_2 = """
    Lorem ipsum dolor sit amet,
    consectetur adipiScing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.
    """
    print()    
    print("Here is a test for string_compare_differences():")
    string_compare_differences(string_1, string_2)