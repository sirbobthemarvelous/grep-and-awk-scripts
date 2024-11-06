

with open('OriginalScript.rpy', 'r') as data_file:
     
    # open output.txt file in append mode
    #use append since the new file is empty, use write when overwriting existing text
    with open('script.rpy', 'a') as output_file:
         
        # read each line from data.txt
        for line in data_file:
            #line = line.lstrip('#') this only works if you ignore the tab thing
            #if line[0] == '#':     # the tab thing stops this from functioning
                #line = line[1:]
            #if line.lstrip()[0] == '#': you can't combine the indexing and function
            """if len(line) > 4:
                if line[4] == '#':
                    line = line[5:] """
            # or I guess you could just remove whitespace, check, then add it back... but that feels inefficient
            # more reliably just strip both whitespace, the comment symbol, and check for if it's the right kind of uncomment
            if len(line) > 1 and line[0] == ' ':
                line = line.lstrip()
                if line[0:4] == "#edit":
                    line = ''
                elif line[0:1] == "#":
                    line = line.lstrip('#')
            line = line.lstrip('#')
            # it into output file
            output_file.write(line) #you could do line.upper() if you wanted everything to yell lmao
