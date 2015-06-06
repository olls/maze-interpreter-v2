Maze Interpreter v2
===================

An interpreter for the Maze programming language, based on the description on the [Esolangs Wiki](http://esolangs.org/wiki/Maze).

Maze is a language based on an ASCII art 'maze' for 'cars' (variables) to move around. The shape of your maze effectively describes the program flow and the branches the variables take. It makes a lot more sense if you look at an example, here is a partial recording of a Fibonacci program running:

![A Fibonacci program running with the interpreter.](http://oliverfaircliff.com/~olls/readme-imgs/maze-interpreter/fibo.gif)

All the examples on the Esolangs wiki page work. I'm not entirely sure if the Turing complete example works correctly, because I'm not exactly sure what it is meant to do, but it doesn't enter the loop properly. See some examples in the [programs](https://github.com/olls/maze-interpreter-v2/tree/master/programs) directory.

You can get the sublime syntax highlighting package from [`sublime-maze`](https://github.com/olls/sublime-maze).

Please create an issue or pull request if you find a problem :)


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

### Extended Syntax
I have extended some of the syntax from the Esolangs Wiki to make the language a little more usable. Here is a list of the features:

#### Named signals
Signals can also be in the form `*X`, where `X` is a letter of number and the name of the signal. The `**` signal will trigger and detect all named signals, whereas named signals will only detect/trigger signals with the same name.

#### Null Direction
`%N` in a function will keep the car in the same cell for the next frame.

#### Line Out
The `>/` cell will print the value of the car with a newline appended to the end.


Behaviour
---------

The specification on the Esolangs wiki is a bit ambiguous in places, so I have had to make some assumptions:

 - The program currently generates an error and exits if two cars are in the same cell, this can be easily changed, but it is not clear from the wiki what is meant to happen.
 - The cars will attempt to move in the direction they were last travelling in first. The opposite direction to the direction they were last travelling in is always tried last. Otherwise directions are tried in this order: `U`, `R`, `D`, `L`.
 - Many start positions are allowed in the map, this is disallowed in the specification, but I included it because it allows more freedom in creating programs. Although it can be fun to make programs just one start as well.
