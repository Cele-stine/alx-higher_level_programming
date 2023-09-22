    MORE CLASSES AND OBGECTS.
Here we get more in depth to Object Oriented Programming(OOP),covering Classmethod, Staticmethod, __str__ and __repr__etc:
In this Directory are .py files with codes that cover the Classes and Objects topics extensivly:


0-rectangle.py
An empty class that defines a rectangle

1-rectangle
Defines a rectangle with private attributes width and height

2-rectangle
Defines a rectangle as off 1-rectangle with public instance methoda area and Perimeter that calculatew the Area and the Perimater of the rectangle.

3-rectangle
Based on 2-rectangle I print a a rectangle representation of Rectanggle using str().
this is what it should look like:
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
When ./3-main.py is run(that is)

4-rectangle
Here using repr() the  string representation of the rectangle to be able to recreate a new instance by using eval() is return.
When ./4-main.py is run:
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True

5-rectangle
Using __del__() a rectangle is deleted a massage is printed aftre that
When 5-main.py is run:
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined

6-rectangle
I add a class public attribute number of instances that keeps track of the number of Rectangle instances.

7-rectangle
another public class attribute that can print Sybolic repricas of the rectangle.
Mine did work as expected it only prints the "#" character Havent figured whre i went wrong yet.
This should be the output when 7-main.py is run:
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...

8-rectangle
Here a staticmethod is introduces tha Checks through the the rectangles to check which one is bigger basecoff the area.

9-rectangle
A new class metod that creats a new rectangle instance where all sides are the same.

10-nQueens
i use the Backtracking algorithm to solve the Nqueens puzzle whwre i had to place N non-attacking Queens.
This was pretty intrestring since i has to learn the Backtracking algorithm and also how chess is played plus the role of the Queen in the chess board. i Have never played chess bytheway.
