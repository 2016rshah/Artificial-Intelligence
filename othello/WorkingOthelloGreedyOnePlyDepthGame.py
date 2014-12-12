"""+==========================+========-========*========-========+==========================+
   ||                         WRITING AN AI FOR THE GAME OF OTHELLO                         ||
   ||  (For an electronic copy in Python 3, go to http://academics.tjhsst.edu/compsci/ai/.) ||
   ||                      by M. Stueben (Revised: December 12, 2014)                       ||
   +==========================+========-========*========-========+==========================+


THE GAME OTHELLO. Othello (aka Reversi) is a game played by two players on a board with 8 rows and 8 columns
and a set of pieces that can change color during the game. The pieces (aka stones and tiles) are white on one
side and black on the other side. Players alternate placing pieces of their color on an 8 x 8 board. The Human
(BLACK) moves first vs. Computer (WHITE).

   If a row, column, or diagonal of consecutive pieces (no blanks) all of the same color becomes flanked
(touched on both ends) by two pieces of the opposite color (one of them being the piece just played, then the
pieces in between are turned over and all become pieces of the boundary color. Hence, the original name
"Reversi." In fact, every legal move MUST turn the color of some of the opponent's pieces. Below White makes a
legal move and turns three black pieces into three white pieces.

                    ......W...         ..........         ......W...
                    ..BBBWBW..    -->  .WBBBWBW..    -->  .WWWWWBW..
                    ......W...         ..........         ......W...
                  White to move        White moves         Result

   If one of the three left-most black pieces (B) was replaced by an empty      +----------------------+
cell, White's move would have been illegal, because no black piece would       1|.  .  .  .  .  .  .  .|
have changed color. If a player cannot legally move, he or she must pass       2|.  .  .  .  .  .  .  .|
the move to the opponent. The game ends when neither player can legally        3|.  .  .  =  .  .  .  .|
move. This usually occurs because the board fills up.                          4|.  .  =  W  B  .  .  .|
                                                                               5|.  .  .  B  W  =  .  .|
   Othello has a fixed starting position, but Reversi does not. See            6|.  .  .  .  =  .  .  .|
diagram. Reversi players use a common pool of 64 pieces, but each Othello      7|.  .  .  .  .  .  .  .|
player has his own pile of 32 pieces. If an Othello player plays his final     8|.  .  .  .  .  .  .  .|
piece--his opponent having passed the move on at least one occasion--the        +----------------------+
player with pieces can finish making legal moves anyway he wants. Othello        a  b  c  d  e  f  g  h
is copyrighted (1973), Reversi (invented prior to 1886) is not. Otherwise,
the games are identical. Since 1977, there has been an Othello world championship.

   In the above diagram, it is always Black to make his first move. Since a legal move must bound consecutive
pieces of the opposite color, Black has only four legal moves: c4, d3, e6, and f5. These positions are in-
dicated by equal signs. In fact, these four moves all lead to the same geometric position either mirrored, or
rotated 180 degrees, or both. So Black's first move is already known by his opponent.

A note on Python's Tk graphics:
     1) The command exit() seems to cause errors in Tk graphics.
     2) Tk graphics commands with syntax errors often do NOT stop the program from running. But they
        do print error messages to the console window.
     3) Global variables are REQUIRED in Python's Tk graphics.                      +----------------+
     4) A global variable, say M, cannot be modified unless the word "global"       |  def doit():   |
        appears on the first line of a function. (I made this mistake several       |      global M  |
        times in writing this program. Argg!) After the word global the list        +----------------+
        of global variables must follow. See the example on the right.
     5) This program was written for my Windows laptop. If your OS is not Windows, then the size of the fonts
        will be slightly different, and the Othello board may not fill the screen. Cross-platform development
        if difficult.
     6) Two useful text characters (used in this program) are character 9679 a solid disk, and character
        9608 a solid rectangle.

ASSIGNMENT: Given this working game of Othello (human (black) vs. computer (white)), write a better strategy.
            But first ...

            1. We want the program to display black's legal moves with the number of white pieces that would
               be turned over if black (the human) chooses any candidate move. In fact the code to do this
               exists in the program. It has just been turned off. Turn it back on.
            2. The numbers displayed to help black choose his move are 'BLACK' and of a small font height.
               Make them 'GOLD' and twice as large.
            3. The program should print the current number of white tiles and black tiles, but somehow the
               scores are always the same. Fix this.
            4. The function copyMatrixToScreen() violates the design principle DRY (don't repeat yourself).
               Fix it. Also, print a DARKGREEN rectangle over the cell to erase the previous numbers (if any)
               that were printed to the cell.
            5. Take a look at the computer's strategy. One way to make the program  considerably stronger is
               to have occupy a corner whenever one is available. Make this change.
            6. The computer uses the greedy strategy. This is usually a pretty good strategy, although rarely
               the optimal strategy. Another reason it is popular is that it is conceptually easy to under-
               stand and then code. Since we are beginners, we will settle for all the experience we can get
               with this simple strategy. The problem is that the computer is just too simple-minded. It just
               looks for the cell that picks up the most points (1-ply depth). Instead, we should make it
               2-ply depth. For each of the computer's legal moves, it should calculate the maximum score
               MINUS the maximum score that will be obtained by the human's best reply. In fact, somewhere in
               this program is a function called bestHumanResponse() based on the simple greedy strategy that
               the computer currently uses. Your job is to change the computer's current strategy from 1-ply
               to 2-ply, using the current bestHumanResponse() function.
            7. Change the bestHumanResponse() function to a 2-ply search. Wait! See the next task.
            8. Notice that the initial bestHumanResponse(), and the initial makeComputerReply() functions are
               identical. The program has violated the design principle DRY (don't repeat yourself). Combine
               them into ONE function. If you look through this program you will see several functions that
               work with both the computer's move and the human's move. The simple design of these unisex
               functions may guide you. Good luck.
                                                     * *
What's next? Answer: THE MINIMAX ALGORITHM with ALPHA-BETA PRUNING. Read about this on the Internet and then
               modify the computer's strategy to go 3- or 4-ply deep. This will make the program tough for a
               human to beat. (We can't apply 3-4 ply thinking yet, because it would make the computer's move
               too slow.) BTW assume 12 possible replies for each of the next 4 moves. Then each ply increases
               the time my a factor of 12. The computer must evaluate 12^4 = 20736 positions to determine its
               best 4-ply move. If each evaluation (4-ply deep) takes only 0.00000964 seconds, then the move
               will be determined in 2 seconds.
"""
##############################################<START OF PROGRAM>##############################################

def setUpCanvas(root): # These are the REQUIRED magic lines to enter graphics mode.
    root.title("A Tk/Python Graphics Program") # Your screen size may be different from 1270 x 780.
    canvas = Canvas(root, width = 1270, height = 780, bg = 'GREY30')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas
#----------------------------------------------------------------------------------------------------Othello--

def createMatrix(): # = the initial position, with BLACK = 1, and WHITE = -1.
    global M
    M = [ [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0,-1, 1, 0, 0, 0,], # The matrix M is GLOBAL.
          [0, 0, 0, 1,-1, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],
          [0, 0, 0, 0, 0, 0, 0, 0,],]
    return M
#----------------------------------------------------------------------------------------------------Othello--

def initializePointMatrices():
    global PW, PB
##--The computer's strategy will be based off of this GLOBAL matrix, which will be modified as
#   the board configuration changes. Remember: row (going down) is first:  P[row][col]
    PW = [ [1000,   50,  100,  100,  100,  100,   50, 1000,], # P[0][0], P[0][1], ..., P[0][7]
           [  50,  -20,  -10,  -10,  -10,  -10,  -20,   50,], # P[1][0], P[1][1], ..., P[1][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[2][0], P[2][1], ..., P[2][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[3][0], P[3][1], ..., P[3][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[4][0], P[4][1], ..., P[4][7]
           [ 100,  -10,    1,    1,    1,    1,  -10,  100,], # P[5][0], P[5][1], ..., P[5][7]
           [  50,  -20,  -10,  -10,  -10,  -10,  -20,   50,], # P[6][0], P[6][1], ..., P[6][7]
           [1000,   50,  100,  100,  100,  100,   50, 1000,],]# P[7][0], P[7][1], ..., P[7][7]
    from copy import deepcopy
    PB = deepcopy(PW)
    return PW, PB
#----------------------------------------------------------------------------------------------------Othello--

def updateTheFourCorners():
    global PW, PB
#---1B. Modify upper-left corner cell's values if the HUMAN has taken that corner.
    if M[0][0] == 1:
        PW[0][1] = -50
        PW[1][0] = -200
        PW[1][1] = -50
        PB[0][1] = 100
        PB[1][0] = 100
        PB[1][1] = 100

#---2B. Modify upper-right corner cell's values if the HUMAN has taken that corner.
    if M[0][7] == 1:
        PW[0][6] = -50
        PW[1][7] = -200
        PW[1][6] = -50
        PB[0][6] = 100
        PB[1][7] = 100
        PB[1][6] = 100

#---3B. Modify lower-left corner cell's values if the HUMAN has taken that corner.
    if M[7][0] == 1:
        PW[6][0] = -50
        PW[6][1] = -200
        PW[7][1] = -50
        PB[6][0] = 100
        PB[6][1] = 100
        PB[7][1] = 100

#---4B. Modify lower-right corner cell's values if the HUMAN has taken that corner.
    if M[7][7] == 1:
        PW[7][6] = -50
        PW[6][7] = -200
        PW[6][6] = -50
        PB[7][6] = 100
        PB[6][7] = 100
        PB[6][6] = 100

#---1W. Modify upper-left corner cell's values if the COMPUTER has taken that corner.
    if M[0][0] == -1:
        PW[0][1] = 100
        PW[1][0] = 100
        PW[1][1] = 100
        PB[0][1] = -50
        PB[1][0] = -200
        PB[1][1] = -50

#---2W. Modify upper-right corner cell's values if the COMPUTER has taken that corner.
    if M[0][7] == -1:
        PW[0][6] = 100
        PW[1][7] = 100
        PW[1][6] = 100
        PB[0][6] = -50
        PB[1][7] = -200
        PB[1][6] = -50

#---3W. Modify lower-left corner cell's values if the COMPUTER has taken that corner.
    if M[7][0] == -1:
        PW[6][0] = 100
        PW[6][1] = 100
        PW[7][1] = 100
        PB[6][0] = -50
        PB[6][1] = -200
        PB[7][1] = -50

#---4W. Modify lower-right corner cell's values if the COMPUTER has taken that corner.
    if M[7][7] == -1:
        PW[7][6] = 100
        PW[6][7] = 100
        PW[6][6] = 100
        PB[7][6] = -50
        PB[6][7] = -200
        PB[6][6] = -50
#----------------------------------------------------------------------------------------------------Othello--

def updateTheMiddleRowsAndColumns():
    global PB, PW
    for n in range (2, 6):
        if M[0][n] == -1:
            PW[1][n] =  20 # TOP    row
            PB[1][n] = -10 # TOP    row
        if M[7][n] == -1:
            PW[6][n] =  20 # BOTTOM row
            PB[6][n] = -10 # BOTTOM row
        if M[n][0] == -1:
            PW[n][1] =  20 # LEFT  column
            PB[n][1] = -10 # LEFT  column
        if M[n][7] == -1:
            PW[n][6] =  20 # RIGHT column
            PB[n][6] = -10 # RIGHT column
        if M[0][n] == 1:
            PW[1][n] = -10 # TOP    row
            PB[1][n] =  20 # TOP    row
        if M[7][n] == 1:
            PW[6][n] = -10 # BOTTOM row
            PB[6][n] =  20 # BOTTOM row
        if M[n][0] == 1:
            PW[n][1] = -10 # LEFT  column
            PB[n][1] =  20 # LEFT  column
        if M[n][7] == 1:
            PW[n][6] = -10 # RIGHT column
            PB[n][6] =  20 # RIGHT column
#----------------------------------------------------------------------------------------------------Othello--

def UpdateThePointMatrices():
    updateTheFourCorners()
    updateTheMiddleRowsAndColumns()
#----------------------------------------------------------------------------------------------------Othello--

def copyMatrixToScreen():# This is where the pieces are played on the screen and flipped.
    canvas.create_text(30,30, text="x", fill = 'BLACK', font = ('Helvetica',1))
    for r in range (8):
       for c in range (8):
           sx = c*70 +  85
           sy = r*70 + 105
           if M[r][c] ==  1:
              canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'BLACK')
           elif M[r][c] == -1:
              canvas.create_oval(sx-25,sy-25, sx+25, sy+25, fill = 'WHITE')
           else:
              canvas.create_oval(sx-25,sy-25, sx+25, sy+25, outline='DARKGREEN',fill = 'DARKGREEN')
    canvas.update()
#----------------------------------------------------------------------------------------------------Othello--

def copyOldBoardToScreenInMiniturizedForm(cc, rr):
 #--erase previous miniture board
    canvas.create_rectangle(650, 400, 821, 567, width = 5, fill    = 'GRAY30')
    ch = chr(9679)
    for r in range (8):
       for c in range (8):
        sx = c*20 + 665
        sy = r*20 + 412
        if M[r][c] ==  1:
           canvas.create_text(sx, sy, text = ch, fill = 'BLACK', font = ('Helvetica', 20, 'bold') )
        if M[r][c] == -1:
           canvas.create_text(sx, sy, text = ch, fill = 'WHITE', font = ('Helvetica', 20, 'bold') )

    canvas.create_text(cc*20 + 665, rr*20 + 413, text = 'B', fill = 'BLACK', font = ('Helvetica', 9, 'bold') )
    canvas.update()      # make all previous changes to the canvas
#----------------------------------------------------------------------------------------------------Othello--

def score(): # returns the number of black and white disks on the board.
    whiteTotal = 0; blackTotal = 0
    for r in range(8):
      for c in range (8):
        if M[r][c] ==  1: blackTotal += 1
        if M[r][c] == -1: whiteTotal += 1
    return (whiteTotal, whiteTotal)
#----------------------------------------------------------------------------------------------------Othello--

def printMatrices(): # <-- This function prints the matrices M, PB, and PW to the console for debugging.
    return           # Printing is slow, so we disable this function.
    print('\n Matrix M')
    print ('     0  1  2  3  4  5  6  7')
    print ('  +--------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         if M[r][c] == 1: ch = '#'
         if M[r][c] ==-1: ch = 'O'
         if M[r][c] == 0: ch = '-'
         if M[r][c] not in {-1,0,1}: ch = '?'
         print ("%3s"%ch, end = '')
      print ("  |")
    print ('  +--------------------------+')
    print ('  |human    = # = BLACK  =  1|')
    print ('  |computer = O = WHITE  = -1|')
    print ('  +--------------------------+')
    print ('M[3][0] =', M[3][0])
#   ------------------------------------------------
    print('\n Matrix PW')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%PW[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#   ------------------------------------------------
    print('\n Matrix PB')
    print ('      0    1    2    3    4    5    6    7')
    print ('  +------------------------------------------+')
    for r in range(8):
      print (r, '|', end = '')
      for c in range (8):
         print ("%5d"%PB[r][c], end = '')
      print ("  |")
    print ('  +------------------------------------------+')
#----------------------------------------------------------------------------------------------------Othello--

def LocateTurnedPieces(r, c, player): # The pieces turned over are of -player's color. A zero in a matrix M
    if M[r][c] != 0: return []        # cell means an empty cell. This function does NOT turn any pieces over.
    totalFlipped =   []
 #--case 1 (move right)
    flipped = []
    if c < 6 and M[r][c+1] == -player:
        for n in range(1, 9):
            if c+n > 7 or M[r][c+n] == 0:
                flipped = []
                break
            if M[r][c+n] == player: break
            flipped += ((r,c+n,),)  # <-- We save the cell locations as tuples.
    totalFlipped += flipped

 #--case 2 (move down)
    flipped = []
    if r < 6 and M[r+1][c] == -player:
        for n in range(1, 9):
            if r+n > 7 or M[r+n][c] == 0:
                flipped = []
                break
            if M[r+n][c] == player: break
            flipped += ((r+n,c,),)
    totalFlipped += flipped

 #--case 3 (move up)
    flipped = []
    if r > 1 and M[r-1][c  ] == -player:
        for n in range(1, 9):
            if r-n < 0 or M[r-n][c] == 0:
                flipped = []
                break
            if M[r-n][c] == player: break
            flipped += ((r-n,c,),)
    totalFlipped += flipped

 #--case 4 (move left)
    flipped = []
    if c > 1 and M[r][c-1] == -player:
        for n in range(1, 9):
            if c-n < 0 or M[r][c-n] == 0:
                flipped = []
                break
            if M[r][c-n] == player: break
            flipped += ((r,c-n,),)
    totalFlipped += flipped

 #--case 5 (move down and right)
    flipped = []
    if r < 6 and c < 6 and M[r+1][c+1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c+n) > 7 or M[r+n][c+n] == 0:
                flipped = []
                break
            if M[r+n][c+n] == player: break
            flipped += ((r+n,c+n,),)
    totalFlipped += flipped

 #--case 6 (move up and left)
    flipped = []
    if r > 0 and c > 0 and M[r-1][c-1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c-n) < 0 or M[r-n][c-n] == 0:
                flipped = []
                break
            if M[r-n][c-n] == player: break
            flipped += ((r-n,c-n,),)
    totalFlipped += flipped

#--case 7 (move up and right)
    flipped = []
    if r > 1 and c < 6 and M[r-1][c+1] == -player:
        for n in range(1, 9):
            if (r-n) < 0 or (c+n) > 7 or M[r-n][c+n] == 0:
                flipped = []
                break
            if M[r-n][c+n] == player: break
            flipped += ((r-n,c+n,),)
    totalFlipped += flipped

 #--case 8 (move down and left)
    flipped = []
    if r < 6 and c > 1 and M[r+1][c-1] == -player:
        for n in range(1, 9):
            if (r+n) > 7 or (c-n) < 0 or M[r+n][c-n] == 0:
                flipped = []
                break
            if M[r+n][c-n] == player: break
            flipped += ((r+n,c-n,),)
    totalFlipped += flipped

    return totalFlipped
#----------------------------------------------------------------------------------------------------Othello--

def printInitialBoardAndDirectionsToScreen(canvas):
    global M; ch = chr(9679) # This character (9679) is the solid disk. 9608 is a solid rectangle.

 #--print title
    canvas.create_text(330, 50, text = "OTHELLO with AI", fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
 #--print directions
    stng = "DIRECTIONS:\n1) Black (human) moves first. Click on any unoccupied cell.\n\
2) If a player cannot move, play passes to the opponent. \n3) Game ends when \
no legal move is possible.\n4) The player with the most colors on the board \
wins.\n5) A legal move MUST cause some pieces to turn color."
    canvas.create_text(810, 100, text = stng, fill = 'WHITE',  font = ('Helvetica', 10, 'bold'))
 #--draw outer box, with red border
    canvas.create_rectangle(50, 70, 610, 630, width = 1, fill    = 'DARKGREEN')
    canvas.create_rectangle(47, 67, 612, 632, width = 5, outline = 'RED'  )

 #--Draw 7 horizontal and 7 vertical lines to make the cells
    for n in range (1, 8): # draw horizontal lines
       canvas.create_line(50, 70+70*n, 610, 70+70*n, width = 2, fill = 'BLACK')
    for n in range (1, 8):# draw vertical lines
       canvas.create_line(50+70*n,  70, 50+70*n, 630, width = 2, fill = 'BLACK')

 #--Place gold lines to indicate dangerous area to play (optional).
    canvas.create_rectangle(47+73, 67+73, 612-73, 632-73, width = 1, outline = 'GOLD'  )
    canvas.create_rectangle(47+2*71, 67+2*71, 612-2*71, 632-2*71, width = 1, outline = 'GOLD'  )

 #--Place letters at bottom
    tab = " " * 7
    stng = 'a' + tab + 'b' + tab + 'c' + tab + 'd' + tab + 'e' + tab + 'f' + tab + 'g' + tab + 'h'
    canvas.create_text(325, 647, text = stng, fill = 'DARKBLUE',  font = ('Helvetica', 20, 'bold'))

 #--Place digits on left side
    for n in range (1,9):
        canvas.create_text(30, 35 + n * 70, text = str(n), fill = 'DARKBLUE', font =('Helvetica', 20, 'bold'))
 #--copy matrix to screen.
    copyMatrixToScreen()

 #--Place score on screen
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))
    stng = "Suggested reply (col, row): (c, 4)"
    canvas.create_text     (755,350,text = stng, fill = 'GREEN',  font = ('Helvetica', 10, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def illegalClick(x, y): # Click is not on board or click is on an already-filled cell.
    player = 1 # player = Black
    if x < 52 or x > 609:
        print("Error 1. Mouse is to left or right of board.")
        return True # = mouse position is off the board

    if y < 62 or y > 632:
        print("Error 2.Mouse is above or below the board.")
        return True # = mouse position is off the board

 #--Calculate matrix position
    c = (x-50)//70
    r = (y-70)//70

    if M[r][c] != 0:
        print("ERROR 3: Cell is occupied at r =", r, " c =", c)
        return True      # = cell is occupied

 #--Not next to cell of opposite color
    flag = 0
    if c < 7 and           M[r  ][c+1] == -player: return False
    if r < 7 and           M[r+1][c  ] == -player: return False
    if r > 0 and           M[r-1][c  ] == -player: return False
    if c > 0 and           M[r  ][c-1] == -player: return False
    if r < 7 and c < 7 and M[r+1][c+1] == -player: return False
    if r > 0 and c > 0 and M[r-1][c-1] == -player: return False
    if r > 0 and c < 7 and M[r-1][c+1] == -player: return False
    if r < 7 and c > 0 and M[r+1][c-1] == -player: return False
    print("ERROR 4: no opposite colored neighbors at r =", r, " c =", c)
    return True # = illegal move
#----------------------------------------------------------------------------------------------------Othello--

def legalMove(player): # Check to see if any pieces will be turned over. A list comprehension will be faster.
    pieces = []
    for r in range(8):
        for c in range(8):
           pieces += LocateTurnedPieces(r, c, player)
        if pieces != []: break
    if pieces ==[]:
       person = 'WHITE'
       if player == 1: person = 'BLACK'
       stng = 'There is no legal move for ' + person
       canvas.create_rectangle(655,260,957,307, width = 0, fill = 'GRAY30')
       canvas.create_text     (800,280,text = stng, fill = 'RED',  font = ('Helvetica', 10, 'bold'))
       return False
    return True
#----------------------------------------------------------------------------------------------------Othello--

def makeMove(c, r, pieces, player):
    global M
    if player not in [1, -1]: exit('ERROR: BAD PLAYER'+ str(player))
 #--make the player's legal move in matrix
    M[r][c] = player

 #--flip pieces to same color as the player
    for elt in pieces:
        M[elt[0]][elt[1]] = player

#--update the screen
    copyMatrixToScreen()

 #--erase old score and previous move
    canvas.create_rectangle(650, 160, 960, 310, width = 5, fill    = 'GRAY30')

 #--print new score
    (BLACK, WHITE) = score()
    stng = 'BLACK = ' + str(BLACK) + '\nWHITE  = ' + str(WHITE)
    canvas.create_text(800, 200, text = stng, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

 #--print previous move on miniture board
    position = "previous move: "+ str(chr(c + 97))+str(r+1)
    canvas.create_text(800, 250, text = position, fill = 'WHITE',  font = ('Helvetica', 20, 'bold'))

    if player == COMPUTER:
       canvas.create_text(c*20 + 665, r*20 + 413, text = 'W', fill = 'WHITE', font = ('Helvetica', 9, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def quit(): # exit() will not work with Tkinter graphics.
    canvas.create_text(330, 350, text = "GAME OVER", \
                       fill = 'RED',  font = ('Helvetica', 40, 'bold'))
    stng = 'THERE ARE NO LEGAL MOVES FOR EITHER PLAYER.'
    canvas.create_rectangle(655, 260, 955, 300, width = 0, fill = 'GRAY30')
    canvas.create_text(805, 280, text = stng, fill = 'GOLD',  font = ('Helvetica', 9, 'bold'))
#----------------------------------------------------------------------------------------------------Othello--

def totalPointsGainedFromFlippingPieces(player, r,c, pieces):
    if player == COMPUTER:
       total = PW[r][c]          # total = the points associated with the piece played on the board.
       for (rr,cc) in pieces:
           total += 2*PW[rr][cc] # Add the values associated with the flipped pieces.
       return total
    if player == HUMAN:
       total = PB[r][c]          # total = the points associated with the piece played on the board.
       for (rr,cc) in pieces:
           total += 2*PB[rr][cc] # Add the values associated with the flipped pieces.
       return total
    exit('ERROR in totalPointsGainedFromFlippingPieces() player = ' + str(player))
#----------------------------------------------------------------------------------------------------Othello--

def makeComputerReply():
    UpdateThePointMatrices()
#--Make a move that picks up the most points using the point matrix (PW).
    bestRow = -1
    bestCol = -1
    maxTotal = float('-inf')
    for r in range(0, 8):
        for c in range(0, 8):
           if M[r][c] == 0:
              pieces = LocateTurnedPieces(r, c, COMPUTER)
              if len(pieces) == 0:
                 continue
              total = totalPointsGainedFromFlippingPieces(COMPUTER, r, c, pieces)
              if maxTotal < total:
                 maxTotal = total
                 bestRow  = r
                 bestCol  = c
                 finalPieces = pieces
    makeMove(bestCol, bestRow, finalPieces, COMPUTER)
#   printBestPotentialReply(COMPUTER) # <--Optional feature
#----------------------------------------------------------------------------------------------------Othello--

def displayAllLegalMovesForHumanPlayer(kolor):
    for r in range(0, 8):
        for c in range(0, 8):
           if M[r][c] == 0: # an empty cell contains a zero integer.
              total  = len(LocateTurnedPieces(r, c, HUMAN))
           if M[r][c] == 0 and total != 0:
              sy = r*70 + 109
              sx = c*70 + 85
              canvas.create_text( sx, sy, text = str(total), fill = kolor, font = ('Helvetica', 10, 'bold') )
#----------------------------------------------------------------------------------------------------Othello--

def click(evt): # A legal move is guaranteed to exist. Note evt = (evt.x, evt.y) = mouse screen coordinates.
    printMatrices()

 #--If move is off board, or cell full, or no opp. neighbor, then CLICK AGAIN.
    if illegalClick(evt.x, evt.y):
        canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
        stng = 'Your last mouse click was an ILLEGAL MOVE.'
        canvas.create_text(800, 280, text = stng, fill = 'RED',  font = ('Helvetica', 9, 'bold'))
        return

 #--Find matrix coordinates (c,r) in terms of mouse coordinates (evt.x, evt.y).
    c = (evt.x-50)//70
    r = (evt.y-70)//70

 #--if none of the computer's pieces will be turned, then CLICK AGAIN.
    pieces     = LocateTurnedPieces(r, c, HUMAN)
    if pieces == []:
       canvas.create_rectangle(660, 270, 940,300, width = 0, fill = 'GRAY30')
       stng = 'Your last mouse click did NOT turn a piece.'
       canvas.create_text(800, 280, text = stng, fill = 'ORANGE',  font = ('Helvetica', 9, 'bold'))
       return

 #--Make human move(s) and computer reply/replies.
    copyOldBoardToScreenInMiniturizedForm(c,r)
    makeMove(c, r, pieces, HUMAN)
    canvas.create_rectangle(655, 330, 870,370, width = 0, fill = 'grey30')
    if legalMove(HUMAN) and not legalMove(COMPUTER): return

 #--Make computer reply/replies (1 = BLACK = human, -1 = computer = WHITE)
    if legalMove(COMPUTER): makeComputerReply() # <--This is the computer's strategy (IMPORTANT!).
    while legalMove(COMPUTER) and not legalMove(HUMAN):
        makeComputerReply()
    #displayAllLegalMovesForHumanPlayer('BLACK')

    if not legalMove(HUMAN) and not legalMove(COMPUTER): quit()
 #-- Note: legal move for human must now necessarily exist.
    return
#----------------------------------------------------------------------------------------------------Othello--

def bestHumanResponse():
    UpdateThePointMatrices()
#--Make a move that picks up the most points using the point matrix (PB).
    bestRow = -1
    bestCol = -1
    maxTotal = float('-inf')
    for r in range(0, 8):
        for c in range(0, 8):
           if M[r][c] == 0:
              pieces = LocateTurnedPieces(r, c, HUMAN)
              if len(pieces) == 0:
                 continue
              total = totalPointsGainedFromFlippingPieces(HUMAN, r, c, pieces)
              print
              if maxTotal < total:
                 maxTotal = total
                 bestRow = r
                 bestCol = c
                 finalPieces = pieces
    return maxTotal, bestRow, bestCol
#===================================<GLOBAL CONSTANTS and GLOBAL IMPORTS>=====================================

# Global Variables should be avoided. But in Python's Tk graphics this is impossible.
from tkinter  import *   # <-- Use "Tkinter" in Python 2.x
root     =  Tk()
canvas   =  setUpCanvas(root)
PW, PB   =  initializePointMatrices()
M        =  createMatrix() # <-- No variable can be passed to the click function.
HUMAN    =  1 # = Black
COMPUTER = -1 # = White
GLOBAL   = True
#====================================================<MAIN>===================================================

def main():
    root.bind('<Button-1>', click) # 1 = LEFT  mouse button.
    root.bind('<Button-3>', click) # 3 = RIGHT mouse button.
    printInitialBoardAndDirectionsToScreen (canvas)
    root.mainloop()                # Now the graphics window waits for the click function to be called.
#----------------------------------------------------------------------------------------------------Othello--
if __name__ == '__main__':  main()
###############################################<END OF PROGRAM>###############################################