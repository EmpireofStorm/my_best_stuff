slots=["1","2","3","4","5","6","7","8","9"]
end=0
def endornot(x):
    x+=1
    yesorno = int(input('Do you want to play again? y/n'))
    if yesorno == "y":
        slots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print(slots)
        crossanddots(slots)
    else:
        print("See you again!")
        quit()
def crossanddots(slots):
    if end==1:
        slots = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("New game with 2 players")
    print("The begining")
    print("1|2|3")
    print("-|-|-")
    print("4|5|6")
    print("-|-|-")
    print("7|8|9")
    count=0
    while True:
        if count%2==0:
            print('Where do you want to place your "x"?')
            inputfromplayer = int(input())
            for i in range(0, len(slots)):
                if i==inputfromplayer:
                    slots[i-1]="x"
                    print(slots[0]+"|"+slots[1]+"|"+slots[2])
                    print("-|-|-")
                    print(slots[3]+"|"+slots[4]+"|"+slots[5])
                    print("-|-|-")
                    print(slots[6]+"|"+slots[7]+"|"+slots[8])
        count+=1
        win(slots)
        if count%2!=0:
            print('Where do you want to place your "o"?')
            inputfromplayer = int(input())
            for i in range(0, len(slots)):
                if i==inputfromplayer:
                    slots[i-1]="o"
                    print(slots[0] + "|" + slots[1] + "|" + slots[2])
                    print("-|-|-")
                    print(slots[3] + "|" + slots[4] + "|" + slots[5])
                    print("-|-|-")
                    print(slots[6] + "|" + slots[7] + "|" + slots[8])
        win(slots)



def win(slots):
    if slots[0] == slots[3] == slots[6]:
        print("Player, who placed", slots[0], "won, because he has streak of 3 at first vertical line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[1] == slots[4] == slots[7]:
        print("Player, who placed", slots[1], "won, because he has streak of 3 at second vertical line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[2]==slots[5]==slots[8]:
        print("Player, who placed", slots[2], "won, because he has streak of 3 at third vertical line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[0]==slots[1]==slots[2]:
        print("Player, who placed", slots[0], "won, because he has streak of 3 at first horizontal line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[3]==slots[4]==slots[5]:
        print("Player, who placed", slots[3], "won, because he has streak of 3 at second horizontal line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[6]==slots[7]==slots[8]:
        print("Player, who placed", slots[6], "won, because he has streak of 3 at third horizontal line")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[0]==slots[4]==slots[8]:
        print("Player, who placed", slots[0], "won, because he has streak of 3 at diagonal")
        print("The game is over")
        end=1
        endornot(0)
    elif slots[2]==slots[4]==slots[6]:
        print("Player, who placed", slots[2], "won, because he has streak of 3 at diagonal")
        print("The game is over")
        end=1
        endornot(0)

crossanddots(slots)