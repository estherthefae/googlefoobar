# LEVEL TWO B
"""
Bunny Worker Locations
======================

Keeping track of Commander Lambda's many bunny workers is starting to get tricky.
You've been tasked with writing a program to match bunny worker IDs to cell
locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's
space station, and as a result the work areas have an unusual layout. They are
stacked in a triangular shape, and the bunny workers are given numerical IDs
starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from
the vertical wall, and y being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2)
has ID 9, and the bunny worker at (2,3) has ID 8. This pattern of numbering
continues indefinitely (Commander Lambda has been adding a LOT of workers). 

Write a function solution(x, y) which returns the worker ID of the bunny at
location (x, y). Each value of x and y will be at least 1 and no greater than
100,000. Since the worker ID can be very large, return your solution as a string
representation of the number.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(3, 2)
Output:
    9

Input:
Solution.solution(5, 10)
Output:
    96

-- Python cases --
Input:
solution.solution(5, 10)
Output:
    96

Input:
solution.solution(3, 2)
Output:
    9
"""


#APPROVED SOLUTIONS
"""
Both of the solutions passed the test cases but I only had the chance to submit
one solution and test again the hidden test cases so I submitted the more
optimal one.
Each function has a timer so when you run every test case, you find out how long
it takes for both functions and you see the optimization in question
"""
import time
def answer(x, y):
    start = time.time()
    num = 1
    diff = 1
    for i in range(y-1):
        num = num + diff
        diff = diff + 1
    for i in range(x-1):
        y = y  + 1
        num = num+ y
    end = time.time()
    return str(num), end-start
def solution(x, y):
    start = time.time()
    cornernum = 1
    if y%2 == 0:
        cornernum += (y/2) * (y-1)
    elif y%2 == 1:
        cornernum += (y-1) + ((y-2) * ((y-1)/2))
    if x%2 == 0:
        result = cornernum + ((y+1) * (x-1)) + ((x-2) + ((x-3) * ((x-2)/2)))
    elif x%2 == 1:
        result = cornernum + ((y+1) * (x-1)) + (((x-1)/2) * (x-2))
    end = time.time()
    return str(result), end - start
print("Hello there\nWelcome to my program\nI hear you want to find worker IDs")
print("\nYou're in the right place")
print("Just enter the coordinates and the ID would be located")
x = int(input("\nEnter x coordinate: "))
y = int(input("Enter y coordinate: "))        
id, timetaken = solution(x, y)
id2, time2 = answer(x,y)
print("\nID FOUND\nWorker ID: ", id)
print("\nTime taken for answer function: ", time2)
print("Time taken for solution function: ", timetaken)
print("\nThanks for using our service.\nAlways remember:\n" +
      "A person without identity is a NONENTITY")
