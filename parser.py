import renderMain

 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse) :
    i = 0
    u = 0
    if ">" in toParse[i]:

        #Scan for a ">"

        while (i < len(toParse)):
        
            while(u < len(toParse[i])):

                if toParse[i][u] == ">":
                    pushEnter(u, len(toParse[i]), i, toParse)
                u+=1
            i+=1
            u = 0
    #Invoke the renderer
    renderMain.startWindow(toParse)
    
def pushEnter(linePos, lineLength, lineElement, list) :
    
    #Check if ">" is at the end of the line
    if linePos+1 != lineLength:
        
        g = lineElement
        p = linePos
        i = 0
        openingTag = ""
        endingTag = ""
        
        parseValue = ""
        #Idenitfy the opening tag

        while(list[g][i] != ">"):
            openingTag += list[g][i]
            i+=1
        openingTag +=">"

        #Loop to the end of the item then add it to a new line
        while(p < lineLength-2 and list[g][p+1] != "<" and list[g][p+2] != "/"):

            p+=1
            parseValue += list[g][p]
        while(p < lineLength-1):
            p+=1
            endingTag += list[g][p]

        list.insert(g+1, openingTag)
        list.insert(g+2, parseValue)
        list.insert(g+3, endingTag)
        del list[g]