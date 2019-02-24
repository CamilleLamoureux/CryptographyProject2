# Cryptography Project
Made by Anaïs Depeau and Camille Lamoureux

## Description
The key is two integers :
- __n__ : greater or equal to 2
- __offset__ : greater or equal to 0

Note that _n_ is a number of rows and _offset_ a shift.

### Ciphering a text
1. Convert to uppercase the text and remove blanks
2. Place the letters like waves of hight _n_, with eventually a shift of the first wave according to the value of _offset_
3. Take the letters from left to right on each row, and the rows from top to bottom

### Deciphering a text
1. Write the letters from left to right, row by row, from top to bottom, at the good places
2. We read the waves from left to right

## First example of use
Considering the text : "Hello World", with the key n = 6 and offset = 0

We imagine a two-dimensional array of 6 rows and 10 coumns (6 rows because of n and 10 columns because our plain text has 10 caracters)

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** | H |   |   |   |   |   |   |   |   |   | 
| **1** |   | E |   |   |   |   |   |   |   | D |     
| **2** |   |   | L |   |   |   |   |   | L |   |
| **3** |   |   |   | L |   |   |   | R |   |   |
| **4** |   |   |   |   | O |   | O |   |   |   |
| **5** |   |   |   |   |   | W |   |   |   |   |

You can see that, when we reach the bottom of the array, we go up, and inversely when we reach the top we go down. We process from left to right.

The cipher text is : HEDLLLROOW

## Second example of use
Still considering the text "Hello Wordl", but with the key n = 6 and offset = 7.
We get this table :

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |
|---|---|---|---|---|---|---|---|---|---|---|
| **0** |   |   |   | L |   |   |   |   |   |   | 
| **1** |   |   | L |   | O |   |   |   |   |   |     
| **2** |   | E |   |   |   | W |   |   |   |   |
| **3** | H |   |   |   |   |   | O |   |   |   |
| **4** |   |   |   |   |   |   |   | R |   | D |
| **5** |   |   |   |   |   |   |   |   | L |   |

And the cipher text becomes : LLOEWHORDL 
