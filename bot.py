import math

NUMBAT = input("Number of batteries: ")
NUMHOLD = input("Number of battery holders: ")
SERIAL_NUMBER = input("Serial number: ")

done = False
indicators = []
while True: #Gathering the indicators
    indicator = input("Input indicators: (FRKunlit / CARlit) / done:")
    if indicator.lower() == "done":
        break
    else:
        indicators.append(indicator)

def solveWires(): # -----------------------WIRE-------------------------------- 
    done = False
    wires = []
    while True: #Getting the wires
        wire = input("Input wires in order (w/bk/bl/r/y)/done: ")
        if wire.lower() == "done":
            break
        else:
            wires.append(wire)

    if len(wires) == 3: #if there are 3 wires

        redwirePresent = False
        for wire in wires:
            if wire.lower() == "r":
                redwirePresent = True
                break

        if redwirePresent == False:
            print("Cut the second wire.")
            return

        if wires[2].lower() == "w":
            print("Cut the last wire.")
            return

        bluewirecount = 0
        for wire in wires:
            if wire.lower() == "bl":
                bluewirecount = bluewirecount + 1
        if bluewirecount > 1:
            print("Cut the last blue wire.")
            return

        print("Cut the last wire.")
        return

    if len(wires) == 4: #If there are 4 wires

        bluewirecount = 0
        yellowwirecount = 0
        redwirecount = 0
        for wire in wires:
            if wire.lower() == "r":
                redwirecount = redwirecount + 1
            elif wire.lower() == "bl":
                bluewirecount = bluewirecount + 1
            elif wire.lower() == "y":
                yellowwirecount = yellowwirecount + 1



        if redwirecount > 1 and (int(SERIAL_NUMBER[5])+1) % 2 == 0:
            print("Cut the last red wire.")
            return

        if wires[3].lower() == 'y' and redwirecount == 0:
            print("Cut the first wire.")
            return

        if bluewirecount == 1:
            print("Cut the first wire.")
            return

        if yellowwirecount > 1:
            print("Cut the last wire.")
            return

        print("Cut the second wire.")
        return

    if len(wires) == 5: #If there are 5 wires
        redwirecount = 0
        yellowwirecount = 0
        blackwirecount = 0
        for wire in wires:
            if wire.lower() == "r":
                redwirecount = redwirecount + 1
            elif wire.lower() == "y":
                yellowwirecount = yellowwirecount + 1
            elif wire.lower() == "bk":
                blackwirecount = blackwirecount + 1

        if wires[4].lower() == "bk" and (int(SERIAL_NUMBER[5])+1) % 2 == 0:
            print("Cut the fourth wire.")
            return
        
        if redwirecount == 1 and yellowwirecount > 1:
            print("Cut the first wire.")
            return

        if blackwirecount == 0:
            print("Cut the second wire.")
            return

        print ("Cut the first wire.")
        return

    if len(wires) == 6: #If there are 6 wires
        yellowwirecount = 0
        redwirecount = 0
        whitewirecount = 0
        for wire in wires:
            if wire.lower() == "y":
                yellowwirecount = yellowwirecount + 1
            elif wire.lower() == "r":
                redwirecount = redwirecount + 1
            elif wire.lower() == "w":
                whitewirecount = whitewirecount + 1

        if yellowwirecount == 0 and (int(SERIAL_NUMBER[5])+1) % 2 == 0:
            print("Cut the fourth wire.")
            return

        if yellowwirecount == 1 and whitewirecount > 1:
            print("Cut the fourth wire.")
            return

        if redwirecount == 0:
            print("Cut the last wire.")
            return

        print("Cut the fourth wire.")
        return
        
def holdButton():  # ---------------------------------------------BUTTON--------------------
    stripcolor = input("Hold the button and type the color of the strip: ")
    if stripcolor.lower() == "b":
        print("Release the button when the countdown timer has a 4 in any position.")
        return
    elif stripcolor.lower() == "w" or stripcolor.lower() == "r":
        print("Release the button when the countdown timer has a 1 in any position.")
        return
    else:
        print("Release the button when the countdown timer has a 5 in any position.")

def solveButton():
    color = input("Color of the button (bl/bk/r/y/w): ")
    text = input("Text written on the button: ")
    litCAR = False
    litFRK = False

    for indicator in indicators:
        if indicator.lower() == "carlit":
            litCAR = True
        if indicator.lower() == "frklit":
            litFRK = True

    if color.lower() == "bl" and text.lower() == "abort":
        holdButton()
    elif int(NUMBAT) > 1 and text.lower() == 'detonate':
        print("Press and immediately release the button.")
        return
    elif color.lower() == "w" and litCar:
        holdButton()
    elif int(NUMBAT) > 2 and litFRK:
        print("Press and immediately release the button.")
        return
    elif color.lower() == "y":
        holdButton()
    elif color.lower() == "r" and text.lower() == "hold":
        print("Press and immediately release the button.")
        return
    holdButton()

def solveKeypad(): #------------------------------------------KEYPAD-------------------------------------
    col1 = ["q", "at", "lambda", "lightning", "dog", "h", "backwardsc"]
    col2 = ["e", "q", "backwardsc", "loop", "wstar", "h", "upsidedownquestionmark"]
    col3 = ["copyright", "boobs", "loop", "k", "r", "lambda", "wstar"]
    col4 = ["6", "p", "bt", "dog", "k", "upsidedownquestionmark", "smiley"]
    col5 = ["trident", "smiley", "bt", "c", "p", "3", "bstar"]
    col6 = ["6", "e", "puzzlepiece", "ae", "trident", "n", "omega"]

    symbols = []
    for i in range(4):
        symbol = input("Input symbol: ")
        symbols.append(symbol.lower())

    while True:
        correctcol = 0
        numsymbols = 0
        for colsymbol in col1:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 1
            break

        numsymbols = 0
        for colsymbol in col2:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 2
            break

        numsymbols = 0
        for colsymbol in col3:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 3
            break
    
        numsymbols = 0
        for colsymbol in col4:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 4
            break
        
        numsymbols = 0
        for colsymbol in col5:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 5
            break
        
        numsymbols = 0
        for colsymbol in col6:
            for symbol in symbols:
                if symbol.lower() == colsymbol:
                    numsymbols += 1
        if numsymbols == 4:
            correctcol = 6
            break
        
    print("Press the keypads in the following order:\n\n\n\n")
    
    if correctcol == 1:
        for colsymbol in col1:
            for symbol in symbols:
                if symbol == colsymbol:
                    print(colsymbol)
                    break

    if correctcol == 2:
        for colsymbol in col2:
            for symbol in symbols: 
                if symbol == colsymbol:
                    print(colsymbol)
                    break

    if correctcol == 3:
        for colsymbol in col3:
            for symbol in symbols: 
                if symbol == colsymbol:
                    print(colsymbol)
                    break

    if correctcol == 4:
        for colsymbol in col4:
            for symbol in symbols: 
                if symbol == colsymbol:
                    print(colsymbol)
                    break

    if correctcol == 5:
        for colsymbol in col5:
            for symbol in symbols: 
                if symbol == colsymbol:
                    print(colsymbol)
                    break
  
    if correctcol == 6:
        for colsymbol in col6:
            for symbol in symbols: 
                if symbol == colsymbol:
                    print(colsymbol)
                    break

def solveMemory():
    memory = []

    stage1 = input("Input display number followed by all the button labels in order: ")

    if int(stage1[0]) == 1:
        memory.append(stage1[2] + "2")
        print("Press " + stage1[2]) 
    elif int(stage1[0]) == 2:
        memory.append(stage1[2] + "2")
        print("Press " + stage1[2])
    elif int(stage1[0]) == 3:
        memory.append(stage1[3] + "3")
        print("Press " + stage1[3])
    elif int(stage1[0]) == 4:
        memory.append(stage1[4] + "4")
        print("Press " + stage1[4])


while True:
    module = input("Input module: ")
    if module.lower() == "wires":
        solveWires()
    if module.lower() == "button":
        solveButton()
    if module.lower() == "keypad":
        solveKeypad()
    if module.lower() == "memory":
        solveMemory()