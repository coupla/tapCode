# tapcode.py -- Utilities to convert strings to and from "tap code"
# https://en.wikipedia.org/wiki/Tap_code

# Define polybius square of letters, using K instead of C as K is used for acknowledgements and is read just as fine.
ENGLISH_TABLE = [['A', 'B', 'K', 'D', 'E'],
                 ['F', 'G', 'H', 'I', 'J'],
                 ['L', 'M', 'N', 'O', 'P'],
                 ['Q', 'R', 'S', 'T', 'U'],
                 ['V', 'W', 'X', 'Y', 'Z']]  # chose K because of acknowledgements via K (as in OK)

# Symbol for the decoding of an unsupported character
WRONG_CHARACTER = '[?]'

# Symbol for the conversion back into tap. Works best with . or #
TAP_CHARACTER = '#'

# Set to true to omit printing X and instead print a new line
AUTO_X = True


# Utility to find an index of a value in a 2D list. Stolen from StackExchange
def index_in_2d(input_list, v):
    for i, x in enumerate(input_list):
        if v in x:
            return i, x.index(v)


# Converts an input_string of taps into list of coordinates
def tap_to_coordinates(input_string):
    # Declare an empty list
    coordinates = []

    # For each word in the list...
    for i in input_string.split():
        # ...append the length of the word to coordinates
        coordinates.append(len(i) - 1)

    # Return a list of coordinates, each coordinate it's own sublist within.
    return [coordinates[i:i + 2] for i in range(0, len(coordinates), 2)]


# Converts an input_list of coordinates into text
# TODO: Refactor such that the bulk of work is in the if and not in the else.
def coordinates_to_text(input_list):
    # Declare an empty list
    output_string = []

    # For all coordinates...
    for i in input_list:

        if len(i) != 2:
            output_string.append(WRONG_CHARACTER)  # If a coordinate is malformed, we don't recognize it.
            continue

        else:
            y, x = i
            if x <= 5 and y <= 5:
                if AUTO_X and (x == 5 and y == 3):
                    output_string.append('\n')  # If we're treating X as a new line, make a new line
                else:
                    output_string.append(ENGLISH_TABLE[y][x])  # ...append the correspondent letter
            else:
                output_string.append(WRONG_CHARACTER)  # We don't recognize coordinates outside of our acceptable range.

    # Return the new text string
    return "".join(output_string)


# Converts an input_string into a list of coordinates
def text_to_coordinates(input_string):
    # Declare an empty list
    output_coordinates = []

    # Normalize the input string into uppercase
    input_string = input_string.upper()

    # For all incoming letters...
    for i in input_string:
        if i.isalpha():
            if i != 'C':
                output_coordinates.append(index_in_2d(ENGLISH_TABLE, i))  # ...append the appropriate coordinate.
            else:
                # If the letter is C...
                output_coordinates.append(index_in_2d(ENGLISH_TABLE, 'K'))  # ...append the coordinate for K.

    # Return our coordinates
    return output_coordinates


# Converts an input_string into taps
def coordinates_to_tap(input_string):
    # Declare an empty list
    output_string = []

    # For every word...
    for i in input_string:
        for j in i:
            output_string.append(TAP_CHARACTER * (j + 1))  # ...append a tap the amount of times needed by coordinate.
            output_string.append(" ")  # Add a space for readability.

    # Return the tap string
    return "".join(output_string)


# Wrapper function to convert from text to tap without writing the coordinates stage.
def text_to_tap(input_string):
    return coordinates_to_tap(text_to_coordinates(input_string))


# All going well, this print statement returns the string within the nested functions. But with # instead of .
print(text_to_tap(coordinates_to_text(
    tap_to_coordinates("..... .. . . .... .... . ..... .... .. ..... ... ..... .. . . .... .... . ..... .... .."))))
