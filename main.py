"""
CSCI-261 (Algorithms) HW 4
Authors: Robert Liedka, Bryan Quinn, Brendan Jones
Purpose: To use Dynamic Programming to solve for pretty printing
"""
import sys

# Max number of chars per line
M = 90

# Used for impossible placements on the cost matrix
infinity = float('inf')


def print_cost_matrix(cost_matrix):
    """
    Given a cost matrix, surround the border with i and j and print
    out the matrix values
    :param cost_matrix: The 2D array representing a matrix
    :return: None
    """
    print('       ', end='')
    for i in range(0, len(cost_matrix)):
        if i < 10:
            print('j=' + str(i) + '     ', end='')
        else:
            print('j=' + str(i) + '    ', end='')
    print('')
    for i in range(0, len(cost_matrix)):
        if i < 10:
            print('i=' + str(i) + ' ', end='')
        else:
            print('i=' + str(i), end='')
        for j in range(0, len(cost_matrix)):
            cost = str(cost_matrix[i][j])
            while len(cost) < 3:
                cost += " "

            print(" | " + cost + " |", end='')
        print("")
    return cost_matrix


def build_cost_matrix(words):
    """
    Given a list of words, create the 2D Cost Matrix where
    the cost is the number of spaces left on a line for a given
    word to line placement.
    :param words: The array of words
    :return: A list of lists (2D Array) representing the costs
    """
    # Initialize the matrix initially with infinity in each
    cost_matrix = [[infinity for i in range(len(words))] for j in range(len(words))]

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
    # print_cost_matrix(cost_matrix)
    return cost_matrix


def find_min_cost_results(words):
    """
    Helper function used to find the results array needed to traverse
    the cost matrix
    :param words: The list of words to use for the cost matrix
    :return: The results array to use for traversing
    """
    min_cost = [None] * len(words)
    result = [None] * len(words)
    
    cost_matrix = build_cost_matrix(words)

    for i in range(len(words) - 1, -1, -1):
        min_cost[i] = cost_matrix[i][len(words) - 1]
        result[i] = len(words)
        for j in range(len(words) - 1, i, -1):
            if not(cost_matrix[i][j-1] == infinity):
                if min_cost[i] > min_cost[j] + cost_matrix[i][j-1]:
                    min_cost[i] = min_cost[j] + cost_matrix[i][j-1]
                    result[i] = j
    return result


def build_pretty_string(words):
    """
    Given a list of words, build and return a string that represents
    the pretty version of the string where pretty is defined as
    having the minimum amount of spaces at the end of a line where
    the max line length is 70 characters, and all words are in the string.
    :param words: The list of words to build a string from
    :return: The pretty formatted string
    """
    min_cost_results = find_min_cost_results(words)

    result_string = ""
    line_tracker = 0
    word_tracker = 0

    while line_tracker < len(words):
        line_tracker = min_cost_results[word_tracker]
        for i in range(word_tracker, line_tracker):
            result_string += words[i] + " "
        result_string += "\n"
        word_tracker = line_tracker
    return result_string


def do_pretty_print(input_file_name, output_file_name):
    """
    Read input, grab all words from input, use the pretty
    string dynamic programming algorithm, then write out
    the pretty string to the output file name
    :param input_file_name: The name of the input file
    :param output_file_name: The namer of the output file
    :return: None
    """
    with open(input_file_name) as f:
        words = f.read().split()

    pretty_string = build_pretty_string(words)

    with open(output_file_name, 'w') as f:
        f.write(pretty_string)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid number of args provided, please provide, read file & write file")
    else:
        do_pretty_print(sys.argv[1], sys.argv[2])
