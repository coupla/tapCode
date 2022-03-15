# tapCode

Playing around with tap code, a form of communication similar to morse code, but without a reliance on a consistent rhythm. Currently translates from text to coordinates, coordinates to tap, and everywhere between. 

Ideally want to translate from text to audio of taps, and audio of tapes to text.

I've made the decision to represent C with K, as K is used for acknowledgement and feels to me like a more "important character".

A constant is available to enable/disable automatic line breaks when using the letter X, as X is used to indicate the end of a sentence. X is not printed.


## What is "tap code"?
[From Wikipedia:](https://en.wikipedia.org/wiki/Tap_code)
The tap code is based on a Polybius square using a 5×5 grid of letters representing all the letters of the Latin alphabet, except for K, which is represented by C. 

| A | B | C/K | D | E |
|    :----:   |    :----:   |    :----:   |    :----:   |    :----:   |
| F | G | H | I | J |
| L | M | N | O | P |
| Q | R | S | T | U |
| V | W | X | Y | Z |

Each letter is communicated by tapping two numbers, the first designating the row and the second (after a pause) designating the column. For example, to specify the letter "B", one taps once, pauses, and then taps twice. The listener only needs to discriminate the timing of the taps to isolate letters. 

## Usage
CC BY with the exception that this code should not be used to translate communication between prisoners.
