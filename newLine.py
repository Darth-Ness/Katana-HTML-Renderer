#When a ">" is detected move the rest of the line to a new element

def pushEnter(linePos, lineLength, lineElement, list) :
    
    #Check if ">" is at the end of the line
    if linePos+1 != lineLength:
        
        g = lineElement
        p = linePos
        i = 0
        openingTag = ""
        endingTag = ""
        
        parseValue = ""
        #print(list)
        #Idenitfy the opening tag
        while(list[g][i] != ">"):

            openingTag += list[g][i]
            i+=1
        openingTag +=">"

        #Loop to the end of the item then add it to a new line

        while(p < lineLength-1 and list[g][p+1] != "<" and list[g][p+2] != "/"):

            p+=1
            parseValue += list[g][p]
        while(p < lineLength-1):
            p+=1
            endingTag += list[g][p]

        list.insert(g+1, openingTag)
        list.insert(g+2, parseValue)
        list.insert(g+3, endingTag)
        del list[g]