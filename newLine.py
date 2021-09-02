import globalvar

#When a ">" is detected move the rest of the line to a new element

def pushEnter(linePos, lineLength, lineElement) :
    
    #Check if ">" is at the end of the line
    if linePos+1 != lineLength:
        
        g = lineElement
        p = linePos
        i = 0
        openingTag = ""
        endingTag = ""
        
        parseValue = ""

        #Idenitfy the opening tag
        while(globalvar.input[g][i] != ">"):

            openingTag += globalvar.input[g][i]
            i+=1
        openingTag +=">"

        #Loop to the end of the item then add it to a new line

        while(p < lineLength-1 and globalvar.input[g][p+1] != "<" and globalvar.input[g][p+2] != "/"):

            p+=1
            parseValue += globalvar.input[g][p]
        while(p < lineLength-1):
            p+=1
            endingTag += globalvar.input[g][p]

        globalvar.input.insert(g+1, openingTag)
        globalvar.input.insert(g+2, parseValue)
        globalvar.input.insert(g+3, endingTag)
        del globalvar.input[g]