import time
import random

tr = [' ', ' ', ' ']
mr = [' ', ' ', ' ']
br = [' ', ' ', ' ']
w = 0
l = 0
d = 0
canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
allpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
oldpos = []
gaming = input("Do you want to play Tic-Tac-Toe?\n")
if gaming.lower() == "yes":
    print(
        "\nTo play, type the coordinates of the square you'd like to play in. e.g.: 'a1' or 'c2'\n"
    )
    print('    a       b       c')
    print('        |       |')
    print('1  ', tr[0], '  |  ', tr[1], '  |  ', tr[2])
    print('  ______|_______|______')
    print('        |       |      ')
    print('2  ', mr[0], '  |  ', mr[1], '  |  ', mr[2])
    print('  ______|_______|______')
    print('        |       |      ')
    print('3  ', br[0], '  |  ', br[1], '  |  ', br[2])
    print('        |       |     \n ')
while gaming.lower() == "yes":
    haswon = False
    posplay = input("Make your move\n")
    if posplay.lower() in allpos and posplay.lower() in canpos:
        canpos.remove(posplay.lower())
        oldpos.append(posplay.lower())
        if posplay.lower() == 'a1':
            tr[0] = 'X'
        if posplay.lower() == 'a2':
            mr[0] = 'X'
        if posplay.lower() == 'a3':
            br[0] = 'X'
        if posplay.lower() == 'b1':
            tr[1] = 'X'
        if posplay.lower() == 'b2':
            mr[1] = 'X'
        if posplay.lower() == 'b3':
            br[1] = 'X'
        if posplay.lower() == 'c1':
            tr[2] = 'X'
        if posplay.lower() == 'c2':
            mr[2] = 'X'
        if posplay.lower() == 'c3':
            br[2] = 'X'
        print('\n    a       b       c')
        print('        |       |')
        print('1  ', tr[0], '  |  ', tr[1], '  |  ', tr[2])
        print('  ______|_______|______')
        print('        |       |      ')
        print('2  ', mr[0], '  |  ', mr[1], '  |  ', mr[2])
        print('  ______|_______|______')
        print('        |       |      ')
        print('3  ', br[0], '  |  ', br[1], '  |  ', br[2])
        print('        |       |      \n')
        if tr == ['X', 'X', 'X']:
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:", 100 * w / w + l + d,
                  "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if mr == ['X', 'X', 'X']:
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:", 100 * w / w + l + d,
                  "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if br == ['X', 'X', 'X']:
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if tr[0] == 'X' and mr[0] == 'X' and br[0] == 'X':
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if tr[1] == 'X' and mr[1] == 'X' and br[1] == 'X':
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if tr[2] == 'X' and mr[2] == 'X' and br[2] == 'X':
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if tr[0] == 'X' and mr[1] == 'X' and br[2] == 'X':
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if tr[2] == 'X' and mr[1] == 'X' and br[0] == 'X':
            print("Congratulations")
            haswon = True
            w = w + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        if canpos == []:
            print("It was a cat's game")
            haswon = True
            d = d + 1
            print("[Total wins:", w, ", Win percentage:",
                  100 * w / (w + l + d), "%]\n")
            gaming = input("Do you want to play again?\n")
            if gaming.lower() == "yes":
                haswon = False
                tr = [' ', ' ', ' ']
                mr = [' ', ' ', ' ']
                br = [' ', ' ', ' ']
                canpos = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
                oldpos = []
        elif haswon != True:
            time.sleep(.75)
            print("Waiting for opponent's decision...")
            time.sleep(2.5)
            aipos = random.choice(canpos)
            canpos.remove(aipos)
            oldpos.append(aipos)
            if aipos == 'a1':
                tr[0] = 'O'
            if aipos == 'a2':
                mr[0] = 'O'
            if aipos == 'a3':
                br[0] = 'O'
            if aipos == 'b1':
                tr[1] = 'O'
            if aipos == 'b2':
                mr[1] = 'O'
            if aipos == 'b3':
                br[1] = 'O'
            if aipos == 'c1':
                tr[2] = 'O'
            if aipos == 'c2':
                mr[2] = 'O'
            if aipos == 'c3':
                br[2] = 'O'
            print("Your opponent played", aipos)
            print('\n    a       b       c')
            print('        |       |')
            print('1  ', tr[0], '  |  ', tr[1], '  |  ', tr[2])
            print('  ______|_______|______')
            print('        |       |      ')
            print('2  ', mr[0], '  |  ', mr[1], '  |  ', mr[2])
            print('  ______|_______|______')
            print('        |       |      ')
            print('3  ', br[0], '  |  ', br[1], '  |  ', br[2])
            print('        |       |     \n ')
            if tr == ['O', 'O', 'O']:
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if mr == ['O', 'O', 'O']:
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if br == ['O', 'O', 'O']:
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if tr[0] == 'O' and mr[0] == 'O' and br[0] == 'O':
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if tr[1] == 'O' and mr[1] == 'O' and br[1] == 'O':
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if tr[2] == 'O' and mr[2] == 'O' and br[2] == 'O':
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if tr[0] == 'O' and mr[1] == 'O' and br[2] == 'O':
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
            if tr[2] == 'O' and mr[1] == 'O' and br[0] == 'O':
                print("You lost")
                haswon = True
                l = l + 1
                print("[Total wins:", w, ", Win percentage:",
                      100 * w / (w + l + d), "%]\n")
                gaming = input("Do you want to play again?\n")
                if gaming.lower() == "yes":
                    haswon = False
                    tr = [' ', ' ', ' ']
                    mr = [' ', ' ', ' ']
                    br = [' ', ' ', ' ']
                    canpos = [
                        'a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'
                    ]
                    oldpos = []
    elif posplay.lower() in oldpos:
        print("Error: that position has already been played in.\nTry again")
    elif posplay.lower() not in allpos:
        print("Error: that is not a position on the board.\nTry again")
print("Goodbye")