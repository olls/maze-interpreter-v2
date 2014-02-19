Syntax
======

Maze controls
-------------

Symbol | Description
:----: | :----------
## or `` | Wall. Cars will not pass through these.
..     | Path. Cars will follow these.
<>     | Splitter. Create a new thread.
42     | Any two-digit numeral. Pause the car for this amount of 'ticks'.
^^     | Start. One per maze only.
()     | Hole. Kill cars.
>>     | Print. Output the value held by the car.
<<     | Grab. Input a value.
--     | Will turn into a wall after being run over.
%L, %R, %D, %U | Directions. Force the car to go Left, Right, Down or Up.
**     | Signal. See below.
AA     | Any two letters. A function to be applied to the car.

Function commands
-----------------

Command | Description
:-----: | :----------
=       | Make equal to. Assign a new value to the car.
-=      | Subtracts a value from the car and store the result in the car.
+=      | Addition. Similar to -=
*=      | Multiplication. Similar to -=
/=      | Division. Similar to -=
<=, ==, >=, >, < | Comparative statements.
%L, %R, %D, %U | Directions. Force the car to go Left, Right, Down or Up.
**      | Signal statement. Return true if there exists a signal in the maze that has a car on it, false otherwise.
IF condition, THEN statement, ELSE statement | Conditional branch statement.
//      | Comment. Ignore the rest of the line.
->      | Define. Assign a function to a function name.