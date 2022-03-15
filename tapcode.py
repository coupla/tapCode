
ENGLISH_TABLE = [['A','B','K','D','E'],
                ['F','G','H','I','J'],
                ['L','M','N','O','P'],
                ['Q','R','S','T','U'],
                ['V','W','X','Y','Z']]      # chose K because of acknowledgements via K (as in OK)
WRONG_CHARACTER = '[?]'    # Symbol for the decoding of an unsupported character
TAP_CHARACTER = '#'        # Symbol for conversion back into tap

auto_x = True

def index2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def tap_to_coordinates(input_string):
    coordinates = [] #Declare empty list
    for i in input_string.split(): #For word in the input string...
        coordinates.append(len(i)-1) #...append the length of the word to coordinates
    return [coordinates[i:i + 2] for i in range(0, len(coordinates), 2)]

def coordinates_to_text(input_string):
    output_string = []

    for i in input_string:
        if len(i) != 2:
            output_string.append(WRONG_CHARACTER)
            continue
        else:
            y, x = i #got XY backward
            if x <= 5 and y <= 5:
                if auto_x and (x == 5 and y == 3):
                    output_string.append('\n')
                else:
                    output_string.append(ENGLISH_TABLE[y][x])
            else:
                output_string.append(WRONG_CHARACTER) #most of my shit is in the "elses" as well as redundant WRONG outputs
    return "".join(output_string)

def text_to_coordinates(input_string):
    output_coords = []
    input_string = input_string.upper()

    for i in input_string:
        if i.isalpha():
            if i != 'C':
                output_coords.append(index2d(ENGLISH_TABLE,i))
            else:
                output_coords.append(index2d(ENGLISH_TABLE,'K'))
    return output_coords

def coordinates_to_tap(input_string):
    output_string = []

    for i in input_string:
        for j in i:
            output_string.append(TAP_CHARACTER*(j+1))
            output_string.append(" ")
    return "".join(output_string)

def text_to_tap(input_string):
    return coordinates_to_tap(text_to_coordinates(input_string))



print(text_to_tap(coordinates_to_text(tap_to_coordinates("..... .. . . .... .... . ..... .... .. ..... ... ..... .. . . .... .... . ..... .... .."))))

