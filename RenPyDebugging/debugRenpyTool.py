

with open('day00.rpy', 'r') as data_file:
     
    # open output textfile file in append mode
    #use append since the new file is empty, use write when overwriting existing text
    with open('debugday00.rpy', 'a') as output_file:
         
        # read each line from input text file
        menuInitial=False
        menuLine=False
        menuWhitespace=100
        for line in data_file:

            if len(line) > 1 and line[0] == ' ': #checking for whitespace
                temp = line.lstrip()
                if(menuLine):                   #It'd be nice to have the menu options be available in the debug page
                    if(menuInitial):            #not the cleanest way to check for whether it's in the menu space, but it works
                        menuWhitespace= len(line)-len(temp)
                        menuInitial=False
                        output_file.write(line)
                    elif(len(line)-len(temp)==menuWhitespace):  #the menu options
                        output_file.write(line)
                        menuInitial=False
                    elif(len(line)-len(temp)>menuWhitespace):  #the text within the menu options
                        menuInitial=False
                        if temp[0:2] == "if":
                            output_file.write(line)
                        elif temp[0:1] == "$":
                            output_file.write(line)
                        elif temp[0:4] == "else":
                            output_file.write(line)
                        elif temp[0:4] == "jump":
                            output_file.write(line)
                        elif temp[0:4] == "menu":
                            output_file.write(line)
                            menuInitial=True
                        elif temp[0:5] == "label":
                            output_file.write(line)
                    else:                                   #exiting the menu space
                        menuLine=False
                        menuInitial=False
                        menuWhitespace=100
                        if temp[0:2] == "if":
                            output_file.write(line)
                        elif temp[0:1] == "$":
                            output_file.write(line)
                        elif temp[0:4] == "else":
                            output_file.write(line)
                        elif temp[0:4] == "jump":
                            output_file.write(line)
                        elif temp[0:4] == "menu":
                            output_file.write(line)
                            menuLine=True
                            menuInitial=True
                        elif temp[0:5] == "label":
                            output_file.write(line)
                elif temp[0:2] == "if":                 #checking for if statements
                    output_file.write(line) 
                elif temp[0:1] == "$":                  #checking for variable changes 
                    output_file.write(line)            
                elif temp[0:4] == "else":               #checking for else statements
                    output_file.write(line)             
                elif temp[0:4] == "jump":               #checking for jump statements
                    output_file.write(line)             
                elif temp[0:4] == "menu":               #checking for menu space
                    output_file.write(line)
                    menuLine=True
                    menuInitial=True
                elif temp[0:5] == "label":              #checking for label statements for readability
                    output_file.write(line)
            else:                                       #no whitespace, and definitly not menuspace anymore
                menuLine=False
                menuInitial=False
                menuWhitespace=100
                if line[0:2] == "if":
                    output_file.write(line)
                elif line[0:1] == "$":
                    output_file.write(line)
                elif line[0:4] == "else":
                    output_file.write(line)
                elif line[0:4] == "jump":
                    output_file.write(line)
                elif line[0:4] == "menu":
                    output_file.write(line)
                    menuLine=True
                    menuInitial=True
                elif line[0:5] == "label":
                    output_file.write(line)


