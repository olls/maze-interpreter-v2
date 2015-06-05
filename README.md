Maze Interpreter v2
===================

My second attempt at a Maze interpreter: http://esolangs.org/wiki/Maze

All the examples on the Esolangs wiki page work. I'm not entirely sure if the Turing complete example works correctly, because I'm not exactly sure what it is meant to do, but it doesn't enter the loop properly. See some examples in the [programs](https://github.com/olls/maze-interpreter-v2/tree/master/programs) directory.

Please create an issue or pull request if you find a problem :)

![A Fibonacci program running with the interpreter.](http://oliverfaircliff.com/~olls/readme-imgs/maze-interpreter/fibonacci.png)


Usage
-----

Depends on python3.

    usage: main.py [-h] [-d] [-c] [-f FPS] file

    A Maze interpreter (http://esolangs.org/wiki/Maze)

    positional arguments:
      file               the program to run

    optional arguments:
      -h, --help         show this help message and exit
      -d, --debug        display the maze during interpretation.
      -c, --no-colors    shows the maze without color when in debug mode.
      -f FPS, --fps FPS  the fps of the maze when in debug mode.


[Syntax](https://github.com/olls/maze-interpreter-v2/blob/master/syntax.md)
---------------------------------------------------------------------------

The parsing is not perfect, but it seems to work well enough. It allows a much simpler syntax than that on the Esolangs wiki, although that works fine too. The commas are not needed between the commands, but you can add as much white space as you want, it will be ignored. Because the white space is ignored, the examples on the wiki need the leading white space converted to walls to align them properly. You can also use a ``` `` ``` (double tick) as a wall, to reduce the heaviness of the solid wall areas.


Behavior
--------

The specification on the Esolangs wiki is a bit ambiguous in places, so I have had to make some assumptions:

 - The program currently generates an error and exits if two cars are in the same cell, this can be easily changed, but it is not clear from the wiki what is meant to happen.
 - The cars will attempt to move in the direction they were last travelling in first. The opposite direction to the direction they were last travelling in is always tried last. Otherwise directions are tried in this order: `U`, `R`, `D`, `L`.
 - Many start positions are allowed in the map, this is disallowed in the specification, but I included it because it allows more freedom in creating programs. Although it can be fun to make programs just one start as well.
