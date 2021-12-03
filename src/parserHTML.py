
 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse, isOnline, fileName) :
    i,u = 0,0
    while (i < len(toParse)):
        while(u < len(toParse[i])):

            if toParse[i][u] == ">":
                pushEnter(u, len(toParse[i]), i, toParse)
            u+=1
        i+=1
        u = 0

    #Invoke the renderer
    from renderMain import startWindow
    startWindow(toParse, isOnline, fileName)

#When a ">" is detected move the rest of the line to a new element

def pushEnter(u, Llen, i, list) :
    
    #Check if ">" is at the end of the line
    if u+1 != Llen:

        #Idenitfy the opening tag
        openingTag = list[i][0: list[i].find(">")]

        parseValue = list[i][u+1: Llen]
        list.insert(i+1, openingTag)
        list.insert(i+2, parseValue)
        del list[i]