# LEVEL TWO A
"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be
resourceful, smart, and a quick thinker. It's not easy building a doomsday
device and capturing bunnies at the same time, after all! In order to make sure
that everyone working for her is sufficiently quick-witted, Commander Lambda
has installed new flooring outside the henchman dormitories. It looks like a
chessboard, and every morning and evening you have to solve a new movement
puzzle in order to cross the floor. That would be fine if you got to be the
rook or the queen, but instead, you have to be the knight. Worse, if you take
too much time solving the puzzle, you get "volunteered" as a test subject for
the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called
solution(src, dest) which takes in two parameters: the source square, on which
you start, and the destination square, which is where you need to land to solve
the puzzle.  The function should return an integer representing the smallest
number of moves it will take for you to travel from the source square to the
destination square using a chess knight's moves (that is, two squares in any
direction immediately followed by one square perpendicular to that direction,
or vice versa, in an "L" shape).  Both the source and destination squares will
be an integer between 0 and 63, inclusive, and are numbered like the example
chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

"""

# APPROVED SOLUTION
def getvalid(num):
    possible = []
    movesum = [-17, -15, -10, -6, 6, 10, 15, 17]
    onemovesum = [-17, -15, -6, 10, 15, 17]
    edgemovesum = [-15, -6, 10, 17]
    otheredgesum = [15, 6, -10, -17]
    otheronemove = [-17, -15, -10, 6, 15, 17]
    if num%8 == 0:
        possible = [(num + x) for x in edgemovesum]
    elif num%8 == 1:
        possible = [(num + x) for x in onemovesum]
    elif num%8 == 7:
        possible = [(num + x) for x in otheredgesum]
    elif num%8 == 6:
        possible = [(num + x) for x in otheronemove]

    else:
        possible = [(num + x) for x in movesum]
    moves = [x for x in possible if x >= 0 and x<= 63]
    return moves
def level(arr):
    content = [i for i in (getvalid(x) for x in arr)]
    oned = [j for i in content for j in i] 
    return oned
def solution(src, dest):
    if src < 0 or src > 63:
        return None
    if dest < 0 or dest > 63:
        return None
    if src == dest:
        return  0
    if dest in getvalid(src):
        return 1
    else:
        count = 1
        if dest in level(getvalid(src)):
            return count + 1
        else:
            count = 2
            again = True
            result = level(getvalid(src))
            while again == True:                
                count = count + 1
                if dest in level(result):
                    return count
                    again = False
                else:
                    result = level(result)
                    again = True

print("Hello Knight.\nHow's everything at the castle?\n\n...assumed response...\n\nOh No!!!\nYou lost your way\nDon't worry we're here to help you")
again = "Y"
while again == "Y":
    src = int(input("\n\nEnter source location: "))
    dest = int(input("Enter desired destination: "))
    if src < 0 or src > 63:
        src = int(input("Invalid input! Value must be between the range of 0 to 63 inclusive. Reenter initial location: "))
    if dest < 0 or dest > 63:
        dest = int(input("Invalid input! Value must be between the range of 0 to 63 inclusive. Reenter desired destination: "))
    moves = solution(src, dest)
    print("\nNumber of required moves: ", moves)
    again = input("\nDo you want to go again? (Y/N): ")
    again = again.upper()
print("\n\nGlad you found your way.\nWe're always happy to help\nGood-Knight! \nYes Pun Intended")
          

        
            
