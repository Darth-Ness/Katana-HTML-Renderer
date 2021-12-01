
 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse, isOnline, fileName) :
    i,u = 0,0
    length = len(toParse)+3
    while (i < length):
        while(u < len(toParse[i])):

            if toParse[i][u] == ">":
                pushEnter(u, len(toParse[i]), i, toParse)
            u+=1
        i+=1
        u = 0

    #Invoke the renderer
    import renderMain
    renderMain.startWindow(toParse, isOnline, fileName)

#When a ">" is detected move the rest of the line to a new element

def pushEnter(linePos, lineLength, lineElement, list) :
    
    #Check if ">" is at the end of the line
    if linePos+1 != lineLength:

        #Idenitfy the opening tag
        openingTag = list[lineElement][0: list[lineElement].find(">")]

        parseValue = list[lineElement][linePos+1: lineLength]
        list.insert(lineElement+1, openingTag)
        list.insert(lineElement+2, parseValue)
        del list[lineElement]