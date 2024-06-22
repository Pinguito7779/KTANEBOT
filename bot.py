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
    elif color.lower() == "w" and litCAR:
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
    labels = []
    positions = []

    stage1 = str(input("Input the display number followed by all of the buttons from left to right: "))
    if stage1[0] == "1":
        positions.append("2")
        labels.append(stage1[2])
        print("Press " + stage1[2])

    elif stage1[0] == "2":
        positions.append("2")
        labels.append(stage1[2])
        print("Press " + stage1[2])

    elif stage1[0] == "3":
        positions.append("3")
        labels.append(stage1[3])
        print("Press " + stage1[3])

    elif stage1[0] == "4":
        positions.append("4")
        labels.append(stage1[4])
        print("Press " + stage1[4])

    stage2 = input("Input the display number followed by all of the buttons from left to right: ")

    if stage2[0] == "1":
        position = str(input("Press 4 and input it's position: "))
        positions.append(position)
        labels.append("4")

    elif stage2[0] == "2":
        position = positions[0]
        positions.append(position)
        labels.append(stage2[int(position)])
        print("Press " + stage2[int(position)])

    elif stage2[0] == "3":
        positions.append("1")
        labels.append(stage2[1])
        print("Press " + stage2[1])

    elif stage2[0] == "4":
        position = positions[0]
        positions.append(position)
        labels.append(stage2[int(position)])
        print("Press " + stage2[int(position)])

    stage3 = str(input("Input the display number followed by all of the button from left to right: "))

    if stage3[0] == "1":
        label = labels[1]
        position = input("Press " + labels[1] + " and input it's position: ")
        positions.append(position)

    elif stage3[0] == "2":
        label = labels[0]
        position = input("Press " + labels[0] + " and input it's position: ")
        positions.append(position)

    elif stage3[0] == "3":
        labels.append(stage3[3])
        positions.append("3")
        print("Press " + stage3[3])

    elif stage3[0] == "4":
        labels.append("4")
        position = input("Press 4 and input it's position: ")
        positions.append(position)

    stage4 = str(input("Input the display number followed by all of the buttons from left to right: "))

    if stage4[0] == "1":
        position = positions[0]
        labels.append(stage4[int(position)])
        print("Press " + stage4[int(position)])

    elif stage4[0] == "2":
        positions.append("1")
        labels.append(stage4[1])
        print("Press " + stage4[1])

    elif stage4[0] == "3":
        position = positions[1]
        positions.append(position)
        labels.append(stage4[int(position)])
        print("Press " + stage4[int(position)])

    elif stage4[0] == "4":
        position = positions[1]
        labels.append(stage4[int(position)])
        print("Press " + stage4[int(position)])

    stage5 = str(input("Input the display number followed by all of the buttons from left to right: "))

    if stage5[0] == "1":
        print("Press " + labels[0])
    elif stage5[0] == "2":
        print("Press " + labels[1])
    elif stage5[0] == "3":
        print("Press " + labels[3])
    elif stage5[0] == "4":
        print("Press " + labels[2])
       

def solveSimonSays():
    vowel0 = ["Blue", "Red", "Yellow", "Green"]
    vowel1 = ["Yellow", "Green", "Blue", "Red"]
    vowel2 = ["Green", "Red", "Yellow", "Blue"]
    novowel0 = ["Blue", "Yellow", "Green", "Red"]
    novowel1 = ["Red", "Blue", "Yellow", "Green"]
    novowel2  = ["Yellow", "Green", "Blue", "Red"]

    hasVowel = False
    numStrikes = input("Input the number of strikes the bomb has: ")
    done = False

    for l in SERIAL_NUMBER:
        if l.lower() == "a" or l.lower() == "e" or l.lower() == "i" or l.lower() == "o" or l.lower() == "u":
            hasVowel = True
    while done == False:
        sequence = input("Input the sequence of flashes in order (r, b, g, y) / done: ")
        if sequence.lower() == "done":
            break
        print("Press in the following order:\n")

        if hasVowel == True:
            if numStrikes == "0":
                for color in sequence:
                    if color.lower() == "r": print(vowel0[0])
                    if color.lower() == "b": print(vowel0[1])
                    if color.lower() == "g": print(vowel0[2])
                    if color.lower() == "y": print(vowel0[3])
            if numStrikes == "1":
                for color in sequence:
                    if color.lower() == "r": print(vowel1[0])
                    if color.lower() == "b": print(vowel1[1])
                    if color.lower() == "g": print(vowel1[2])
                    if color.lower() == "y": print(vowel1[3])
            if numStrikes == "2":
                for color in sequence:
                    if color.lower() == "r": print(vowel2[0])
                    if color.lower() == "b": print(vowel2[1])
                    if color.lower() == "g": print(vowel2[2])
                    if color.lower() == "y": print(vowel2[3])

        if hasVowel == False:
            if numStrikes == "0":
                for color in sequence:
                    if color.lower() == "r": print(novowel0[0])
                    if color.lower() == "b": print(novowel0[1])
                    if color.lower() == "g": print(novowel0[2])
                    if color.lower() == "y": print(novowel0[3])
            if numStrikes == "1":
                for color in sequence:
                    if color.lower() == "r": print(novowel1[0])
                    if color.lower() == "b": print(novowel1[1])
                    if color.lower() == "g": print(novowel1[2])
                    if color.lower() == "y": print(novowel1[3])
            if numStrikes == "2":
                for color in sequence:
                    if color.lower() == "r": print(novowel2[0])
                    if color.lower() == "b": print(novowel2[1])
                    if color.lower() == "g": print(novowel2[2])
                    if color.lower() == "y": print(novowel2[3])


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
    if module.lower() == "simon says":
        solveSimonSays()
