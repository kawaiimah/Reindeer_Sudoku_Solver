"""

Solves a Reindeer Sudoku array where ' ' is placeholder for unknown letters 

"""

import sys

# Set puzzle
df = []
print('\nSelect puzzle:-')
print('1. BLIZEM')
print('2. DASHER')
print('3. DANCER')
print('4. SLEIGH')
choice = input('Your choice? ')

if choice == '1':
    rd = ['B','L','I','X','E','M']
    df.append('  E   ')
    df.append('  M  X')
    df.append('L  B  ')
    df.append(' B   M')
    df.append('  L   ')
    df.append('   M E')
elif choice == '2':
    rd = ['D','A','S','H','E','R']
    df.append('    R ')
    df.append(' S    ')
    df.append(' H E  ')
    df.append('    A ')
    df.append('R    S')
    df.append(' AE H ')
elif choice == '3':
    rd = ['D','A','N','C','E','R']
    df.append(' C    ')
    df.append('N  D  ')
    df.append('C    N')
    df.append('ED    ')
    df.append('      ')
    df.append('AE  CD')
elif choice == '4':
    rd = ['S','L','E','I','G','H']
    df.append('S     ')
    df.append(' GIS  ')
    df.append('    S ')
    df.append('G  H  ')
    df.append('    LE')
    df.append('   G  ')
else:
    sys.exit()

# Import letters into array
ary = []
for i in range(6):
    temp = []
    for c in df[i]:
        temp.append(c)
    ary.append(temp)

# Show user the array and check if ok to proceed
print('\nChosen puzzle:')
for i in range(6):
    print(ary[i])
if input('Proceed to solve? ').lower() != "y":
    sys.exit()


# Set up helper functions for recursive solving
def possible(y,x,n):

    # This function checks if it is possible for n to be at position y,x
    
    global ary
   
    # Check if n already exists in the same column or row
    for i in range(6):
        if ary[y][i]==n or ary[i][x]==n:
            return False

    # Check if n already exists in the 3x2 block
    x0 = (x//3)*3
    y0 = (y//2)*2
    for i in range(3):
        for j in range(2):
            if ary[y0+j][x0+i]==n:
                return False

    return True


def solve():

    # Main recursive function that steps thru the array looking for ' ',
    # tries n from rd (which contains the full reindeer name) in that position,
    # then calls itself again for the rest of the array
    
    global ary

    for y in range(6):
        for x in range(6):
            if ary[y][x]==' ':
                for n in rd:
                    if possible(y,x,n):
                        ary[y][x] = n
                        solve()
                        ary[y][x] = ' '
                return

    # Prints solution once no more ' 's are found
    for i in range(6):
        print(ary[i])


# Take a deep breath, start the ball rolling!
solve()