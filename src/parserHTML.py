
 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse, isOnline, fileName) :
    i,x = 0,0
    while (i < len(toParse)):
        x=0
        for u in toParse[i]:
            if u == ">": pushEnter(len(toParse[i]), i, toParse,x);x-=1
            x+=1
        i+=1

    #Invoke the renderer
    from renderMain import startWindow
    startWindow(toParse, isOnline, fileName)

#When a ">" is detected move the rest of the line to a new element

def pushEnter(Llen, i, list,x) :
    if x+1 != Llen:
        #Idenitfy the opening tag
        openingTag = list[i][0: list[i].find(">")]

        parseValue = list[i][x+1: Llen]
        list.insert(i+1, openingTag)
        list.insert(i+2, parseValue)
        del list[i]