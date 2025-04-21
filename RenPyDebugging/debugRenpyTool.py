

with open('day00.rpy', 'r') as data_file:
     
    # open output.txt file in append mode
    #use append since the new file is empty, use write when overwriting existing text
    with open('debugday00.rpy', 'a') as output_file:
         
        # read each line from data.txt
        for line in data_file:
            # or I guess you could just remove whitespace, check, then add it back... but that feels inefficient
            # more reliably just strip both whitespace, the comment symbol, and check for if it's the right kind of uncomment

            if len(line) > 1 and line[0] == ' ':
                temp = line.lstrip()
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
                elif temp[0:5] == "label":
                    output_file.write(line)
            else: 
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
                elif line[0:5] == "label":
                    output_file.write(line)


