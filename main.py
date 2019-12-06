# Algo HW 4
# Robert Liedka, Bryan Quinn, Brendan Jones
import sys

M = 10  ## Max number of chars per line


# If a given line contains words i through j and leave exactly one space between words
# the number of extra space chars at the eol is: M - j + i - sum(j, k=i)lk
def DoPrettyPrint(fromFileName, toFile):
    with open(fromFileName) as fromFile:
        content = fromFile.read()
    newString = ""
    charOffset = 0

    while True:
        spaces = 0
        if charOffset + M < len(content):
            currentLine = content[charOffset: charOffset + M]
            while currentLine[len(currentLine) - spaces - 1] != " ":  # walk back
                spaces += 1
            newString += currentLine[0:M - spaces - 1] + (" " * spaces) + "\n"
            charOffset += M - spaces
        else:
            currentLine = content[charOffset:]
            spaces = M - len(currentLine)
            newString += currentLine + (" " * spaces) + "\n"
            break

    print(newString)


def recursive_pretty_print(from_file_name, to_file_name):
    pass


def num_extra_spaces_in_line(words, starting_index, ending_index):
    """
    Given a list of words, a starting index, and and ending index,
    this function returns how many extra spaces there would be in a
    line if all the words from the words[starting_index] to words[ending_index]
    :param words: The list of words
    :param starting_index: The starting index of words to put on the line
    :param ending_index: The ending index of words to put on the line
    :return: The number of extra spaces there would be on a line
    """
    words_to_put_on_line = words[starting_index:ending_index + 1]
    num_characters_in_line = num_characters_in_words(words_to_put_on_line)

    num_spaces_between_words = (ending_index - starting_index)
    return M - num_spaces_between_words - num_characters_in_line


def num_characters_in_words(words):
    """
    Given a list of words, find the total number of characters for all words in words
    :param words: The list of words to count characters for
    :return: The total number of characters for all the words in the list words
    """
    num_characters = 0
    for word in words:
        num_characters += len(word)
    return num_characters


# if __name__ == '__main__':
#     if (len(sys.argv) != 3):
#         print("Invalid number of args provided, please provide, read file & write file")
#     else:
#         DoPrettyPrint(sys.argv[1], sys.argv[2])

# Example line
# continuous internationalization integration summation productization

## Tests
def test_num_characters_in_words():
    words = ["apple", "banana", "fruit", "bacon"]
    actual = num_characters_in_words(words)
    expected = 21
    passing = actual == expected
    print("Num characters in words works? " + str(passing))
    if not passing:
        print("Expected " + str(expected))
        print("Actual " + str(actual))

def test_num_extra_spaces_in_line():
    words = ["apple", "banana", "fruit", "bacon"]
    actual = num_extra_spaces_in_line(words, 0, len(words) - 1)
    expected = M - len("apple banana fruit bacon")
    passing = actual == expected
    print("Num extra spaces in line works? " + str(passing))
    if not passing:
        print("Expected " + str(expected))
        print("Actual " + str(actual))

def test_num_extra_spaces_in_line_indexed():
    words = ["apple", "banana", "fruit", "bacon"]
    actual = num_extra_spaces_in_line(words, 1, 2)
    expected = M - len("banana fruit")
    passing = actual == expected
    print("Num extra spaces in line works? " + str(passing))
    if not passing:
        print("Expected " + str(expected))
        print("Actual " + str(actual))

def test_num_extra_spaces_in_line_single_word():
    words = ["apple", "banana", "fruit", "bacon"]
    actual = num_extra_spaces_in_line(words, 1, 1)
    expected = M - len("banana")
    passing = actual == expected
    print("Num extra spaces in line works? " + str(passing))
    if not passing:
        print("Expected " + str(expected))
        print("Actual " + str(actual))

#test_num_characters_in_words()
test_num_extra_spaces_in_line_single_word()
test_num_extra_spaces_in_line()
test_num_extra_spaces_in_line_indexed()
# With [apple, banana, fruit, bacon] we get this line:
#apple banana fruit bacon
#123456789123456789212345
# This has 25 characters in it
# Max characters is 90
# 90 - 25 = 65
# The definition of the function is giving 66
# 90 - 4 + 1 - 21
# 87 - 21 = 66

infinity = float('inf')



def build_cost_matrix(words):
    # Initialize the matrix initially with infinity in each
    cost_matrix = [[float('inf') for i in range(len(words))] for j in range(len(words))]

    # Populate the matrix with the cost (if positive) for each potential word placement
    for i in range(0, len(words)):
        # Put the i-th word in the i-th line
        cost_matrix[i][i] = M - len(words[i])
        for j in range(i + 1, len(words)):
            previous_word_cost = cost_matrix[i][j-1]
            current_word_cost = len(words[j])
            cost_of_space_between_words = 1
            total_new_cost = previous_word_cost - current_word_cost - cost_of_space_between_words

            # Only update the value if it has a positive cost,
            # otherwise, it will remain as infinite value
            if total_new_cost >= 0:
                cost_matrix[i][j] = total_new_cost

    return cost_matrix


def find_result_indexes(words):
    min_cost = [None] * len(words)
    result = [None] * len(words)
    
    cost_matrix = build_cost_matrix(words)

    
    for i in range(len(words) - 1, -1, -1):
        min_cost[i] = cost_matrix[i][len(words) - 1]
        result[i] = len(words)
        for j in range(len(words) - 1, i, -1):
            if not(cost_matrix[i][j-1] == infinity):
                if min_cost[i] > min_cost[j] + cost_matrix[i][j - 1]:
                    min_cost[i] = min_cost[j] + cost_matrix[i][j-1]
                    result[i] = j

    result_string = ""
    line_tracker = 0
    word_tracker = 0
    while line_tracker < len(words):
        line_tracker = result[word_tracker]
        for i in range(word_tracker, line_tracker):
            result_string += words[i] + " "
        result_string += "\n"
        word_tracker = line_tracker
    return result_string




print(find_result_indexes(["apple", "banana", "bacon", "cheese", "cat", "amazing"]))
